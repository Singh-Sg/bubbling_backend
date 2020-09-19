#Bubbling Micro Services

Bubbling Micro Services is related to api for car and manufacture.

Getting Started
---------------

To work on the sample code, you'll need to clone project's repository to your
local computer. If you haven't, do that first. 

github repo :

bitbucket repo :

git clone 

1. Create a Python virtual environment for your Django project. This virtual
environment allows you to isolate this project and install any packages you
need without affecting the system Python installation. At the terminal, type
the following command:

    $ virtualenv -p python3.6 venv

2. Activate the virtual environment:

    $ source venv/bin/activate

3. Install Python dependencies for this project:

    $ pip install -r requirements.txt

4. For Database schema:
	$ You need to create 2 database where database name:bubbling_api_backend and user_manager using default user.
	$ sudo -u postgres psql  (Login into postgres console)
    $ postgres=# create database bubbling_api_backend;
    $ create database user_manager;

    $ python manage.py migrate
    $ python manage.py create_group  (This to apply Permitions to the groups in API_BACKEND Project)


5. Create Super User

    $ python manage.py createsupersuer
    $ Note: For both project you have to create same email and password:
    $ Email: deependrasg@gamil.com
    $ Password: data@321

6. Start the Django development server:

    $ python manage.py runserver 8001 (For api backend)
    $ python manage.py runserver 8000 (For User Manager)

7. Open http://127.0.0.1:8000/ and http://127.0.0.1:8002/  in a web browser to view your application.



What's Here
-----------

This sample includes:

* README.md - this file
* api_backend/ - this directory contains first Django Microservice
* user_manager/ - this directory contains second Django Microservice

API Docs:
---------

1) http://127.0.0.1:8000/users/token-auth/
  Info: Login user where you will get TOKEN
  Method: POST
  Parameter: 
    ```
     {
        "password": "student@123",
        "email": "admin@gmail.com"
    }
    ```


2) http://127.0.0.1:8000/users/create_auth/
  Info: Create User By Using admin
  Method: POST
  Parameter: 
    ```
        {
            "password": "student@123",
            "email": "deependrasg3@gmail.com",
            "first_name": "Singh",
            "last_name": "deependra"
        }
    ```

3) http://127.0.0.1:8000/manufacturer/
  Info: Create manufacturer
  Method: POST
  Parameter: 
    ```
        {
            "name": "Tata Moters",
            "description": "Tata Moters India",
            "country": 7
        }
    ```

4) http://127.0.0.1:8000/manufacturer/e4c953f6-0cd9-46a6-9ce8-365ec53b115f/
  Info: GET manufacturer
  Method: GET


5) http://127.0.0.1:8000/manufacturer/e4c953f6-0cd9-46a6-9ce8-365ec53b115f/
  Info: Update Manufacture
  Method: PATCH
  Parameter: 
    ```
        {
            "name": "Tata Moters",
            "description": "Tata Moters India New",
            "country": 1
        }
    ```

6) http://127.0.0.1:8000/manufacturer/e4c953f6-0cd9-46a6-9ce8-365ec53b115f/
  Info: Delete manufacturer
  Method: Delete



6) http://127.0.0.1:8000/car/
  Info: Create CAR
  Method: POST
  Parameter: 
    ```
        {
          "name": "Verena",
          "color": "Red",
          "number_of_doors": 4,
          "price": 42.1,
          "model_name": "SUV",
          "owner": "c36986c8-e8d5-4f39-af5e-ffcb738316a4",
          "manufacturer": "27aa6996-1f24-430c-b554-2c9b17fa4f4e"
        }
    ```
  Note: 
      1)Here manufacturer is a id of manufacturer object.
      2)Here owner is a uuis of user objects "user_uuid": "4697771f-e5ae-46f9-86d1-7d4b3369c250".
        a) User should not be ADMIN
        b) You will get user_uuid from while create user (http://127.0.0.1:8000/users/create_auth/)
           or using admin panel









Note: Please import Bubblings.postmant_collection in your postman for all APIs information



