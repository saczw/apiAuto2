import requests

from config import base_url


class ReqApi:
    # 初始化
    def __init__(self):
        self.url=base_url+'exam/api/sys/user/reg'
        self.headers={
            'content-type':'application/json'
        }
    def RegMethod(self,json):
        resp=requests.post(url=self.url,headers=self.headers,json=json)
        return resp