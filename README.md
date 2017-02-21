# datastore_demo
Datastore demo

## Setup

### Ensure Python 2.7 is on your path:
```
python --version
```
If missing or wrong version, install from [https://www.python.org/downloads/](https://www.python.org/downloads/) and add to your path.

### Create a virtual environment
- Verify that `virtualenv` is installed:
```
virtualenv --help
```

- If it is not installed, installed it with `pip`:
```
pip install virtualenv
```

- Create the virtual environment `venv`
```
virtualenv venv
```

- Activate the virtual environment
    - Windows DOS command: `venv\scripts\activate.bat`
    - Windows Powershell: `venv\scripts\activate.ps1`
    - Bash: `source venv/bin/activate`

### Install requirements
```
pip install -r requirements.txt
```

## Run locally

From command line (DOS, Powershell, bash):
```
./demo.sh
```
