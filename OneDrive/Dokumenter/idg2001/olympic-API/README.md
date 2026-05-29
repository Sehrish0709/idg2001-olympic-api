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

# Assignment 2

In Assignment 2, the Olympic API from Assignment 1 was extended with new functionality and several microservices.

## API Improvements

The API was updated to version 2 and now includes:

* User management
* Token management
* Sport filtering by country, year and medal
* Token validation for protected endpoints

Users must have available tokens to access Olympic data. One token is consumed for each request.

## Token Shop Service

A separate token shop service was created to allow users to purchase additional tokens. This service communicates with the main API and updates the user's token balance.

## Cache Service

A cache service was added to improve performance. When a request has already been processed, the result can be returned from the cache instead of being generated again.

The cache service also keeps track of cache hits and cache misses.

## Rate Limiter Service

A rate limiter service was implemented to prevent users from sending too many requests in a short period of time.

This helps protect the API and ensures fair usage.

## Logger Service

A logger service was created to record API activity.

Information is stored in CSV log files and includes details about requests, cache usage and other system events.

Retention endpoints were also implemented to make log management easier.

## Docker and Microservices

Docker was used to containerize all services.

Docker Compose was used to run the complete system with multiple containers.

The project consists of:

* Main API
* Token Shop Service
* Cache Service
* Rate Limiter Service
* Logger Service

Volumes were also used to store datasets and log files.

## Testing and Code Quality

Pytest was used to test important functionality in the system.

Flake8 was used to check code style and maintain consistency.

Mypy was used for static type checking.

All implemented tests pass successfully.
