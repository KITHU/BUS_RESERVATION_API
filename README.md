[![Build Status](https://app.travis-ci.com/KITHU/SHOP_API.svg?branch=develop)](https://app.travis-ci.com/KITHU/SHOP_API)
[![Coverage Status](https://coveralls.io/repos/github/KITHU/SHOP_API/badge.svg?branch=develop)](https://coveralls.io/github/KITHU/SHOP_API?branch=develop)

# **BUS RESERVATION-Api**
### **API Documentation**
- This is a sample api using drf, It has two types of users admin and customers
  - [swagger documentation](https://shop-api-v1.herokuapp.com/)

## **Set Up Development Environment:**
- Clone the repo and cd into it:
- Make a copy of the .env.sample file and rename it to .env and update the variables accordingly
- ensure redis server is running
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

### MVT URLS
```
  [admin portal:]()
  [customer portal:]()
```
## **Endpoints:**
### Bus

`POST /api/v1/tickets/bus/`

Example request body:
``` 
{
  "no_of_seat": 33,
  "bus_name": "super metro"
}

```

`Get /api/v1/tickets/bus/`
- Returns bus objects in the database

`Get /api/v1/tickets/bus/<id>`
- Returns a specific bus object in the database

`Delete /api/v1/tickets/bus/<id>`
- delete a specific bus object in the database

### Route
`POST /api/v1/tickets/route/`

Example request body:
``` 
{
  "from_destination": "string",
  "to_destination": "string"
}
```
`Get /api/v1/tickets/route/`
- Returns route objects in the database

`Get /api/v1/tickets/route/<id>`
- Returns a route bus object in the database

`Delete /api/v1/tickets/route/<id>`
- delete a specific route object in the database

### Schedule
`POST /api/v1/tickets/schedule/`

Example request body:
``` 
{
  "departure_time": "string",
  "arrival_time": "string",
  "date_of_travel": "2022-02-13",
  "bus": 0,
  "route": 0
}
```
`Get /api/v1/tickets/schedule/`
- Returns schedule objects in the database

`Get /api/v1/tickets/schedule/<id>`
- Returns a schedule bus object in the database

`Delete /api/v1/tickets/schedule/<id>`
- delete a specific schedule object in the database


### Reservation
`POST /api/v1/tickets/reservation/`

Example request body:
``` 
{
  "customer_name": "string",
  "seat_no": 0,
  "schedule": {
    "departure_time": "string",
    "arrival_time": "string",
    "date_of_travel": "2022-02-13",
    "bus": bus_id,
    "route": route_id
  }

}
```
`Get /api/v1/tickets/reservation/`
- Returns reservation objects in the database

`Get /api/v1/tickets/reservation/<id>`
- Returns a reservation object in the database

`Delete /api/v1/tickets/reservation/<id>`
- delete a specific reservation object in the database

