import pytest

from common.jsonUtils import ReadJson
from config import Base_path


class TestRegApi:
# 用参数化,先要取到数据
    list=ReadJson(r'D:\pythonProject\apiAuto2\data\reg.json')
    @pytest.mark.parametrize('reg_info',list)
    def test_reg(self,reg,reg_info):
        self.reg=reg
        json={
            "userName": reg_info['userName'],
            "password":reg_info['password'] ,
            "realName":reg_info['realName']
        }
        resp=self.reg.RegMethod(json=json)
        print(resp.request.body)
        # print(Base_path)

