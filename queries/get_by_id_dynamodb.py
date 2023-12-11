import boto3
from boto3.dynamodb.conditions import Key

owner = "john@doe.com"
task_id = "7b0f4bc8-4751-41f1-b3b1-23a935d81cd6"

dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:9999")
table = dynamodb.Table("tasks-api")

query_kwargs = {
    "KeyConditionExpression": Key("PK").eq(f"#PK#{owner}") & Key("SK").eq(f"#SK#{task_id}"),
}
task = response = table.query(**query_kwargs)["Items"][0]

print(task)