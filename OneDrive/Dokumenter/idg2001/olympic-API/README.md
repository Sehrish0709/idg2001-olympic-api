# Olympic API

## Description

This project is a REST API built using FastAPI.  
It allows users to retrieve data related to the Olympic Games, such as sports.

The API includes a token-based system where each request costs 1 token.  
Users must have available tokens to access the API endpoints.


## Features

- User management (create, retrieve, delete users)
- Token system (each API call consumes 1 token)
- Olympic data endpoint:
  - Sport (with filtering)
- Query filtering for sport endpoint (country, year, medal)
- API versioning using `/v1/`
- Automated testing using pytest


## Technologies used

- Python
- FastAPI
- SQLAlchemy (for database handling)
- SQLite (local database)
- Pytest (for testing)


## Dataset

The Olympic data is loaded from a CSV file (`olympics.csv`).

The dataset is based on Olympic athlete data from Kaggle.  
To improve performance, only a subset of approximately 1000 rows is used.

The API reads the CSV file and filters data dynamically based on user input.


## Data handling

Olympic data is not stored in the database.

Instead:
- User data is stored in a SQLite database
- Olympic data is read from a CSV file

This separates user management from dataset handling and keeps the solution simple.


## How to run the project

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Start the API server

```bash
python -m uvicorn app.main:app --reload
```

3. Open the API documentation

Open your browser and go to:  
http://127.0.0.1:8000/docs

This page allows you to test all endpoints directly.


## Running tests

To run the automated tests, use:

```bash
python -m pytest
```

The tests check that:

- Users can be created
- Tokens are consumed when using the API


## Example usage

### Create a user

POST /v1/user/?email=test@mail.com&password=123

This creates a new user with an initial amount of tokens.


### Retrieve sport data

GET /v1/sport/football?user_id=1

This returns sport data and reduces the user's tokens by 1.


### Retrieve sport data with filters

GET /v1/sport/football?user_id=1&country=NOR&year=2020&medal=gold

This demonstrates how query parameters can be used to filter results.


## Token system

- Each API request costs 1 token
- If a user has 0 tokens, the API returns an error
- Tokens can be added using the `/v1/tokens` endpoint


## Notes

- The database is used to store users and their tokens
- The API structure is designed to demonstrate how a token-based system works
- The Olympic data is based on a real dataset but simplified to improve performance
