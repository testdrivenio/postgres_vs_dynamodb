import boto3


client = boto3.client("dynamodb", endpoint_url="http://localhost:9999")
client.create_table(
    TableName="tasks-api",
    KeySchema=[
        {"AttributeName": "PK", "KeyType": "HASH"},
        {"AttributeName": "SK", "KeyType": "RANGE"},
    ],
    AttributeDefinitions=[
        {"AttributeName": "PK", "AttributeType": "S"},
        {"AttributeName": "SK", "AttributeType": "S"},
        {"AttributeName": "GS1PK", "AttributeType": "S"},
        {"AttributeName": "GS1SK", "AttributeType": "S"},
    ],
    GlobalSecondaryIndexes=[
        {
            "IndexName": "GS1",
            "KeySchema": [
                {"AttributeName": "GS1PK", "KeyType": "HASH"},
                {"AttributeName": "GS1SK", "KeyType": "RANGE"},
            ],
            "Projection": {"ProjectionType": "ALL"},
        },
    ],
    BillingMode="PAY_PER_REQUEST",
)

TASKS = [
    {
        "PK": "#TASK#john@doe.com",
        "SK": f"#TASK#afb225e9-dd19-4803-9b72-51958a8d7202",
        "id": "afb225e9-dd19-4803-9b72-51958a8d7202",
        "status": "OPEN",
        "owner": "john@doe.com",
        "title": "Buy milk",
        "GS1PK": "#TASK#OPEN",
        "GS1SK": f"#TASK#afb225e9-dd19-4803-9b72-51958a8d7202",
    },
    {
        "PK": "#PK#john@doe.com",
        "SK": f"#SK#7b0f4bc8-4751-41f1-b3b1-23a935d81cd",
        "id": "7b0f4bc8-4751-41f1-b3b1-23a935d81cd",
        "status": "CLOSED",
        "owner": "john@doe.com",
        "title": "Kiss your wife",
        "GS1PK": "#TASK#CLOSED",
        "GS1SK": f"#TASK#7b0f4bc8-4751-41f1-b3b1-23a935d81cd",
    },
]


dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:9999")
table = dynamodb.Table("tasks-api")

for task in TASKS:
    table.put_item(
        Item=task
    )