import os
import re
from pathlib import Path


def find_file_exists(file_path):
    pattern_json = re.compile(r'.*\.json')
    pattern_jpg = re.compile(r'.*\.jpg')

    file_json = [file for file in os.listdir(file_path) if
                 pattern_json.match(file)]
    file_jpg = [file for file in os.listdir(file_path) if
                pattern_jpg.match(file)]

    for i in range(len(file_json)):
        file_json_name = Path(file_json[i]).stem
        test_path = file_path + file_json_name + ".jpg"
        if not os.path.exists(test_path):
            print(".jpg文件不存在：", test_path)
            json_path = file_path + file_json_name + ".json"
            os.remove(json_path)

    for i in range(len(file_jpg)):
        file_jpg_name = Path(file_jpg[i]).stem
        test_path = file_path + file_jpg_name + ".json"
        if not os.path.exists(test_path):
            print(".json文件不存在：", test_path)
            jpg_path = file_path + file_jpg_name + ".jpg"
            os.remove(jpg_path)
            print("json文件不存在，对应jpg已删除：", jpg_path)


if __name__ == '__main__':
    path = r'D:\\lijianlin\\项目\\软件\\API\\数据集\\两客一危\\0430\\'
    find_file_exists(path)


