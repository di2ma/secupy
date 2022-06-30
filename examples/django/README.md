### Activate your host

python -m secupy activate --token xxxxxx --label boilerplate

### Build your source code

python -m secupy build -s .\src\ -d .\protected_src\ -v --exclude **\__pycache__

### Execute protected code

> Go to protected_src folder and execute:

secupy -m manage runserver 0.0.0.0:8000 or python -m secupy -m manage runserver 0.0.0.0:8000

### Test yout first protected Django app

> Open your preferred browser and go to http://127.0.0.1:8000/core/homepage/ 
