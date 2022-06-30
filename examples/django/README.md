python -m secupy activate --token xxxxxx --label boilerplate
python -m secupy build -s .\src\ -d .\protected_src\ -v --exclude **\__pycache__
enter in protected_src folder and execute:
secupy -m manage runserver 0.0.0.0:8000 or python -m secupy -m manage runserver 0.0.0.0:8000

open browser on http://127.0.0.1:8000/core/homepage/ 