# Image Labels Generator Using AWS Rekognition

The Image Labels Generator is an AWS-powered tool designed to automate image analysis by identifying and labeling objects in images using Amazon Rekognition, a state-of-the-art AI image analysis service. This project offers a scalable, cost-efficient, and serverless solution for tasks such as digital asset management, automated tagging, and content moderation.

# Key Features

Support for Multiple Formats: Handles JPEG, JPG, and PNG files.

Automated Object Detection: Identifies objects, their bounding boxes, and confidence scores in real time.

User-Friendly Frontend: Allows image upload and displays results with bounding boxes rendered directly on the UI.

Serverless Architecture: Utilizes AWS Lambda, S3, and Rekognition for backend workflows.

Secure Access: Employs Amazon Cognito for secure user authentication and authorization.

# AWS Services Used: 

Amazon S3: Stores images and results (in JSON format).

AWS Lambda: Processes images and triggers Rekognition.

Amazon Rekognition: Detects objects and generates bounding box coordinates.

Amazon Cognito: Manages authentication for secure image uploads.

AWS Amplify: Hosts the frontend application integrated with GitHub.

IAM Roles and Policies: Ensures secure interaction between AWS services.

CloudWatch: Monitors and logs Lambda functions for better debugging and tracking.

# Project Workflow

Image Upload: Users upload images via the web interface.

S3 Bucket: Images are stored in an S3 bucket, triggering a Lambda function.

Lambda Function: Processes the image, calls Rekognition for object detection, saves results (bounding box coordinates and confidence intervals) in JSON format in the S3 results folder.

Frontend Rendering: Polls the S3 results folder for the JSON output. Displays the image with bounding boxes rendered based on detected objects. Implementation Details

# Frontend: 
Built with HTML, CSS, and JavaScript. Features real-time bounding box rendering using the canvas element.

# Backend:
Configures S3 notifications to trigger Lambda functions upon image upload.
Implements IAM roles for secure access and permissions.
Stores detection results in JSON format for seamless integration.

# Integration: 
Enabled CORS for S3 to allow Amplify-hosted frontend to access data.
