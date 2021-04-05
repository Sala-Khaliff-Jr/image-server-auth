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

# References

[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)

[Flask Authentication - Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)

[Python pillow PIL Fork](https://pillow.readthedocs.io/en/stable/)
