# DynamoDB vs. Postgres Examples

This repository supports tutorial [DynamoDB vs. Postgres - Which database to choose for your Python project?](https://testdriven.io/blog/postgres-vs-dynamodb/).

## How to run the code
### Start the databases
```shell
$ docker-compose up -d
```

### Create virtual environment
```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt 
```

### Fill the databases with data
```shell
$ export PYTHONPATH=$PWD:$PYTHONPATH
$ (venv) python fill_data/create_table_dynamodb.py
$ (venv) python fill_data/create_table_postgres.py
```

### Run the examples
```shell
$ export PYTHONPATH=$PWD:$PYTHONPATH
$ (venv) python queries/list_all_by_owner_dynamodb.py
$ (venv) python queries/list_all_by_owner_postgres.py
```

You can do the same for other scripts in `queries` directory.