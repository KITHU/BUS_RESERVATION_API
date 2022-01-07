[![Build Status](https://app.travis-ci.com/KITHU/SHOP_API.svg?branch=develop)](https://app.travis-ci.com/KITHU/SHOP_API)
[![Coverage Status](https://coveralls.io/repos/github/KITHU/SHOP_API/badge.svg?branch=develop)](https://coveralls.io/github/KITHU/SHOP_API?branch=develop)

# **RBAC-Api**
### **API Documentation**
- This is a sample api using drf, It has three types of users admin, managers and cashier

  - [swagger documentation](https://shop-api-v1.herokuapp.com/)

## **Set Up Development Environment:**
- Clone the repo and cd into it:
- Make a copy of the .env.sample file and rename it to .env and update the variables accordingly
- Activate a virtual environment:
  ```
    pipenv shell
  ```

- Install all Dependancies
  ```
   pipenv install 
  ```
- Apply migrations:
  ```
    python manage.py migrate

  ```
  - Create admin user
  ```
    python manage.py createsuperuser
  ```

- Run App
  ```
    python manage.py runserver
  ```

- Run Tests
  ```
    pytest
  ```

### test user details
```
  email: test@test.com
  password: test1234

```
## **Endpoints:**
### Register

`POST /api/v1/auth/register/`

Example request body:
``` 
{
    "username":"doe",
    "email":"doe@gmail.com",
    "role" : 1,
    "password":"1234"
    "user_manager": user_id
}

Nb: role is optional field, by default a cashier role three will be created

admin = 1
manager = 2
cashier = 3
```

### Login
`POST /api/v1/auth/login/`

Example request body:
``` 
{
    "email":"doe@gmail.com",
    "password":"1234"
}
```

## **users**
### List 
`GET /api/v1/auth/users/`

```
  This endpoint will return all users
  Response can be filtered to return all admin, managers or cashiers
  Response can be filtered to return all user who are sharing the same manager
```

### List 
`GET /api/v1/auth/users/`

```
  This endpoint will return all sub_users
  Response can be filtered to return all sub_users who are either admin, managers or cashiers 
```