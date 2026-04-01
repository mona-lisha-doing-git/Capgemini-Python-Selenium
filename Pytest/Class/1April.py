import requests

# response1 = requests.get("https://petstore.swagger.io/v2/store/inventory")
# print(response1.text)
# print(response1.status_code)
# print(response1.json())

# response2 = requests.get("https://petstore.swagger.io/v2/findByStatus?status=sold")
# print(response1.text)
# print(response1.status_code)
# print(response1.json())

response3 = requests.get("https://petstore.swagger.io/v2/pet/1390")
# assert 200 == response3.status_code, f"Not successful, it is {response3.status_code}"
#
# print(response3.status_code)

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

response4 = requests.post("https://petstore.swagger.io/v2/pet", json=payload)

assert 200 == response4.status_code, f'Not successful, {response4.status_code}'

print(response4.status_code)
print(response4.text)

response5 = requests.delete("https://petstore.swagger.io/v2/pet/111")

assert 200 == response5.status_code, f'Not successful, {response5.status_code}'

print(response5.status_code)
print(response5.json())
