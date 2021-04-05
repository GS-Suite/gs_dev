import requests


import requests

response = requests.post("https://gs-suite-dev.herokuapp.com/sign_in/", json = {"username": "keane_pereira", "password": "K3@n3P3r3ir@"})
print(response.status_code)
print()
