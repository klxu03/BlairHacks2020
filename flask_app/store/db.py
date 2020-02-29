import boto3

dynamoDB = boto3.resourse('dynamodb')

table = dynamoDB.create_table{
    TableName = 'sujayAndSam',

    KeySchema = [
        {
            'AttributeName '
        }
    ]
}