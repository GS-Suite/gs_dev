import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os
BASE_URL = os.getenv("BASE_URL")


TOKEN = None
UID = None

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


def test_get_user_dashboard():
    global TOKEN, UID
    response = requests.post(
        url = f"{BASE_URL}/get_user_dashboard/",
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
    UID = res["data"]["uid"]


def test_get_user_classrooms():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/get_user_classrooms/",
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_get_user_enrolled():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/get_user_enrolled/",
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_get_user_profile():
    global TOKEN, UID
    response = requests.post(
        url = f"{BASE_URL}/get_any_user_profile/",
        json = {
            "username": "test_username",
            "user_id": UID
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True