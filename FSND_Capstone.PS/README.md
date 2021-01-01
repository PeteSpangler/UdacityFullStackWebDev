# FSND_Capstone.PS
## Final project for Udacity Full Stack Web Dev Nanodegree
The motivation for this project was to practice the skills and demonstrate knowledge of the material presented in the course.
This app allows to record simple stats for hockey players, both Skaters and Goalies. There are two roles:
Fan, which allows to only see which Skaters and Goalies are in the database and
GM, which can post, patch, and delete stats and see full details for both Skaters and Goalies. 
Heroku Link: https://spangcapstone.herokuapp.com

### Vital dependencies and platforms
-[Flask]
Flask is a lightweight microservices web framework that utilizes Python.
-[SQLAlchemy]
SQLAlchemy is a SQL ORM that allows user to write pythonic code and not raw SQL.
-[Auth0]
Auth0 is how authentication and authorization is achieved in this api.
-[PostgreSQL]
The relational database platform used in this API
-[Heroku]
The cloud platform this API has been deployed on.

# Getting Started:

### Python 3.7 (Virtual Environment)

Best practice to work within a Virtual environment to keep dependencies in one place within
project. 
Follow instructions on how to do so here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

### PIP Requirements and Environmental Variables
Once you have setup your virtual environment running, easily install requirements with the following command:
```bash
pip install -r requirements.txt
```
Set the necessary environment variables:
These can be found within the setup.sh file.

### Running Local Tests
First, a database must be created to restore the sql database provided.
```bash
createdb capstone
psql capstone < hockeystats.psql
```
Configure the database path to connect to this new locally created postgres database:
```bash
export DATABASE_URL=<local_database_url>
```
Then deploy locally and run the tests from another terminal:
```bash
export FLASK_APP=app.py
flask run --reload
python test.py
```

## API Reference
The application is hosted on Heroku, so testing can easily be accomplished through Postman. A postman collection 
can be found within this repository. If you are testing this API shortly after it has been uploaded for review,
the JWT tokens within the repository should still be active. Otherwise, follow the steps below to generate fresh JWT tokens.

## Authentication:
Authentication for this API is done with the assistance of AUTH0 and can be done using a Google Account
or with an email address and password. I have gone ahead and registered two users for this app,
one with the Fan level of access and the other with the all-seeing GM level of access.
GM login:
******
fan login:
******

After logging in at the following link:
****** the JWT found in the address bar and add it into postman as a global variable for either
Grab the JWT specifying fan_token or GM_token from the URL to complete the tests by updating the environment variables in Postman.

## Models and Roles
There are two roles in this API:
-Fan
Which has permissions for:
get:skaters	get ids and names of skaters	

get:goalies	get ids and names of goalies
-GM
Which has permissions for:
get:skaters	     get ids and names of skaters	

get:goalies	     get ids and names of goalies	

get:skaters-info	get long details of skaters	

post:skater	    add new skater to database	

patch:skater	edit skater in database	

delete:skater	remove skater from database	

get:goalies-info	get long details of goalies	

post:goalies	add new goalie to database	

patch:goalie	edit goalie details	

delete:goalie	remove goalie from database

### Models
There are two models:
*Skaters
    *Name
    *Position(pos)
    *Points(pts)
    *Goals(gls)
*Goalies
    *Name
    *Goals Against Average(gaa)
    *Shutouts(so)
    *Wins(w)

### Error Handling
Errors are returned as JSON in the following format:
```json
{
            'success': False,
            'error': 401,
            'message': 'Authentication error'
            }
```
The following error types will be returned when requests fail:
- 401: Authentication Error
- 403: Forbidden
- 404: Resource Not Found
- 422: Unprocessable 
- 500: Internal Server Error

## Endpoints
1. GET '/' (returns simple message that app is live/running on Heroku)
2. GET '/login-results' (returns simple message to retrieve JWT from address bar response)
3. GET '/skaters/int:id' (returns long details of skater with given id)
4. GET '/goalies/int:id' (returns long details of goalie with given id)
5. GET '/skaters' (returns short details of all skaters)
6. GET '/goalies' (returns short details of all goalies)
7. POST '/skaters' (create new skater)
8. POST '/goalies' (create new goalie)
9. PATCH '/skaters/int:id' (update skater at given id)
10. PATCH '/goalies/int:id' (update goalie at given id)
11. DELETE '/skaters/int:id' (delete skater at given id)
12. DELETE '/goalies/int:id' (delete skater at given id)

## Endpoint Responses
```json
1. {
            'success': True,
            'FSND Capstone project': 'a simple NHL season stats recorder.'
            }

2. {
            'success': True,
            'You have made it in successfully.': 'Check the address bar for your JWT for testing.'
            }

3. 
{
    "skater": {
        "gls": 31,
        "id": 7,
        "name": "Jack Eichel",
        "pos": "C",
        "pts": 11
    },
    "success": true
}
4.
{
    "goalie": {
        "gaa": 0.882,
        "id": 4,
        "name": "Malcom Subban",
        "so": 1,
        "w": 12
    },
    "success": true
}
5.
{
    "skaters": [
        {
            "id": 1,
            "name": "Austen Matthews"
        },
        {
            "id": 2,
            "name": "Connor McDavid"
        },
        {
            "id": 3,
            "name": "Taylor Hall"
        },
        {
            "id": 4,
            "name": "Elias Petterssen"
        },
        {
            "id": 5,
            "name": "Duncan Keith"
        },
        {
            "id": 6,
            "name": "Cale Makar"
        },
        {
            "id": 19,
            "name": "Jack Hughes"
        },
        {
            "id": 20,
            "name": "Jack Hughes"
        },
        {
            "id": 21,
            "name": "Jack Hughes"
        }
    ],
    "success": true
}
6.
{
    "gs": [
        {
            "id": 1,
            "name": "Carey Price"
        },
        {
            "id": 2,
            "name": "Corey Hart"
        },
        {
            "id": 3,
            "name": "Carey Price"
        },
        {
            "id": 4,
            "name": "Malcom Subban"
        },
        {
            "id": 7,
            "name": "Sergei Bobrovsky"
        },
        {
            "id": 8,
            "name": "Sergei Bobrovsky"
        },
        {
            "id": 9,
            "name": "Sergei Bobrovsky"
        },
        {
            "id": 10,
            "name": "Sergei Bobrovsky"
        },
        {
            "id": 11,
            "name": "Sergei Bobrovsky"
        },
        {
            "id": 12,
            "name": "Sergei Bobrovsky"
        }
    ],
    "success": true
}
7.
{
    "new_Skater": [
        {
            "gls": 12,
            "id": 19,
            "name": "Jack Hughes",
            "pos": "C",
            "pts": 31
        }
    ],
    "success": true
}

8.
{
    "new_Goalie": [
        {
            "gaa": 0.9,
            "id": 7,
            "name": "Sergei Bobrovsky",
            "so": 1,
            "w": 23
        }
    ],
    "success": true
}
9.
{
    "edited_skater": [
        {
            "gls": 27,
            "id": 4,
            "name": "Elias Petterssen",
            "pos": "C",
            "pts": 66
        }
    ],
    "success": true
}
10.
{
    "fix_goalie": {
        "gaa": 0.909,
        "id": 1,
        "name": "Carey Price",
        "so": 9,
        "w": 27
    },
    "success": true
}
11.
{
    "Deleted": 7,
    "success": true
}
12.
{
    "Deleted": 5,
    "success": true
}

```

# Acknowledgements
-Udacity Knowledge Team, specifically JungleBadger
-https://github.com/the-geekiest-nerd