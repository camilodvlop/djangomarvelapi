# djangomarvelapi
This REST API retrieves information about characters from the Marvel API and returns a list of their latest appearances.
First you need the API key from Marvel´s developers site: https://developer.marvel.com/
we are going to use the get "/v1/public/characters" to obtain all or the matching charachters from marvel 
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


# create EC2 instance with AMI of Ubuntu  // crear instancia ec2 en AWS tipo ubuntu
# para instalar docker  Actualizar el sistema:
sudo apt-get update -y
sudo apt-get upgrade -y
# Instalar dependencias necesarias:
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y
# Agregar el repositorio de Docker
# Añadir la clave GPG oficial de Docker para verificar la autenticidad de los paquetes
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# Añadir el repositorio de Docker para Ubuntu:
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
# Actualizar el índice de paquetes:
sudo apt-get update -y
# instalar Docker:
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
# Iniciar y habilitar Docker
sudo systemctl start docker
sudo systemctl enable docker
# Verificar la instalación de Docker
sudo docker --version
# Permitir el uso de Docker sin sudo
sudo usermod -aG docker $USER
newgrp docker
# Verificar que Docker funciona sin
docker --version
# Obtener la imagen desde Docker Hub
docker pull camilodvlop/django-marvel-api:v1
# verificar las imágenes descargadas
docker images
# Ejecutar el contenedor
docker run -p 80:8000 camilodvlop/django-marvel-api:v1
docker ps

