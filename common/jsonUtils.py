import json

def ReadJson(filepath):
    """
    :param filepath: 文件路径
    :return: 文件中的数据
    """
    with open(file=filepath,mode='r',encoding='utf-8') as file:
        #按照指定路径 模式 编码格式打开文件
        # as file 给这个数据流起个名字叫做file
        json_data=json.load(file)
        return json_data

def Read_Json(filepath):
    with open(file=filepath,mode='r',encoding='utf-8') as file:
        json_data=json.load(file)
        return json_data
