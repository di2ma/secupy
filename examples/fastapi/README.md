### Activate your host

```bash
python -m secupy activate --token xxxxxx --label boilerplate
```

### Build your source code

```bash
python -m secupy build -s src -d protected_src -u entrypoint.py
```

### Execute protected code

> Go to protected_src folder and execute:

```bash
uvicorn entrypoint:app
```

### Test yout first protected Fastapi app

> Open your preferred browser and go to http://127.0.0.1:8000/ or http://127.0.0.1:8000/items/10?q=team_license_hosts
