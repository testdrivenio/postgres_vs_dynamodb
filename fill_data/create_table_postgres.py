from models import Session, Task

TASKS = [
    {
        "status": "OPEN",
        "owner": "john@doe.com",
        "title": "Buy milk"
    },
    {
        "status": "CLOSED",
        "owner": "john@doe.com",
        "title": "Kiss your wife"
    },
]


session = Session()

with session.begin():
    for task in TASKS:
        session.add(Task(**task))