import requests
class TestGetCookie():
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.status_code)
        print(dict(response.cookies))
        cookie_name = 'HomeWork1'
        cookie_value = 'hw_value'
        #print(response.cookies[cookie_name])

        assert cookie_name in response.cookies, f"Cannot find cookie with name '{cookie_name}' in the response"

        assert response.cookies[cookie_name] == cookie_value, f"The value of cookie in response doesn't equal {cookie_value}"


