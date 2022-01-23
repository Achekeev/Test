<h1>Develops Test Task</h1>

Postman link https://www.getpostman.com/collections/7336c2bb2ed1e8a7e126

Code formatted with black

To run on local machine:
1) Create a virtual environment(venv, pipenv or poetry)
2) Install requirements(pip3 install -r requirements)
3) Make migrations(python3 manage.py makemigrations && python3 manage migrate)
4) Create Super User(python3 manage.py createsuperuser)
5) Run the local Server(python3 manage.py runserver)


To run with docker:
1) Install Docker, Docker-compose
2) Build(docker-compose build)
3) Start(docker-compose up -d)
4) Make migrations(docker-compose exec web ./manage.py makemigrations(migrate))
5) Create Super User(docker-compose exec web ./manage.py createsuperuser)
