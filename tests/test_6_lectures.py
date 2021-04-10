import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os
BASE_URL = os.getenv("BASE_URL")


TOKEN = None
UID = None
LECTURE_UID = None


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


def test_add_lecture():
    sign_in()
    get_user_classrooms()
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/add_lecture/",
        json = {
            "lecture_name": "test_lecture",
            "lecture_link": "https://youtu.be/8vHil1Az2dE",
            "playlists": ["test_playlist"],
            "lecture_description": "A testing description",
            "lecture_resources": "No resources",
            "classroom_uid": UID
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_get_classroom_lecture_videos():
    global TOKEN, UID, LECTURE_UID
    response = requests.post(
        url = f"{BASE_URL}/get_classroom_lecture_videos/",
        json = {
            "classroom_uid": UID
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
    LECTURE_UID = res["data"][0]["_id"]["$oid"]


def test_get_classroom_lecture_playlists():
    global TOKEN, UID
    response = requests.post(
        url = f"{BASE_URL}/get_classroom_lecture_playlists/",
        json = {
            "classroom_uid": UID
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_delete_lecture():
    global TOKEN, UID, LECTURE_UID
    response = requests.post(
        url = f"{BASE_URL}/delete_lecture/",
        json = {
            "classroom_uid": UID,
            "lecture_uid": LECTURE_UID
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True