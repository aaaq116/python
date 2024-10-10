import os
import sys
import re
import json
import shutil
from pathlib import Path


def find_content_move_file():
    # 输入文件夹地址
    path = r'D:\\20240819'
    buffer = dict()
    num = 0
    # 取路径下的文件名，生成列表
    file_names = os.listdir(path)
    # 遍历列表下的文件名
    for file_name in file_names:
        # 代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
        if file_name != sys.argv[0]:
            # 当文件名以.jpg后缀结尾时
            if file_name.endswith('.json'):
                with open(os.path.join(path, file_name), 'r', encoding='utf-8') as f:
                    # , encoding='utf-8'
                    content = json.load(f)
                    for i in range(len(content['shapes'])):
                        # if content['shapes'][i]['label'] in ["person", "cyclists"]:
                        #     src_path = "D:\\lijianlin\\项目\\软件\\API\\数据集\\两客一危\\0809\\"
                        #     dst_path = "D:\\lijianlin\\项目\\软件\\API\\数据集\\两客一危\\处理\\"
                        if content['shapes'][i]['label'] in ["Dangerous_car", "Minibus", "Large_bus", "van"]:
                            src_path = "D:\\20240819\\"
                            dst_path = "D:\\lijianlin\\项目\\软件\\API\\数据\\img\\img\\20240818\\"
                            # 源文件路径
                            src_file = src_path + file_name
                            # 目标文件夹路径
                            dst_file = dst_path + file_name
                            if not os.path.exists(dst_file):
                                shutil.copy(src_file, dst_file)


def move_file_from_name():
    pattern_json = re.compile(r'.*\.json')
    file_json = \
        [file for file in os.listdir(r'D:\\lijianlin\\项目\\软件\\API\\数据\\img') if
         pattern_json.match(file)]

    # file_json = [file for file in os.listdir(r'D:\\lijianlin\\项目\\软件\\API\\数据集\\两客一危\\0903') if pattern_json.match(file)]
    print(len(file_json))
    for i in range(len(file_json)):
        file_jpg_name = Path(file_json[i]).stem
        src_path = f'D:\\lijianlin\\项目\\软件\\API\\数据\\img\\img\\20240905\\{file_jpg_name}.jpg'
        # # src_path = f'D:\\20240819\\{file_jpg_name}.jpg'
        dst_path = f'D:\\lijianlin\\项目\\软件\\API\\数据\\img\\{file_jpg_name}.jpg'

        # src_path = f'D:\\lijianlin\\项目\\软件\\API\\数据\\img\\img\\20240902\\{file_jpg_name}.jpg'
        # dst_path = f'D:\\lijianlin\\项目\\软件\\API\\数据集\\两客一危\\0903\\{file_jpg_name}.jpg'
        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path)


def del_file():
    pattern_json = re.compile(r'.*\.json')
    file_json = \
        [file for file in os.listdir(r'D:\\lijianlin\\项目\\软件\\API\\数据\\0506') if
         pattern_json.match(file)]
    for i in range(len(file_json)):
        file_jpg_name = Path(file_json[i]).stem
        jpg_path = f'D:\\lijianlin\\项目\\软件\\API\\数据\\0506\\{file_jpg_name}.json'
        os.remove(jpg_path)


if __name__ == '__main__':

    # find_content_move_file()
    move_file_from_name()
    # del_file()
