
# **Shop-Api**
### **API Documentation**
- This is a sample api using drf, It has three types of users admin, managers and cashier
  ##### admin
  - admin can create users, products and also delete them.
  ##### manager
  - managers can create products and also manage products
  ##### cashier
  - cashiers can only view products

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

## **products**
### create 
`POST /api/v1/products/product/`

Example request body:
``` 
{
    "name": "vodka",
    "price": 205.00
}
```
Authentication required.

### list
`GET /api/v1/products/product/`

Authentication is not required.

### retrieve 
`GET /api/v1/products/product/<pk:int>`

Authentication not required.

### update 
`UPDATE /api/v1/products/product/<pk:int>`

Authentication IS required.

### delete
`DELETE /api/v1/products/product/<pk:int>`

Authentication IS required.