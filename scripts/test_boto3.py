import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

with open('text.txt', 'rb') as data:
    s3.Bucket('stackflow-data-lake').put_object(Key='text.txt', Body=data)