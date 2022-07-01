### Activate your host

```bash
python -m secupy activate --token xxxxxx --label boilerplate
```

### Build your source code

```bash
python -m secupy build -s src -d protected_src -u manage.py
```

### Execute protected code

> Go to protected_src folder and execute:

```bash
secupy -m manage runserver 0.0.0.0:8000
```

or
```bash
python -m manage runserver 0.0.0.0:8000
```

> Use with 'django' module instead of 'manage.py' need 'usercustomize.py':

```bash
echo "import secupy" > usercustomize.py
```

```bash
PYTHONPATH=. secupy -m django runserver --settings='secupy_django_boilerplate.settings'
```

or

```bash
PYTHONPATH=. python -m django runserver --settings='secupy_django_boilerplate.settings'
```
or

```bash
export DJANGO_SETTINGS_MODULE='secupy_django_boilerplate.settings'
PYTHONPATH=. secupy -m django runserver 0.0.0.0:8000
```

or

```bash
export DJANGO_SETTINGS_MODULE='secupy_django_boilerplate.settings'
PYTHONPATH=. python -m django runserver
```

### Test yout first protected Django app

> Open your preferred browser and go to http://127.0.0.1:8000/core/homepage/ 
