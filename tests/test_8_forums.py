import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os
BASE_URL = os.getenv("BASE_URL")


TOKEN = None
UID = None


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


def get_user_classrooms():
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


def test_create_forum():
    sign_in()
    get_user_classrooms()
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/create_forum/",
        json = {
            "classroom_uid": UID,
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_get_forum_chat():
    global TOKEN, UID
    response = requests.post(
        url = f"{BASE_URL}/get_forum_chat/",
        json = {
            "classroom_uid": UID,
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_send_message():
    global TOKEN, UID
    response = requests.post(
        url = f"{BASE_URL}/send_message/",
        json = {
            "classroom_uid": UID,
            "message": "Hello, welcome to the testing phase",
            "reply_user_id": "",
            "reply_msg_id": ""
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_delete_forum():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/delete_forum/",
        json = {
            "classroom_uid": UID,
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
