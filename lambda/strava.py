import requests
import urllib3
from typing import Any
import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AUTH_URL = "https://www.strava.com/oauth/token"
ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"


def authenticate() -> str:
    print("Requesting Access Token...")
    payload = {
        "client_id": "129381",
        "client_secret": "a90122f7856af6db5c0025c6150aba946f365439",
        "refresh_token": "a2c0932160c8e7d448db048a6f89f2596fbfc990",
        "grant_type": "refresh_token",
        "f": "json",
    }

    res = requests.post(AUTH_URL, data=payload, verify=False)
    access_token = res.json()["access_token"]
    print(f"Access Token = {access_token}")

    return access_token


def list_activities(
    access_token: str,
    after: datetime.datetime = datetime.datetime(2000, 1, 1),
    per_page: int = 30,
    page: int = 1,
) -> dict[Any, Any]:
    print("Requesting Activities ...")

    header = {"Authorization": "Bearer " + access_token}

    activities = requests.get(
        ACTIVITIES_URL,
        headers=header,
        params={"after": after.timestamp(), "per_page": per_page, "page": page},
    ).json()
    print(f"A total of {len(activities)} activites retrieved")

    return activities
