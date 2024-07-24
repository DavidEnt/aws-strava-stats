import datetime
import boto3
import json

import strava


def lambda_handler(event, context):
    access_token = strava.authenticate()
    activities = strava.list_activities(
        access_token, after=datetime.datetime.now() - datetime.timedelta(days=7)
    )

    active_hours = 0
    for act in activities:
        active_hours += act["moving_time"] / 3600

    message = {
        "subject": "Weekly Strava Report",
        "html_txt": f"Last week you were active for {round(active_hours, 1)} hours.",
        "to_addresses": ["david.enthoven@live.nl"],
    }
    print(f"Sending the following message: {message}")

    sqs_client = boto3.client("sqs")
    sqs_client.send_message(
        QueueUrl="https://sqs.eu-west-1.amazonaws.com/077369991239/emails-to-send-out",
        MessageBody=json.dumps(message),
    )