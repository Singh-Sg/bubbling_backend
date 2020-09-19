#Bubbling Micro Services
---------------

Bubbling Django MicroServices is related to APIs for car and manufacture.

Getting Started
---------------

To work on the sample code, you'll need to clone project's repository to your
local computer. If you haven't, do that first. 

github repo : https://github.com/Singh-Sg/bubbling_backend.git


git clone https://github.com/Singh-Sg/bubbling_backend.git

1. Create a Python virtual environment for your Django project. This virtual
environment allows you to isolate this project and install any packages you
need without affecting the system Python installation. At the terminal, type
the following command:
    ```
      $ virtualenv -p python3.6 venv
    ```
2. Activate the virtual environment:
    ```
      $ source venv/bin/activate
    ```

3. Install Python dependencies for this project:
    ```
      $ pip install -r requirements.txt
    ```

4. For Database schema:
    ```
      $ You need to create 2 database where database name:bubbling_api_backend and user_manager using default user.
    $ sudo -u postgres psql  (Login into postgres console)
      $ postgres=# create database bubbling_api_backend;
      $ postgres=# create database user_manager;
      $ python manage.py migrate
      $ python manage.py create_group  (This to apply Permission to the groups in API_BACKEND Project)
   ```

5. Create Super User
    ```
      $ python manage.py createsupersuer
      $ Note: For both project you have to create same email and password:
      $ Email: deependrasg@gamil.com
      $ Password: data@321
    ```

6. Start the Django development server:
    ```
      $ python manage.py runserver 8001 (For api_backend)
      $ python manage.py runserver 8000 (For user_manager)
    ```
7. Open http://127.0.0.1:8000/ and http://127.0.0.1:8001/  in a web browser to view your application.



What's Here
-----------

This sample includes:

* README.md - this file
* api_backend/ - this directory contains first Django Microservice
* user_manager/ - this directory contains second Django Microservice
* Bubblings.postmant_collection: Postman export file you can import in postman here all api infomation presents


API Docs:
---------

1) http://127.0.0.1:8000/users/token-auth/
  Info: User Login API where you will get TOKEN
  Method: POST
  Parameter: 
    ```
     {
        "password": "student@123",
        "email": "admin@gmail.com"
    }
    ```


2) http://127.0.0.1:8000/users/create_auth/
  Info: `Create User By admin`
  Method: `POST`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note: Here Token from admin user, Simple user token will not work
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
  Info: `Create manufacturer`
  Method: `POST`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note: Here Token from admin user, Simple user token will not work
  Parameter: 
    ```
        {
            "name": "Tata Moters",
            "description": "Tata Moters India",
            "country": 7
        }
    ```

4) http://127.0.0.1:8000/manufacturer/e4c953f6-0cd9-46a6-9ce8-365ec53b115f/
  Info: `GET manufacturer`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note: Here Token from admin user, Simple user token will not work
  Method: `GET`


5) http://127.0.0.1:8000/manufacturer/e4c953f6-0cd9-46a6-9ce8-365ec53b115f/
  Info: `Update Manufacture`
  Method: `PATCH`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note: Here Token from admin user, Simple user token will not work
  Parameter: 
    ```
        {
            "name": "Tata Moters",
            "description": "Tata Moters India New",
            "country": 1
        }
    ```

6) http://127.0.0.1:8000/manufacturer/e4c953f6-0cd9-46a6-9ce8-365ec53b115f/
  Info: `Delete manufacturer`
  Method: `Delete`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note: Here Token from admin user, Simple user token will not work


7) http://127.0.0.1:8000/car/
  Info: `Create CAR object by admin user`
  Method: `POST`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note: Here Token from admin user, Simple user token will not work
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


8) http://127.0.0.1:8000/car/6a850802-3582-4813-9f56-fb924fd99ae1/
  Info: `GET Car Object by ID`
  Method: `GET`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note: Here Token from admin user, Simple user token will not work


9) http://127.0.0.1:8000/car/6a850802-3582-4813-9f56-fb924fd99ae1/
  Info: `Update CAR Objects`
  Method: `PATCH`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note: Here Token from admin user, Simple user token will not work
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


10) http://127.0.0.1:8000/car/6a850802-3582-4813-9f56-fb924fd99ae1/
  Info: `Delete Car Object by ID`
  Method: `Delete`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note: Here Token from admin user, Simple user token will not work



#### This api can use Both(Admin and Simple User) type user.


11) http://127.0.0.1:8000/car-list/
  Info: `Showing the all car objects`
  Method: `GET`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note: Here Token from Admin User or Simple User
  OutPut:
    ```
      {
        "car_data": [
            {
                "id": "6a850802-3582-4813-9f56-fb924fd99ae1",
                "name": "Tata Pajaro",
                "color": "White",
                "number_of_doors": 4,
                "price": 20.0,
                "model_name": "TATA Tta",
                "owner": "c36986c8-e8d5-4f39-af5e-ffcb738316a4",
                "created_at": "2020-09-19T15:06:08.175625Z",
                "updated_at": "2020-09-19T15:24:46.132490Z",
                "manufacturer": "27aa6996-1f24-430c-b554-2c9b17fa4f4e"
            }
        ]
    }
    ```


12) http://127.0.0.1:8000/manufacturer-list/
  Info: Showing the all manufacturer objects
  Method: `GET`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note_1: Here Token from Admin User or  Simple User
  Note_2: Here you will get Country Name not a int value
  OutPut:
    ```
      {
          "manufacturer_data": [
              {
                  "id": "27aa6996-1f24-430c-b554-2c9b17fa4f4e",
                  "country": "Japan",
                  "name": "Update Manufacture",
                  "description": "Welcome To Tata Manufacture",
                  "created_at": "2020-09-19T15:03:19.324843Z",
                  "updated_at": "2020-09-19T15:04:18.091937Z"
              }
          ]
      }
    ```


13) http://127.0.0.1:8000/users/profile/
  Info: `Showing login user info`
  Method:  `GET`
  Headers: `{"Authorization":"Token 69d32d6aa44063eed31e92eda4a0253cbe365160"}`
  Note_1: Here Token from Admin User or  Simple User
  OutPut:
    ```
      {
          "data": {
              "email": "admin@gmail.com",
              "first_name": "",
              "last_name": "",
              "user_uuid": "7fa9e14f-05f5-4424-b7c6-7a9a337f9c05"
          }
      }  
    ```
