# Confitec Test

This is a restful api with a single endpoint to search an Artist top 10 hits.

## Table of Contents
- [Installing](#installing)
- [Running](#running)
- [Tests](#tests)
- [Docker](#docker)

## Installing

If you want to only run the project using [docker](https://docs.docker.com/engine/install/) you can skip this section to [docker](#docker).

For the next steps you need:

- [python3](https://www.python.org/downloads/) 
- [redis](https://redis.io/download/)
- A running [DynamoDB](https://aws.amazon.com/dynamodb/) server

1. It is recommended to create a virtual enviroment first.
    ```
    python -m venv .venv
    ```

2. Activate the virtual enviroment 
    ```
    source .venv/bin/activate # Linux
    source .venv/Scripts/activate # Windows
    ```

3. Install the dependencies
    ```
    pip install -r requirements.txt
    ```

4. Set up all the required environment variables as in the *.env.example* file

5. Make sure you have your [aws credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) set up aswell


## Running
```
export FLASK_ENV=development # enable hot reload
flask run
```

After the command you should see something like
```
* Debug mode: on
* Running on http://127.0.0.1:5000/
```

## Tests

This application has **unit** tests and **integration** tests.


1. Unit test

   ```
   python -m unittest discover
   ```

2. Integration test

    ```
    behave
    ```

PS: The integration test still using the same Dynamo table as the application

## Docker

For the next steps you need:

- [Docker](https://docs.docker.com/engine/install/) installed
- A running [DynamoDB](https://aws.amazon.com/dynamodb/) server

1. Running
    
    ```
    docker-compose up -d
    ```

2. You should be able to access the application on PORT=8000