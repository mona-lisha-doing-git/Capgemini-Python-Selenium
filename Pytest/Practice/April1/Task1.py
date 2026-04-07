import requests

'''
post
get
delete
'''

def Post():
    payload = {
        "id": 111,
        "category": {
            "id": 1,
            "name": "Animal"
        },
        "name": "Tom",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post("https://petstore.swagger.io/v2/pet", json=payload)
    return response.json()['id']


def Get(id1):
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{id1}")
    print(response.text)


def Delete(id1):
    response = requests.delete(f"https://petstore.swagger.io/v2/pet/{id1}")
    print(response.status_code)


id1 = Post()
Get(id1)
Delete(id1)
