import pytest
from common import jsonUtils
from api.api_reg import RegApi
class Test_RegApi:
    # 去创建夹具
    #参数化
    list1=jsonUtils.ReadJson(r"D:\pythonProject\apiAuto2\data\reg.json")
    @pytest.mark.parametrize('reginfo',list1)
    def test_Reg(self,reg,reginfo):
        self.reg=reg
        self.json={
            "userName": reginfo['userName'],
            "password": reginfo['password'],
            "realName": reginfo['realName']
        }
        resp=self.reg.reg_login(json=self.json)
        # assert resp.status_code == 200
        # assert resp.json()['msg'] == reginfo['msg']
        # in 是判断字符串中存在 ,不能用于json
        # assert '存在' in resp.text
        # assert reginfo['msg_in'] in resp.text
        # assert reginfo['code'] == resp.json()['code']
        print(resp.json())

