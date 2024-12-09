```sh
    psql -U postgres -h localhost -W
```

If poetry not workig add on terminal

```sh
    $env:Path += ";$env:USERPROFILE\AppData\Roaming\Python\Python313\Scripts"
```

Init uvicorn:

```sh
poetry run uvicorn app.main:app --reload
```
