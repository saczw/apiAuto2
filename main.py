# 生成allure测试报告
import os

import pytest

pytest.main(["--alluredir=./report/allure_result", "--clean-alluredir"])

os.system("allure generate ./report/allure_result -o ./report/allure_report --clean")
