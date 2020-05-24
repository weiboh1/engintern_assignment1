import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
	s3 = boto3.client('s3')
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
	s3_uploadfile = s3.put_object(Bucket='weiboh1-helloworld',Key='now.txt',Body=timestampStr)
	return {
        'statusCode': 200,
        'body': json.dumps('File now.txt has been uploaded!')
    }