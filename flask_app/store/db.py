import boto3

dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamoDB.create_table(
    TableName = 'Walmart2',

    KeySchema = [
        {
            'AttributeName' : 'produce',
            'KeyType': 'HASH'
        },
        {
            'AttributeName' : 'prices',
            'KeyType' : 'RANGE'
        }
    ],

    AttributeDefinitions=[
        {
            'AttributeName': 'produce',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'prices',
            'AttributeType': 'N'
        }
    ]
)

print(table.table_status)
