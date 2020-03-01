import boto3
import csv
import time

# Takes a name and makes a product table with attribute name called
def createTable(name):
    dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamoDB.create_table(
        TableName = name,

        KeySchema = [
            {
                'AttributeName' : 'name',
                'KeyType': 'HASH'
            }
        ],

        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table

# loads data from a csv file into a specified database
def loadData(filename, database):
    dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamoDB.Table(database)
    with open(filename) as f:
        csv_reader = csv.reader(f, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            table.put_item(
                Item={
                    'name': row[0],
                    headers[1]: row[1],
                    headers[2]: row[2],
                    headers[3]: row[3],
                }
            )

# gets data from a item name
def getData(name, database):
    dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamoDB.Table(database)
    try:
        info = table.get_item(Key={'name': name}).get('Item')
    except:
        info = "Error"
    return info

#returns a list of all data with price
def getDataByPrice(price, database):
    dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamoDB.Table(database)
    try:
        info = []
        all_items = table.scan(ProjectionExpression="#nm, price",ExpressionAttributeNames={"#nm":"name"}).get('Items')
        for item in all_items:
            if int(item.get('price')) == price:
                info.append(item)
        return info
    except:
        info = "Error"
    return info

# Takes in a csv named [filename].csv and makes a database called [name] with data
# from the csv file
def csvToDatabase(filename, name):
    createTable(name)
    time.sleep(5)
    loadData(filename, name)
