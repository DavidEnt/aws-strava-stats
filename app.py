#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk.stack import ScheduledLambdaStack

app = cdk.App()
ScheduledLambdaStack(
    app,
    "StravaStats",
)
app.synth()
