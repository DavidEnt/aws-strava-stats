from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_events as events,
    aws_events_targets as events_targets,
)
from constructs import Construct


class ScheduledLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        layer = _lambda.LayerVersion.from_layer_version_arn(
            self,
            "Layer_Version",
            "arn:aws:lambda:eu-west-1:077369991239:layer:requests:1",
        )

        # Define the Lambda function resource
        lambda_function = _lambda.Function(
            self,
            "Lambda_Function",
            runtime=_lambda.Runtime.PYTHON_3_10,
            code=_lambda.Code.from_asset(
                "lambda"
            ),  # Points to the lambda directory,
            handler="main.lambda_handler",  # Points to the file and function in the lambda directory
            layers=[layer],
        )

        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["sqs:SendMessage"],
                resources=["*"],
            )
        )

        schedule = events.Rule(
            self,
            "weekly-strava-trigger",
            targets=[events_targets.LambdaFunction(lambda_function)],
            schedule=events.Schedule.cron(minute="0", hour="23", week_day="1",)
        )