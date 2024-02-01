import boto3
import os

client = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_ADMIN_ACCESS_KEY'), aws_secret_access_key=os.environ.get('AWS_ADMIN_SECRET'))
objects = client.list_buckets()

if __name__ == "__main__":

    print(f"woot \n{objects}")
