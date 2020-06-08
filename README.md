# whatMemeAmI
First we need to install [python](https://www.python.org/downloads/).
   
After that we need to Install [pip](https://pip.pypa.io/en/stable/installing/),
pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from [python.org](https://www.python.org/downloads/) or if you are working in a Virtual Environment created by virtualenv or pyvenv.

Now pip need to install all dependencies for the project.
```
pip install -r requirements.txt
```
Create under the "main" folder an empty folder with following name "database"

Now we need to collect all staticfiles
```
python manage.py collectstatic --no-input --clear
```
Now we need to migrate the Database
```
python manage.py migrate
```

After that we can run following command to start our application.
```
python manage.py runserver --settings=whatMemeAmI.local_settings

```
Our application can be accessed via: [`http://127.0.0.1:8000`](http://127.0.0.1:8000)

If you want to run your production environment with your locally code changes you need to run following commands

Take down old volume
```
docker-compose down -v
```
Build Images (change: fill properties {string, name, pw} must be the same each time you want access the same database)
```
SECRET_KEY=string DATABASE_NAME=name SQL_USER=name SQL_PASSWORD=pw docker-compose -f docker-compose.prod.yml up --build 
```
Create an admin
```
docker-compose -f docker-compose.prod.yml exec whatMeme python manage.py createsuperuser
```

Our application can be accessed via: [`http://localhost:1337/`](http://localhost:1337/)

To run the application in an docker enviroment without nginx and wsgi follow steps above but use following file: 
```
docker-compose.yml instead of docker-compose.prod.yml
```
