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

