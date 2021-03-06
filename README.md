# monorepo-api
Scalable Mono repo dockerized backend REST API implementation with Python Flask

[![CodeFactor](https://www.codefactor.io/repository/github/ucdevinda123/monorepo-api/badge)](https://www.codefactor.io/repository/github/ucdevinda123/monorepo-api)

## Architecture:

![diagram](https://user-images.githubusercontent.com/4921099/131813802-c4ae3fd2-3d28-493b-bcbc-3296e9ec09bc.png)



## How to Build:

Got to your root directory and
         
     docker-compose up --build

If you want to run in the virtual environment

      pip3 install -r requirements.txt
Activate virtual environment : 
      
      source venv/bin/activate
      export FLASK_ENV=development
      export FLASK_APP=run
      flask run

## Project Strucuture

Monorepo-API (Root)
-authentication (Flask api responsible for authentication of the users could also called userservice)

-nginx - Act as the API gateway and uwsgi application server runs on it

-streaming-service - Comming soon.. (Flask API which Will be resposible for the streaming service)

## API Enpoint from authentication service

   - **Token** : POST http://127.0.0.1/api/v1/auth/token

     
           Request
               {
               "username":"",
               "password" : ""
               }
          Response:
             {
             "access_token": "",
             "code": 200,
             "refresh_token": "",
             "success": true
             }

- **Refresh Token** : POST http://127.0.0.1/api/v1/auth/token/refresh

            Request:
            Bearer Token : (Refresh Token)

            Response:

            {
            "access_token": "",
            "code": 200,
            "success": true
            }

- **Register** POST http://127.0.0.1/api/v1/auth/register

         Request
         {
         "username":"",
         "password" : ""
         }

         Response:
         {
         "code": 201,
         "msg": "Registration Successfully",
         "success": true
         }

- **Me** GET http://127.0.0.1/api/v1/auth/me
         Bearer Token : (Access Token)

         Response:
         {
         "code": 200,
         "success": true,
         "user": {
         "id": 1,
         "name": "tt@erer"
         }
         }
 
