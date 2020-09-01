import requests

class TestMenberApi:

    session = requests.Session()

    def setup(self):
        params = {
            "corpid": "wwa13c41f500dfde5f",
            "corpsecret": "H9BPzHWGglF3du4sB6zoc1-9bO-EmSZmLjNu8TY2fc8"
        }
        r = self.session.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        self.session.params.update({"access_token": r.json()['access_token']})

    def test_create(self):
        data = {
            "userid": "zhangsan111",
            "name": "张三",
            "alias": "jackzhang",
            "mobile": "+86 13800000000",
            "department": [1]
        }
        r = self.session.post("https://qyapi.weixin.qq.com/cgi-bin/user/create", json=data)
        assert r.json()["errcode"] == 0
        print(r.json())

    def test_get(self):
        params = {
            "userid": "zhangsan111"
        }
        r = self.session.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get", params=params)
        assert r.json()["errcode"] == 0
        print(r.json())

    def test_update(self):
        data = {
            "userid": "zhangsan111",
            "name": "李四",
            "position": "测试工程师",
            "email": "zhangsan@gzdev.com"
        }
        r = self.session.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update", json=data)
        assert r.json()["errcode"] == 0
        print(r.json())

    def test_delete(self):
        params = {
            "userid": "zhangsan111"
        }
        r = self.session.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=params)
        assert r.json()["errcode"] == 0
        print(r.json())
