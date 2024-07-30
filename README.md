# Django based Bitcoin price alert system (redis , postgres)
#### you can create bitcoin price targets , if targets are met you will recieve email.
> [!IMPORTANT]
> ### Usage
> - i will soon dockerize and docker-compose this project for ease of use.
> - establish redis server on your system , i am currently running it on docker and binded to port 9000
> - install or have docker image of postgresql , create database test
> - make sure you have all dependencies mentioned in requirements.txt
> - this application uses JWT based authentication.
> - type python manage.py runserver for running the application.

> [!TIP]
> ### endpoints
> - post  http://127.0.0.1:8000/api/token/  for jwt based token generation.
> - post  http://127.0.0.1:8000/alerts/create/ for creating alerts
>   - body {
  "target_price": "67000.00",
  "email": "user@example.com"
}  
> - get http://127.0.0.1:8000/alerts/fetch/ for fetching alerts triggered or non - triggered
> - del http://127.0.0.1:8000/alerts/delete/n/  replace n with id of entry you want to delete , this will delete the alert
> [!NOTE]
│   sample.py
│
└───price
    │   db.sqlite3
    │   manage.py
    │   requirements.txt
    │
    ├───myapp
    │   │   admin.py
    │   │   apps.py
    │   │   binance_websocket.py
    │   │   models.py
    │   │   serializers.py
    │   │   tests.py
    │   │   urls.py
    │   │   views.py
    │   │   __init__.py
    │   │
    │   ├───migrations
    │   │   │   0003_initial.py
    │   │   │   0004_alter_alert_id.py
    │   │   │   __init__.py
    │   │   │
    │   │   └───__pycache__
    │   │           0001_initial.cpython-310.pyc
    │   │           0002_initial.cpython-310.pyc
    │   │           0003_initial.cpython-310.pyc
    │   │           0004_alter_alert_id.cpython-310.pyc
    │   │           __init__.cpython-310.pyc
    │   │
    │   └───__pycache__
    │           admin.cpython-310.pyc
    │           apps.cpython-310.pyc
    │           models.cpython-310.pyc
    │           serializers.cpython-310.pyc
    │           urls.cpython-310.pyc
    │           views.cpython-310.pyc
    │           __init__.cpython-310.pyc
    │
    └───price
        │   asgi.py
        │   settings.py
        │   urls.py
        │   wsgi.py
        │   __init__.py
        │
        └───__pycache__
                settings.cpython-310.pyc
                urls.cpython-310.pyc
                wsgi.cpython-310.pyc
                __init__.cpython-310.pyc

