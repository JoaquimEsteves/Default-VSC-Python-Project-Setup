# Default-VSC-Python-Project-Setup

Easy setup for python projects with visual studio code

Simply replace all strings named `template` with your own project name!

### Vscode plug-ins install snippets

- Save plug-ins to a .txt:

```
$ code --list-extensions > vscode.txt
```

- install plug-ins from the .txt:

```
$ cat vscode.txt | xargs -n 1 code --install-extension
```

## Installing

The recommended tool for using this template is [poetry](https://python-poetry.org/docs/basic-usage/)

Running `poetry shell` will also allow you easy access to `black`, `mypy`, `isort`, `flake8`

Example:

```bash
$ poetry shell
Creating virtualenv template-(...) in /home/username/.cache/pypoetry/virtualenvs
Spawning shell within /home/username/.cache/pypoetry/virtualenvs/template-(...)
. /home/username/.cache/pypoetry/virtualenvs/template-(...)/bin/activate
$ mypy src
src/template/example.py:11: error: Incompatible return value type (got "str", expected "int")
Found 1 error in 1 file (checked 3 source files)
$ flake8 src
(...)
src/template/example.py:11:21: W292 no newline at end of file
$ black src
reformatted /home/.../src/template/example.py
All done! ✨ 🍰 ✨
1 file reformatted, 3 files left unchanged.
$ isort


                 _                 _
                (_) ___  ___  _ __| |_
                | |/ _/ / _ \/ '__  _/
                | |\__ \/\_\/| |  | |_
                |_|\___/\___/\_/   \_/

      isort your imports, so you don't have to.

(...)
```

## Testing

If you've used poetry simply run `poetry run pytest tests`.

The `test_version` test should fail until you set your own environment variable

```bash
$ poetry run pytest tests
=============================================== test session starts ===============================================
platform linux -- Python 3.8.5, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /home/lab-ubuntu/Projects/Default-VSC-Python-Project-Setup
collected 3 items

tests/test_template.py F..                                                                                  [100%]

==================================================== FAILURES =====================================================
__________________________________________________ test_version ___________________________________________________

    def test_version() -> None:
        """
        Tests getting variables from the environment
        """
>       assert __version__ == "0.1.0"
E       AssertionError: assert None == '0.1.0'

tests/test_template.py:12: AssertionError
============================================= short test summary info =============================================
FAILED tests/test_template.py::test_version - AssertionError: assert None == '0.1.0'
=========================================== 1 failed, 2 passed in 0.12s ===========================================
```

## Logging

This project comes prepackaged with a set of sane defaults for logging.
See the source file and `__docs__` over on `logging_setup.py` if you're
interested

### A Short guide to Virtual Environments

_If_ you don't feel like using poetry or you're new to python's whole packaging
shenanigans then I'd still recommend to use a **Virtual Envirnoment**.

Creating a virtual environment is useful so you'll have all of your
dependencies nicely packaged together.

If you're familiar with `node_modules` they're basically the same thing.
<sup>there's also loads of different [virtual environment setups](https://stackoverflow.com/a/41573588)
<sub>Ok look, you gotta do your research <sup>but don't get me started on <sub><sup>conda!</sup></sub>
</sup>
</sub>
</sup>

You can create a virtual environment like so:

```bash
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

```bash
$ source .example_environment_folder/bin/activate
(.example_environment_folder) $ which python
/home/.../etc/.../.example_environment_folder/bin/python
```

Install your libraries with:

```bash
(.example_environment_folder) $ pip install -r requirements.txt
```

And notice how they're now installed on `.example_environment_folder/lib/python3.X/site-packages`
