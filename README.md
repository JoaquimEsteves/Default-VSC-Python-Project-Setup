# Default-VSC-Python-Project-Setup

Easy setup for python projects with visual studio code

The `setup.cfg` should be dropped in your main project directory

### Vscode plug-ins install snippets

* Save plug-ins to a .txt:

``` 
$ code --list-extensions > vscode.txt
```

* install plug-ins from the .txt:

``` 
$ cat vscode.txt | xargs -n 1 code --install-extension
```

## Logging: A Usage Guide

Assume you have a folder structure like so:

``` bash
.
├── LICENSE
├── example
│   └── yo.py
├── logging_setup.py
└── main.py
```

All you'd have to do to setup the logger would be to:

``` python
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
[2020-06-02 12:03:24,171]  CRITICAL { /path/to/yo.py:3  } - yo
```

The `/path/to/yo2.py:3` format is very useful, as you can just ctrl-click it to open it directly in VSC!
Note: There's no getLogger shenanigans!
Note 2: The rotating file handler ensures no log file will be over 5MB long!
This is the default maximum for VSC, as it'll get quite confused if a text file is longer than 5MB

### A Short guide to Virtual Environments

Creating a virtual environment is useful so you'll have all of your 
dependencies nicely packaged together.

If you're familiar with `node_modules` they're basically the same thing.
<sup>there's also loads of different [virtual environment setups](https://stackoverflow.com/a/41573588)
<sub>Ok look, you gotta do your research <sup>but don't get me started on <sub><sup>conda!</sup></sub>
</sup>
</sub>
</sup>

You can create a virtual environment like so:

``` bash 
$ python3 -m venv .example_environment_folder

``` 

This will create a folder like so:

```

.example_environment_folder
├── bin
│   ├── activate
│   ├── (...etc)
│   ├── python -> python3
│   └── python3 -> /path/to/python3
├── include
├── lib
│   └── python3.8
│       └── site-packages
│           ├── easy_install.py
│           ├── (barely empty folder)
│           └── (...etc)
├── lib64 -> lib
├── pyvenv.cfg
└── share

    └── python-wheels
        ├── appdirs-1.4.3-py2.py3-none-any.whl
        └── (...etc)

``` 

Notice, that your `env` folder contains a link to whichever python interpreter
you used to create it.

Notice also, that the `include` folder is empty and the `site-packages` is also
practically empty.

This is so that you'll be able to have multiple versions of pip packages with
(hopefully) no conflicts.

You can _manually_ call the `env` python like so:

```bash
$ .example_environment_folder/bin/python
Python 3.X.X (default, Apr 1 2020, 0:00:00) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

You can also _activate_ the environment.
This is useful as it cleans up all of your `PATH` variables.

``` bash
$ source .example_environment_folder/bin/activate
(.example_environment_folder) $ which python
/home/.../etc/.../.example_environment_folder/bin/python
```

Install your libraries with: 

```bash 
(.example_environment_folder) $ pip install -r requirements.txt
``` 

And notice how they're now installed on `.example_environment_folder/lib/python3.X/site-packages` 
