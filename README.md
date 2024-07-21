# AWS Strava API

The aim of this project is to provide the infrastructure and code to send emails from AWS. 

## HOW DOES IT WORK

This project contains the AWS CDK (IaC) infrastructure for the following components:

1. A SQS QUEUE to collect the messages to be send.
2. A Lambda function that collects the messages and calls the SES service. 

## PREREQUISITES

- Installed and setup the AWS CLI infrastucture.
- Installed python and poetry.
- Created a Stack of the AWS-Mailer project.
- A lambda layer containing the 'requests' package

## HOW TO GET STARTED

1. Open the folder 'aws-strava-stats' in your favorite IDE.
2. Setup a poetry virtual environment. 
3. Activate the poetry environment.
4. Install python packages in the virtual environment.
5. Prepare the lambda layer: 
    ```powershell
    mkdir -p .build/common_layer 
    
    poetry export --without=dev --without-hashes --format=requirements.txt > .build/common_layer/requirements.txt

    pip install -t .build/common_layer -r .build/common_layer/requirements.txt
    ```
5. Run `cdk deploy' command in the cdk subfolder.
6. Validate the correct deployment of services in Cloudformation.
