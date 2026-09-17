# -*- coding: utf-8 -*-
import subprocess
import os
import shutil
import sys

if __name__ == '__main__':
    # Jenkins内置环境变量 WORKSPACE，代表job工作空间根目录
    workspace = os.environ.get("WORKSPACE", os.getcwd())
    allure_results = os.path.join(workspace, "report", "allure-results")

    # 删除旧结果文件夹
    if os.path.exists(allure_results):
        shutil.rmtree(allure_results)
    # 新建空文件夹
    os.makedirs(allure_results, exist_ok=True)

    print("===== 开始执行pytest测试 =====")
    print(f"allure原始结果保存路径：{allure_results}")
    py_path = sys.executable
    pytest_cmd = [py_path, "-m", "pytest", f"--alluredir={allure_results}"]
    pytest_ret = subprocess.run(pytest_cmd, check=False)

    print("\n执行结束！")
    print(f"pytest返回码：{pytest_ret.returncode}")
