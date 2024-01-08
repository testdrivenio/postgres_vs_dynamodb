import boto3
from boto3.dynamodb.conditions import Key

owner = "john@doe.com"

dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:9999")
table = dynamodb.Table("tasks-api")
last_key = None
query_kwargs = {
    "KeyConditionExpression": Key("PK").eq(f"#TASK#{owner}"),
}
tasks = []
while True:
    if last_key is not None:
        query_kwargs["ExclusiveStartKey"] = last_key
    response = table.query(**query_kwargs)
    tasks.extend(response["Items"])
    last_key = response.get("LastEvaluatedKey")
    if last_key is None:
        break

print(tasks)