# djangomarvelapi
This REST API retrieves information about characters from the Marvel API and returns a list of their latest appearances.
First you need the API key from Marvel´s developers site: https://developer.marvel.com/
we are going to use the get "/v1/public/characters" to obtain all or the matchin charachters from marvel 
http://gateway.marvel.com/v1/public/characters?name=wolverine&ts=1111222&apikey=123467&hash=ffd275c5130566a2916217b101f26150
ts is a timestamp
hash - a md5 digest of the ts parameter, your private key and your public key (e.g. md5(ts+privateKey+publicKey) the code is responsible for this. you still can test marvel's API on postman, set a random numeric value to ts var and use any online MD5 encoder web tool and paste the random number followeb by your private api key and ypur publik key, then copy the result and send it as the hash value, in the ts parameter paste the same numeric value you used.

This project uses Django and djangorestframework (DRF) to work as a REST API
using powershell install the dependencies
pip install django djangorestframework requests
pip install python-decouple  # para poder obtener las variables de entorno
django-admin startproject marvelapi  # to create a django project
cd .\marvelapi\  # to stand in the new folder created
 python manage.py startapp api    # creates a folder called api with python classes

python manage.py runserver  # corre el servicio localmente




** To run the project **
if you use docker:
docker build -t django-marvel-api . 
docker run -p 8000:8000 django-marvel-api



