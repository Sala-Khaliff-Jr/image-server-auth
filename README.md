## Image Server

A Flask Web server with user authentication that allows to upload images and retrieve the images

## Steps to run the code

To install the required packages

`pip install -r requirements.txt`

To create the sql lite database

`python create_db.py`

To tell Flask where to look for the project files

`export FLASK_APP=project`

To run the Flask Server 

`flask run`

and then navigate to localhost:5000

* click on sign up to create a new user
* login with the username and id created
* goto uploads and select image to upload
* navigate to gallery to view the uploaded images

*known issues are listed in issues tab*