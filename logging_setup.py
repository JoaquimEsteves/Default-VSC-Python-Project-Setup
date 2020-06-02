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

This will result in a `.logs/warnings.log` file being created, with each line having an output similar to:

```
[2020-06-02 12:03:24,171]  CRITICAL { /path/to/yo2.py:3  } - yo
```

The `/path/to/yo2.py:3` format is very useful, as you can just ctrl-click it to open it directly in VSC!

Note: There's no getLogger shenanigans!

Note 2: The rotating file handler ensures no log file will be over 5MB long!
This is the default maximum for VSC, as it'll get quite confused if a text file is longer than 5MB

"""
import logging.config
from typing import Dict, Any
from pathlib import Path

Logging_Keys = Any

_default_log_file = "./logs/warnings.log"

# Saying it's a Dict: Any is not very useful,
# Check out the proper documentation over at:
# https://docs.python.org/3/library/logging.config.html?#configuration-dictionary-schema
CONFIG: Dict[str, Logging_Keys] = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
        'short': {
            'format': "[%(asctime)s]  %(levelname)s { %(pathname)s:%(lineno)d  } - %(message)s"
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'short',
            'class': 'logging.StreamHandler',
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "WARNING",
            "formatter": "short",
            "filename": "./logs/warnings.log",
            "maxBytes": 5_242_880,  # 5MB
            "backupCount": 10,
            "encoding": "utf8"
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
        },
        'plugins': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False
        }
    },
}


def setup_log() -> None:
    # Will create the log file and directory if it doesn't exist
    filename = Path(_default_log_file)
    filename.parent.mkdir(parents=True, exist_ok=True)
    filename.touch(exist_ok=True)
    logging.config.dictConfig(CONFIG)
