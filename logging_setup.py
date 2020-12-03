""" Logging: A Usage Guide

Assume you have a folder structure like so:

```bash
.
├── LICENSE
├── example
│   └── yo.py
├── logging_setup.py
└── main.py
```

All you'd have to do to setup the logger would be to:
```python
# in main.py
from logging_setup import setup_log
setup_log()
...
# in example/yo.py
from logging import log
log(50, "yo")
```

This will result in a `.logs/warnings.log` file being created, with each line
having an output similar to:

```
[2020-06-02 12:03:24,171]  CRITICAL { /path/to/yo.py:3  } - yo
```

The `/path/to/yo.py:3` format is very useful, as you can just ctrl-click it to
open it directly in VSC!

Note: There's no getLogger shenanigans!

Note 2: The rotating file handler ensures no log file will be over 5MB long!
This is the default maximum for VSC, as it'll get quite confused if a text
file is longer than 5MB

## Using the wrapper

Using the wrapper will allow us to quickly inspect all function calls!
It's basically a fancy print

* Usage:

```python
from logging_setup import log_wrapper

@log_wrapper()
def yo(arg, key_arg=0):
    return arg + key_arg

yo(0)
yo(0, key_arg=5)
yo('aze')
```

Would produce:

```python
[2020-06-02 ...]  WARNING { /path/to:118  }
    Function yo called with following params: (0,), {}
[2020-06-02 12:51:04,205]  WARNING { /path/to:118  }
    Function yo called with following params: (0,), {'key_arg': 5}
[2020-06-02 12:51:04,206]  WARNING { /path/to:118  }
    Function yo called with following params: ('aze',), {}
[2020-06-02 12:51:04,206]  ERROR { /path/to:122  }
    can only concatenate str (not "int") to str
Traceback (most recent call last):
  File "/path/to", line 120, in wrapper
    return func(*args, **kwargs)
  File "/path/to", line 6, in yo
    return arg + key_arg
TypeError: can only concatenate str (not "int") to str
```

"""
from functools import wraps, partial
import logging
from logging import WARNING
import logging.config
from typing import Dict, Any, Callable, Optional
from pathlib import Path

Logging_Keys = Any
λ = Callable[..., Any]

_default_log_file = "./logs/warnings.log"
_default_file_log_level = "WARNING"
_default_console_log_level = "DEBUG"

# Saying it's a Dict: Any is not very useful,
# Check out the proper documentation over at:
# https://docs.python.org/3/library/logging.config.html?#configuration-dictionary-schema
CONFIG: Dict[str, Logging_Keys] = {
    "disable_existing_loggers": False,
    "version": 1,
    "formatters": {
        "short": {
            "format": (
                "[%(asctime)s]  %(levelname)s "
                "{ %(pathname)s:%(lineno)d  }\n\t%(message)s"
            )
        },
    },
    "handlers": {
        "console": {
            "level": _default_console_log_level,
            "formatter": "short",
            "class": "logging.StreamHandler",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": _default_file_log_level,
            "formatter": "short",
            "filename": "./logs/warnings.log",
            "maxBytes": 5_242_880,  # 5MB
            "backupCount": 10,
            "encoding": "utf8",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
        },
        "plugins": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}


def setup_log() -> None:
    # Will create the log file and directory if it doesn't exist
    filename = Path(_default_log_file)
    filename.parent.mkdir(parents=True, exist_ok=True)
    filename.touch(exist_ok=True)
    logging.config.dictConfig(CONFIG)


def _attach_wrapper(obj: Any, func: Optional[λ] = None) -> λ:
    """Helper function that attaches function as attribute of an object"""
    if func is None:
        return partial(_attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def log_wrapper(level: int = WARNING) -> λ:
    """Wrap any function so you can log all function calls! Wow

    Usage example:

    ```python
    from logging_setup import log_wrapper

    @log_wrapper(50) # That would be critical level
    def yo(arg, key_arg=0):
        return arg + key_arg

    yo(0)
    yo(0, key_arg=5)
    yo('aze')
    ```

    """

    def decorate(func: λ) -> λ:
        setup_log()
        logger = logging.getLogger(func.__module__)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.log(
                level,
                (
                    f"Function {func.__name__} called with "
                    f"following params: {args}, {kwargs}"
                ),
            )
            try:
                return func(*args, **kwargs)
            except BaseException as e:
                logger.error(e, exc_info=True)
                raise e

        return wrapper

    return decorate
