# encoding: utf-8
import requests
import requests.packages
import json
salt_api = "http://192.168.1.11:8000/"


class SaltApi:
    """
    定义salt api接口的类
    初始化获得token
    """
    def __init__(self):
        self.url = "http://192.168.1.11:8000/"
        self.username = "saltapi"
        self.password = "saltapi"
        self.headers = {
            "Content-type": "application/json"
        }
        self.params = {"client": "local", "fun": "", "tgt": ""}
        # self.params = {`client`: `local`, `fun`: ``, `tgt`: ``, `arg`: ``}
        self.login_url = self.url + "login"
        self.login_params = {"username": self.username, "password": self.password, "eauth": "pam"}
        self.token = self.get_data(self.login_url, self.login_params)["token"]
        self.headers["X-Auth-Token"] = self.token

    def get_data(self, url, params):
        send_data = json.dumps(params)
        request = requests.post(url, data=send_data, headers=self.headers, verify=False)
        # response = request.text
        # response = eval(response)     使用x-yaml格式时使用这个命令把回应的内容转换成字典
        # print response
        # print request
        # print type(request)
        response = request.json()
        result = dict(response)
        # print result
        return result["return"][0]

    def salt_command(self, tgt, method, arg=None):
        if arg:
            params = {"client": "local", "fun": method, "tgt": tgt, "arg": arg}
        else:
            params = {"client": "local", "fun": method, "tgt": tgt}

        result = self.get_data(self.url, params)
        return result

    def list_all_key(self):
        params = {'client': 'wheel', 'fun': 'key.list_all'}
        result = self.get_data(self.url, params)
        return result





