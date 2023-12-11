from models import Session, Task

tasks = []
last_evaluated_id = -1
session = Session()

while True:
    query = session.query(Task).filter(Task.id > last_evaluated_id).order_by(Task.id).limit(10)
    tasks.extend(query.all())
    last_evaluated_id = tasks[-1].id
    if len(tasks) < 10:
        break

print(tasks)
