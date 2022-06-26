# API for doctor qualification

A dead simple Django project using Django REST framework.

## Setup

---
* Download the files from this repo
* Change the directory to the folder where you downloaded files
* For installing required packages, execute the following command in terminal:
    
    ``$pip install -r requirements.txt``
  

* After successful installation execute the following commands:
    ```
  $python manage.py migrate
  $python manage.py runserver
    ```
* Visit ``127.0.0.1:8000`` in your browser!

## Structure

In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around collections and elements, both of which are resources.

In our case, we have two resource, ``doctor`` and ``direction`` so we will use the following URLS - ``/doctor/`` and ``/direction/``
for collections and elements, respectively:

|  Endpoint | HTTP Method |  CRUD Method| Result|
|---|---|---|---|
|  ``direction`` | GET  | READ  | Get all directions  |
|  ``direction/:id`` | GET  | READ  | Get a single directions  |
| ``doctor``  | GET  | READ  | Get all doctors  |
| ``doctor/:id``  | GET  | READ  | Get info about one doctor  |
| ``doctor``  | POST  | CREATE  | Add doctor  |
| ``doctor/:id``  | DELETE  | DELETE  | Delete doctor  |


## Pagination

The API supports pagination, by default responses have a page_size=2 but if you want change that you can pass through
params page_size={your_page_size_number}

```
http://127.0.0.1:8000/api/v1/doctor/?page=2
```

## Filter 

The API supports filtering, you can filter doctors by their direction and/or work experience like this:
```
http://127.0.0.1:8000/api/v1/doctor/?direction=1&work_exp=1
http://127.0.0.1:8000/api/v1/doctor/?direction=2&work_exp=8
```

## Sorting

You can also sort list like so:
```
http://127.0.0.1:8000/api/v1/doctor/?ordering=work_exp
http://127.0.0.1:8000/api/v1/doctor/?ordering=-sort_num
```

## Slug
Was add slug URL and now, instead:
```
http://127.0.0.1:8000/api/v1/direct/1/
```
you can use:
```
http://127.0.0.1:8000/api/v1/direct/dentist/
```


Build with ❤️ by [psteeep](https://github.com/psteeep)