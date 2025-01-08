import boto3
import json

rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract S3 bucket and file name from the event triggered by S3 upload
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    # Skip non-image files
    if not (file_name.lower().endswith('.jpg') or file_name.lower().endswith('.jpeg') or file_name.lower().endswith('.png')):
        print(f"Skipping non-image file: {file_name}")
        return {
            'statusCode': 200,
            'body': 'Skipped non-image file'
        }

    try:
        print(f"Received image file: {file_name}")

        # Call Rekognition to detect labels
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket_name, 'Name': file_name}},
            MaxLabels=20,  
            MinConfidence=75  
        )

        labels = response['Labels']
        print("Detected labels:", labels)

        # Prepare result to store in S3
        result = {
            'labels': labels,
            'image_url': f'https://{bucket_name}.s3.us-east-1.amazonaws.com/{file_name}'
        }

        # Save result as JSON in the 'results' folder
        result_key = f'results/{file_name}.json'
        s3.put_object(
            Bucket=bucket_name,
            Key=result_key,
            Body=json.dumps(result),
            ContentType='application/json'
        )

        return {
            'statusCode': 200,
            'body': f'Results saved to: {result_key}'
        }

    except Exception as e:
        print("Error processing image:", e)
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
