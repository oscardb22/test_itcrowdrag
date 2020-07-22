## Endpoints Table

| order | Endpoint | Description |
| ----- | -------- | ----------- |

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
3. Run Django

    `python manage.py runserver`
3. Run Django

    `python manage.py runserver`
---
**NOTE**

all transaction need the authentication header token

`Authorization: Token `

```json


```
---