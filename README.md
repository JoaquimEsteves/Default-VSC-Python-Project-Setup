# Default-VSC-Python-Project-Setup

Easy setup for python projects with visual studio code

The `mypy.cfg` should be dropped in your main project directory

### Provisioning of the virtual environment

Create the environment

```
python3 -m venv env
```

or

```
virtualenv -p python3 env
```

Activate the environment

```
source env/bin/activate
```

Install the libraries

```
pip install -r requirements.txt
```

### Vscode plug-ins install snippets

save plug-ins to a .txt:

code --list-extensions > vscode.txt

install plug-ins from the .txt:

cat vscode.txt | xargs -n 1 code --install-extension
