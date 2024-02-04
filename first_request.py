import requests
from json.decoder import JSONDecodeError

payload = {"name":"User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params = payload)
print(response.text)
print(response.status_code)
try:
    parsed_response_text = response.json()
    print(parsed_response_text["answer"])
except JSONDecodeError:
    print("Respose is not JSON")

response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1":"value1"})
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1":"value1"})
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
second_response = response
print(response.status_code)
print(first_response.url)
print(second_response.url)

headers = {"some_header":"U123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)
print(response.text)
print(response.headers)