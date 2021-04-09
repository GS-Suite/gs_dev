import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os


BASE_URL = os.getenv("BASE_URL")


def sign_in():
    response = requests.post(
        url = f"{BASE_URL}/sign_in/",
        json = {"username": "test_username", "password": "test_password"}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
    return res["token"]