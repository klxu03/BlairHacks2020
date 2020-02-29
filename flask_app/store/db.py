import boto3

dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamoDB.create_table(
    TableName = 'Walmart2',

    KeySchema = [
        {
            'AttributeName' : 'produce',
            'KeyType': 'HASH'
        }
    ],

    AttributeDefinitions=[
        {
            'AttributeName': 'produce',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print(table.table_status)
