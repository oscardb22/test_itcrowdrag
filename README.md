## Endpoints Table

| Endpoint | Description | Need Token  |
| -------- | ----------- | ----------- |
| http://localhost:8000/users/sign_in/ | this endpoint make authentication and return the transaction token | NO |
| http://localhost:8000/users/sign_out/ | this endpoint remove transaction token and exit the user | YES |
| http://localhost:8000/users/register/user/ | this endpoint register a system user | YES |
| http://localhost:8000/users/update/< id:int >/user/ | this endpoint update a system user | YES |
| http://localhost:8000/users/list/user/ | this endpoint list all system users | YES |
| http://localhost:8000/movie/register/movie/ | this endpoint register a movie | YES |
| http://localhost:8000/movie/update/< int:id >/movie/ | this endpoint update a movie | YES |
| http://localhost:8000/movie/delete/< int:id >/movie/ | this endpoint delete a movie | YES |
| http://localhost:8000/movie/list/movie/ | this endpoint list all movies | NO |
| http://localhost:8000/person/register/person/ | this endpoint register a person | YES |
| http://localhost:8000/person/update/< int:id >/person/ | this endpoint update a person | YES |
| http://localhost:8000/person/delete/< int:id >/person/ | this endpoint delete a person | YES |
| http://localhost:8000/person/list/person/ | this endpoint list all person | NO |

# Instructions

1. create a virtualenv (optional)

    `virtualenv -p python3.8 env`
    
    `source env/bin/active`
2. install requirements of the requirements.txt file

    `pip install -r requirements.txt`
3. execute the commands makemigrations y migrate for create the BD

    `python manage.py makemigrations users movie person`
    
    `python manage.py makemigrations`
    
    `python manage.py migrate`
4. Create super user

    `python manage.py createsuperuser`
5. Run Django

    `python manage.py runserver`
---
**NOTE**

all transaction need the authentication header token

`Authorization: Token `

```json


```
---