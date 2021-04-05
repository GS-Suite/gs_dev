import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os


BASE_URL = os.getenv("BASE_URL")

TOKEN = None

def test_sign_up_new():
    response = requests.post(
        url = f"{BASE_URL}/sign_up/",
        json = {
            "username": "test_username",
            "password": "test_password",
            "email": "test.gs.suite@gmail.com",
            "first_name": "test_first_name",
            "last_name": "test_last_nam"
        }
    )
    assert response.status_code == 200

    res = json.loads(response._content)
    assert res["success"] == True


def test_sign_up_existing():
    response = requests.post(
        url = f"{BASE_URL}/sign_up/",
        json = {
            "username": "test_username",
            "password": "test_password",
            "email": "test.gs.suite@gmail.com",
            "first_name": "test_first_name",
            "last_name": "test_last_name"
        }
    )
    assert response.status_code == 200

    res = json.loads(response._content)
    assert res["success"] == False


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


def test_sign_out():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/sign_out/",
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
    TOKEN = None