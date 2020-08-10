# Payment Aggregator Service
Simple RESTful API that provides payment data aggregator for an improved touch based payment system.


# Features

## API User Management
 - User registration
 - Login via access token creation
 - Refresh tokens, to create new access tokens when access tokens expire
 - Revoking refresh tokens

## Customer Management
 - Get customer Details by BVN
 - Get customer Details by Phone number
 - Get customer Details by Email

 
   
 # Frameworks and Libraries

The API uses the following libraries and frameworks to deliver the functionalaties described above:

- [Flask](https://palletsprojects.com/p/flask/) - For our web server.
- [flask-restful](https://flask-restful.readthedocs.io/en/latest/installation.html) - For building cool Rest-APIs.
- [Pipenv](https://pipenv.readthedocs.io/en/latest/) For managing python virtual environments.
- [mongoengine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/) - For managing our database.
- [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) - For serializing user requests.
- [Postman](https://www.getpostman.com/downloads/) - For testing our APIs.
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) For hashing user password.
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/) For creating tokens for authorization and authentication.
- [Celery](https://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html) - to schedule long-running tasks.
  

# How to Test


```sh
1. git clone https://github.com/SirGidy/aggregator-service.git

2. Run code from your preferred IDE 

3. Navigate to http://127.0.0.1:5000/ to consume endpoints

```

[click here ](https://github.com/SirGidy/aggregator-service/blob/master/FlaskMongoDB.postman_collection.json) for sample request json objects to be imported to Postman


Happy testing !!!

