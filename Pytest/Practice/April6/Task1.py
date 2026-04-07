import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urllib3.disable_warnings()
base_url = "https://www.shoppersstack.com/shopping"

token = ""
UserId = ""

def add_shopper():
    body = {
        "city": "Banglore",
        "country": "India",
        "email": "monalisha@gmail.com",
        "firstName": "hello",
        "gender": "FEMALE",
        "lastName": "world",
        "password": "password",
        "phone": 9234567890,
        "state": "Karnataka",
        "zoneId": "ALPHA"
    }

    response = requests.post(f"{base_url}/shoppers",json=body, verify=False)

    print(response.status_code)
    print(response.json())

def user_login():
    global token, UserId
    body = {
        "email": "monalisha@gmail.com",
        "password": "password",
        "role": "SHOPPER"
        }

    response = requests.post(f"{base_url}/users/login", json=body, verify=False)

    print(response.status_code)
    print(response.json())
    token = response.json()["data"]['jwtToken']
    UserId = response.json()["data"]['userId']
    print(f"Token value: {token}")
    print(f"User Id: {UserId}")

def get_user_info():
    header = { "Authorization": f"Bearer {token}"}
    response = requests.get(f"{base_url}/shoppers/{UserId}",
                headers=header, verify=False)
    print(response.status_code)
    print(response.json())


add_shopper()
user_login()
get_user_info()