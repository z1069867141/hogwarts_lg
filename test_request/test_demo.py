import requests
from hamcrest import *
from requests.auth import HTTPBasicAuth


class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        print(r.raw.read(10))
        print(r.request)
        assert r.status_code == 200

    def test_header(self):
        r = requests.post('https://httpbin.testing-studio.com/post', headers={"h": "header demo"})
        assert r.json()['headers']['H'] == "header demo"

    def test_json(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.json()['json']['level'] == 1

    def test_xmk(self):
        xml = """<?xml version='1.0' encoding='utf-8'?>
        <a>6<a>"""
        headers = {"Content-Type": "application/xml"}
        r = requests.post('https://httpbin.testing-studio.com/post', data=xml, headers=headers)
        print(r.json())

    def test_hamcrest(self):
        url = "https://home.testing-studio.com/categories.json"
        r = requests.get(url)
        print(r.json())
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('开源项目'))

    def test_cookie_header(self):
        url = "https://httpbin.testing-studio.com/cookies"
        header = {"Cookie": "hogwarts=school",
                  'User-Agent': 'hogwarts'}
        r = requests.get(url, headers=header)
        print(r.request.headers)

    def test_cookie_add(self):
        url = "https://httpbin.testing-studio.com/cookies"
        header = {'User-Agent': 'hogwarts'}
        cookie_data = {"hogwarts": "school",
                       "teacher": "AD"}
        r = requests.get(url, headers=header, cookies=cookie_data)
        print(r.request.headers)

    def test_oauth(self):
        r = requests.get(url="https://httpbin.testing-studio.com/basic-auth/oaisdjfoifadj/51651",
                         auth=HTTPBasicAuth("oaisdjfoifadj", "51651"))
