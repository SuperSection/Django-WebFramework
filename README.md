## How to install Tailwind in Django

**Firstly install pip in the virtual environment (*if required*)** : use any one of the below command
- `python -m pip install --upgrade pip`
- `python -m ensurepip --upgrade`

### To install Tailwind
- `uv pip install django-tailwind`
- `uv pip install 'django-tailwind[reload]'`

- `python manage.py tailwind init`

<br>

**After thar in settings.py**

Set NPM_BIN_PATH = 'C:/Program Files/nodejs/npm.cmd'
<br>Change it according to your OS

add in INSTALLED_APPS : <br>
[ 'tailwind', 'theme', 'django_browser_reload' ]

add MIDDLEWARE : <br>
[ 'django_browser_reload.middleware.BrowserReloadMiddleware' ]

<br>

**in urls.py** 
add a urlpatterns: <br>
[ path("__ reload __/", include("django_browser_reload.urls")) ]

Then run the following command and start tailwind along with the server
- `python manage.py tailwind install`
- `python manage.py tailwind start`

