# Audio-File-Server

## Setup codebase
1. Clone code:
      `git clone https://github.com/fahad39039/Audio-File-Server.git`
2. Navigate to the cloned directory.
3. Install virtual environment if not installed -> `pip install virtualenv`
4. Create virtual environment -> `virtualenv <env_name>`
5. Install all project requirements -> `pip install -r requirements.txt`

## Create database
1. In mysql create database "audiofileproject"
2. Database connection string -> `mysql://<username>:<password>@<host>/<db_name>`
<br>In my case this is `mysql://root:root@localhost/audiofileproject`

## Run flask app
1. Run flask app using these commands:<br>`1. set FLASK_APP=main.py` <br> `2. flask run`
