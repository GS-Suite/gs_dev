import requests
import json

from dotenv import load_dotenv
load_dotenv()
import os
BASE_URL = os.getenv("BASE_URL")


TOKEN = None
UID = None
PATH = ""


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


def test_create_folder():
    sign_in()
    get_user_classrooms()
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/resources/create_folder/",
        json = {
            "classroom_uid": UID,
            "folder_name": "test_folder",
            "path": f"/classrooms/{UID}"
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True

'''
def test_upload_file():
    global TOKEN, UID

    file = open("test_file.txt", "w")
    file.write("Hello. This is a test file.")
    file.close()
    
    f = open("test_file.txt", 'rb')
    response = requests.post(
        url = f"{BASE_URL}/resources/upload_file/",
        files = {
            "file": (
                f.name, f, 
                "multipart/form-data",
            ),
            "classroom_uid": UID,
            "path": f"/classrooms/{UID}/test_folder"
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True'''


def test_get_files_and_folders():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/resources/get_files_and_folders/",
        json = {
            "classroom_uid": UID,
            "path": f"/classrooms/{UID}"
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True


def test_delete_folder():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/resources/delete_folder/",
        json = {
            "classroom_uid": UID,
            "path": f"/classrooms/{UID}/test_folder"
        },
        headers = {"token": TOKEN}
    )
    assert response.status_code == 200
    
    res = json.loads(response._content)
    assert res["success"] == True
