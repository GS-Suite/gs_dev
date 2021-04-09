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


def test_create_classroom():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/create_classroom/",
        json = {
            "class_name": "test_classroom1"
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_get_user_classrooms():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/get_user_classrooms/",
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
    assert len(res["data"]) == 1


def test_get_user_enrolled():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/get_user_enrolled/",
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True