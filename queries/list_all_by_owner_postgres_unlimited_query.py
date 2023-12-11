from models import Session, Task

session = Session()
tasks = session.query(Task).all()

print(tasks)
