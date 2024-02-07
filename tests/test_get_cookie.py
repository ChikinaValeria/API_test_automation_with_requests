import requests
class TestGetCookieAndHeader():

    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.status_code)
        print(dict(response.cookies))
        cookie_name = 'HomeWork'
        cookie_value = 'hw_value'
        #print(response.cookies[cookie_name])

        assert cookie_name in response.cookies, f"Cannot find cookie with name '{cookie_name}' in the response"

        assert response.cookies[cookie_name] == cookie_value, f"The value of cookie in response doesn't equal {cookie_value}"

    def test_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.status_code)
        print(dict(response.headers))
        header_name = 'x-secret-homework-header'
        header_value = 'Some secret value'
        #print(response.headers[header_name])
        assert header_name in response.headers, f"Cannot find header with name {header_name} in the last response"
        assert response.headers[header_name] == header_value, f"The value of header in response doesn't equal {header_value}"


