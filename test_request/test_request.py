import requests

corpid = "ww7498486774626c7d"
corpsecret = "KfBc78vzqdYYCvFC4Wh-rCglFSSLwNZ1hozVK-3nlEs"


def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    result = requests.get(url).json()
    return result["access_token"]


def test_get():
    token = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=LiZhengYang"
    print(requests.get(url).json())


def test_add():
    token = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    data = {
        "userid": "Akienoijosfd",
        "name": "akien",
        "mobile": "15023521252",
        "department": [1]
    }
    print(requests.post(url, json=data).json())
