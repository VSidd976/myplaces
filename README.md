# myplaces

## Instalation

Use **git** to install myplaces.

```bash
git clone https://github.com/VSidd976/myplaces.git
```

### Dependencies

* **Python 3.12 or later**
* **Django**

Create **virtual env** and use **pip** to install dependencies.

```bash
pip install -r requirements.txt
```

## Executing

Execute following commands to apply migrations and run server.

```bash
cd myplaces
python manage.py migrate
python manage.py runserver
```

Ctrl/command + left click on the local address to open ui in browser.
