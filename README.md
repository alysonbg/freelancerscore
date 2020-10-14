# freelancerscore
![Python application](https://github.com/alysonbg/freelancerscore/workflows/Python%20application/badge.svg)

How to install and run this project locally(Python 3.8 required):
```console
git clone https://github.com/alysonbg/freelancerscore.git
cd freelancerscore
cp contrib/env-sample .env
python -m pip install pipenv
pipenv install -d
docker-compose up -d
python manage.py migrate
python manage.py runserver
```