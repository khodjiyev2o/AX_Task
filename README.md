# MINT
Back-End Service for MINT.

Visit the [Demo]() 

## Getting Started

1. Clone the project from the Github repo :

````
git clone https://github.com/khodjiyev2o/AX_Task
````

2. Go to the project directory -> ./ax

3. Create virtual environment :

````
python3 -m venv venv
````

4. Activate virtual environment  : 

````
source\venv\bin\activate
````

if you are using Windows ,then :

````
venv\Scripts\activate
````
if UNIX/LINUX, then :
````
source venv\bin\activate
````
4. Create the .env file and fill out the missing values. You can look at all missing values in sample.env file:

For example: 
````
SECRET_KEY='django-insecure-$i^+*htoqjh4@g%vtw&k2u1ow7jq-84-6fg)u2pt3(l&h1su^9'
````
5. Build  the docker image

````

$ docker build -t app .

````
6. Run the docker container

````

$  docker run --restart=always --name mint -dp 80:8000 app 

````

    
7. Open your browser and paste one of the urls :

* http://127.0.0.1:80
* http://localhost:80
* http://0.0.0.0:80

