import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os
BASE_URL = os.getenv("BASE_URL")


TOKEN = None
UID = None
ENTRY_CODE = None
ATTENDANCE_CODE = None

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


def test_take_attendance():
    sign_in()
    get_user_classrooms()
    global TOKEN, ATTENDANCE_CODE
    response = requests.post(
        url = f"{BASE_URL}/take_attendance/",
        json = {
            "classroom_uid": UID,
            "timeout_minutes": 30
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
    ATTENDANCE_CODE = res["data"]["attendance_token"]


def test_give_attendance():
    global TOKEN, UID
    response = requests.post(
        url = f"{BASE_URL}/take_attendance/",
        json = {
            "classroom_uid": UID,
            "attendance_token": ATTENDANCE_CODE
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


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


def test_view_student_attendance():
    global TOKEN, UID
    response = requests.post(
        url = f"{BASE_URL}/view_student_attendance/",
        json = {
            "classroom_uid": UID
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_view_classroom_attendance():
    global TOKEN, UID
    response = requests.post(
        url = f"{BASE_URL}/view_classroom_attendance/",
        json = {
            "classroom_uid": UID
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_stop_attendance():
    global TOKEN, UID, ATTENDANCE_CODE
    response = requests.post(
        url = f"{BASE_URL}/stop_attendance/",
        json = {
            "classroom_uid": UID,
            "attendance_token": ATTENDANCE_CODE
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_delete_user_attendance():
    global TOKEN, UID, ATTENDANCE_CODE
    response = requests.post(
        url = f"{BASE_URL}/delete_user_attendance/",
        json = {
            "classroom_uid": UID,
            "attendance_token": ATTENDANCE_CODE
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True