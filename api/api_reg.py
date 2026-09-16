import requests

from config import base_url

class RegApi:
    # 初始化方法
    def __init__(self):
        # 创建属性  不变的东西，都可以做成属性
        self.url=base_url+'/exam/api/sys/user/reg'
        self.headers={
            'content-type':'application/json'
        }
    def reg_login(self,json):
        session=requests.Session()
        resp=session.post(url=self.url,headers=self.headers,json=json)
        return resp
