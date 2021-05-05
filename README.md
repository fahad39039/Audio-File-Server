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

## How to test APIs by postman
1. **create_file api**
```
url = /create 
method = Post
content-type=application/json
```
Body for song
```
 {
  "audioFileType":"song",
  "audioFileMetadata":{
      "duration_in_sec":30,
      "name":"Test song"
      }
  }
```
Body for podcast
```
{
      "audioFileType":"podcast",
      "audioFileMetadata":{
              "duration_in_sec":100,
              "name":"Test song 2",
              "host":"Test Host",
              "participants":["P1", "P2"]
              }
      }
```
Body for audiobook
```
{
      "audioFileType":"audiobook",
      "audioFileMetadata":{
              "duration_in_sec":200,
              "title":"Test Title",
              "author":"Test Author",
              "narrator":"Test Nar"
      }
  }
```
2. **delete_file_by_id api**
```
url = /delete/<audio_file_type>/<audio_file_id> 
method = Delete
content-type=application/json
```
Example -><br> 1. `/delete/song/1` <br> 2. `/delete/podcast/1` <br> 2. `/delete/audiobook/1` 

3. **update_file_by_id api**
```
url = /update/<audio_file_type>/<audio_file_id> 
method = Delete
content-type=application/json
```
Body for song
```
 {
  "audioFileType":"song",
  "audioFileMetadata":{
      "duration_in_sec":32,
      "name":"Test song 34"
      }
  }
```
Body for podcast
```
{
      "audioFileType":"podcast",
      "audioFileMetadata":{
              "duration_in_sec":109,
              "name":"Test song 24",
              "host":"Test Host 1",
              "participants":["P1", "P2"]
              }
      }
```
Body for audiobook
```
{
      "audioFileType":"audiobook",
      "audioFileMetadata":{
              "duration_in_sec":201,
              "title":"Test Title 1",
              "author":"Test Author 3",
              "narrator":"Test Nar 1"
      }
  }
```

4. **get_files api**
```
url = /get/<audio_file_type>/<audio_file_id> **OR** /get/<audio_file_type>
method = GET
content-type=application/json
```
Example-> <br>
`/get/song` - returns all song stored in database<br>
`/get/song/1` - get a song whose id is 1
