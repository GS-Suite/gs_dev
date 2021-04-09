import requests
import json

from tests.functions import sign_in

TOKEN = None


def test_sign_in():
    global TOKEN
    TOKEN = sign_in()


def test_sign_out():
    global TOKEN
    response = requests.post(
        url = f"{BASE_URL}/sign_out/",
        headers = {
            "token": TOKEN
        }
    )
    assert response.status_code == 200

    res = json.loads(response._content)
    assert res["success"] == True
    TOKEN = None