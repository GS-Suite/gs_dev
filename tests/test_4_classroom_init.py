import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os
BASE_URL = os.getenv("BASE_URL")


TOKEN = None
UID = None
ENTRY_CODE = None


def sign_in():
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
    sign_in()
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
    global TOKEN, UID
    response = requests.post(
        url = f"{BASE_URL}/get_user_classrooms/",
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
    assert len(res["data"]) == 1
    UID = res["data"][0]["uid"]


def test_generate_join_code():
    global TOKEN, ENTRY_CODE, UID
    response = requests.post(
        url = f"{BASE_URL}/generate_classroom_join_code/",
        json = {
            "classroom_uid": UID
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
    ENTRY_CODE = res["data"]["entry_code"]


def test_get_user_enrolled():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/get_user_enrolled/",
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True