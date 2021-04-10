import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os
BASE_URL = os.getenv("BASE_URL")


TOKEN = None
UID = None
ANNOUNCEMENT_ID = None


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


def test_create_announcement_pane():
    sign_in()
    get_user_classrooms()
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/create_announcement_pane/",
        json = {
            "classroom_uid": UID,
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_get_all_announcements():
    global TOKEN, UID
    response = requests.post(
        url = f"{BASE_URL}/get_all_announcements/",
        json = {
            "classroom_uid": UID,
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_post_announcement():
    global TOKEN, UID
    response = requests.post(
        url = f"{BASE_URL}/post_announcement/",
        json = {
            "classroom_uid": UID,
            "announcement": '''
            Announcement Test!!!!!
            okay.
            '''
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_get_all_announcements_again():
    global TOKEN, UID, ANNOUNCEMENT_ID
    response = requests.post(
        url = f"{BASE_URL}/get_all_announcements/",
        json = {
            "classroom_uid": UID,
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
    ANNOUNCEMENT_ID = res["data"]["forum_stuff"]["posts"][0]["announcement_id"]


def test_delete_announcement():
    global TOKEN, ANNOUNCEMENT_ID
    response = requests.post(
        url = f"{BASE_URL}/delete_announcement/",
        json = {
            "classroom_uid": UID,
            "announcement_id": ANNOUNCEMENT_ID
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
