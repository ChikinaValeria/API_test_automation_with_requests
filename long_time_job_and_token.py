import requests
import time

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response1.text)
print(response1.status_code)
# парсим джейсон
parsed_response_text = response1.json()
# сохраняем токен в переменную
token = parsed_response_text["token"]
# сохраняем скорость выполнения в переменную
seconds = parsed_response_text["seconds"]
# формируем параметр гет-запроса в виде словаря
data = {"token": token}

# запрос раньше времени (Job is NOT ready)
time.sleep(5)
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params = data)
print(response2.text)
print(response2.status_code)

# запрос по истечении срока выполнения таски (Job is ready)
time.sleep(seconds-5)
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params = data)
print(response3.text)
print(response3.status_code)



