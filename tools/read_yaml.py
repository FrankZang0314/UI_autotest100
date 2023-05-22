import os
import yaml

from config import BASE_PATH


def read_yaml(filename):
    file_path=BASE_PATH+os.sep+"data"+os.sep+filename
    print("----------------")
    print(BASE_PATH)                 #  F:\黑马\2021软件测试全套\3天由浅入深黑马头条软件测试实战\资料-3天由浅入深黑马头条软件测试实战\3天黑马头条项目代码+笔记\ui自动化代码\ui自动化代码\UI_autotest
    print(file_path)                 #  F:\黑马\2021软件测试全套\3天由浅入深黑马头条软件测试实战\资料-3天由浅入深黑马头条软件测试实战\3天黑马头条项目代码+笔记\ui自动化代码\ui自动化代码\UI_autotest\data\mp_login.yaml
    arr=[]
    # with open("../data/mp_login.yaml","r",encoding="utf-8") as f:
    with open(file_path, "r", encoding="utf-8") as f:                #动态路径
    #     print(yaml.safe_load(f).values())
        for datas in yaml.safe_load(f).values():
            # arr.append(datas.values)
            # print(datas)                                            #{'userame': '13812345678', 'code': '26810', 'expect': '13812345678'}
            arr.append(tuple(datas.values()))
    return arr


# def read_yaml():
#     # file_path=BASE_PATH+os.sep+"data"+os.sep+filename
#     arr=[]
#     with open("../data/mp_login.yaml","r",encoding="utf-8") as f:
#     # with open(file_path, "r", encoding="utf-8") as f:                #动态路径
#     #     print(yaml.safe_load(f).values())
#         for datas in yaml.safe_load(f).values():
#             print(datas)                    #{'userame': '13812345678', 'code': '26810', 'expect': '13812345678'}
#             # arr.append(datas.values())     # [dict_values(['13812345678', '26810', '13812345678'])]
#             # arr.append(list(datas.values())) #[['13812345678', '26810', '13812345678']] list和tuple都可以，一般选择tuple
#             arr.append(tuple(datas.values()))  # [('13812345678', '26810', '13812345678')]
#     return arr

if __name__ == '__main__':
    # print(read_yaml())
    print(read_yaml("mp_login.yaml"))