# Setup && Deploy

```sh
    psql -U postgres -h localhost -W
```

## Install Poetry

```sh
pip install poetry
```

cd to current root directory && run:

```sh
poetry install
```

If poetry not workig add on terminal

```sh
    $env:Path += ";$env:USERPROFILE\AppData\Roaming\Python\Python313\Scripts"
```

If you want to mantain the poetry path on your Windows Kernel:

```sh
notepad $PROFILE
```

Insert into PROFILE:

```sh
$env:Path += ";$env:USERPROFILE\AppData\Roaming\Python\Python313\Scripts"
```

Init uvicorn:

```sh
poetry run uvicorn app.main:app --reload
```

## Migration

Para migrar la base de datos mediante sqlalchemy:

```sh
    poetry run python app/db/migrate.py
```

## Test

```sh
    poetry run pytest
```

To run a specific test:

```sh
    poetry run pytest tests/<filename>.py
```
