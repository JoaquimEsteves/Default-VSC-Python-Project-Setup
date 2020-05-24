# Default-VSC-Python-Project-Setup
Easy setup for python projects with visual studio code


The `setup.cfg` should be dropped in your main project directory, and the settings.json should go into the
`.vsc` folder


### Mandatory Pip installs

```
python3 -m pip install mypy mypy-extensions autopep8 flake8 flake8-mypy
```

Note: Always type `path/to/python -m pip` so you'll know where  you _actually_ installed your pip packages.
