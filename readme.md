# (dvmn) Yandex.Afisha

Project created to share interesting Moscow places and give some information about it.
Starting server create map, where marked places from database with their description and photos.
Link for working site: [alexnv.pythonanywhere.com](https://alexnv.pythonanywhere.com/)

## Preview

![img.png](static/images/site_preview.png)

## Install

 1. Clone repository:

```commandline
https://github.com/alexnv/18-dvmn-yandex-afisha
```

 2. Install requirements:

```commandline
pip install -r requirements.txt
```

3. Create `.env` (example):

```commandline
SECRET_KEY=django-insecure-b5et!+...           # secret key of your Django-project
DEBUG=true                                     # true or false
ALLOWED_HOSTS=127.0.0.1, .pythonanywhere.com   # hosts. For local: 127.0.0.1

STATIC_URL=/static/                            # your static files url
STATIC_ROOT=static                             # your static files dir name

MEDIA_URL=/media/                              # media files url.  Format: '/media_url/'
MEDIA_ROOT=media                               #media files dir name
```

 4. Make migrations:

```commandline
python3 manage.py migrate
```

 5. Create super user to django access:

```commandline
python3 manage.py createsuperuser

```

6. run on pythonanywhere.com
```commandline
python3 manage.py collectstatic 
```
