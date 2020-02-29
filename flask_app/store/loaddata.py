import csv
import boto3


dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamoDB.Table('Walmart2')
# TODO create a table for the csv file
def loaddata(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            table.put_item(
                Item={
                    'produce': row[0],
                    headers[1]: row[1],
                    headers[2]: row[2],
                    headers[3]: row[3],
                }
            )

loaddata("spreadsheet-upload/store_side.csv")
