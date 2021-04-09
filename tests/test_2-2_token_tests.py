import requests
import json


from dotenv import load_dotenv
load_dotenv()
import os
BASE_URL = os.getenv("BASE_URL")

TOKEN = None


def test_sign_in():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/sign_in/",
        json = {"username": "test_username", "password": "test_password"}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
    TOKEN = res["token"]


def test_token_validation():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/validate_token/",
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
    TOKEN = res["token"]


def test_token_refresh():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/refresh_token/",
        headers = {"token": TOKEN}
    )
    assert response.status_code == 500

    res = json.loads(response._content)
    assert res["success"] == True
    TOKEN = res["token"]