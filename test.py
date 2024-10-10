# import os
# import sys
# import json
# from pathlib import Path
#
#
# # 文件名增加指定字符
# # os.walk方法：在父文件夹下，将所有某种类型的文件（无论其在子文件夹里还是子文件夹外）加上前缀
# def modify_files_data(file_path):
#     buffer = dict()
#     # 取路径下的文件名，生成列表
#     file_names = os.listdir(file_path)
#     # 遍历列表下的文件名
#     for file_name in file_names:
#         # 代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
#         if file_name != sys.argv[0]:
#             # 当文件名以.jpg后缀结尾时
#             if file_name.endswith('.json'):
#                 with open(os.path.join(path, file_name), 'r') as f:
#                     content = json.load(f)
#                     file_image_path = Path(content['imagePath']).stem + ".jpg"
#                     content['imagePath'] = file_image_path
#                 buffer = content
#                 with open(os.path.join(path, file_name), 'w') as write_f:
#                     json.dump(buffer, write_f, indent=4, ensure_ascii=False)
#                 write_f.close()
#
#
# if __name__ == '__main__':
#     # 输入文件夹地址
#     path = r'D:\\lijianlin\\项目\\软件\\API\\数据集\\两客一危\\0719'
#     modify_files_data(path)

import os
folder_path = input("请输入文件夹路径：")
# 创建文件夹和子文件夹
path = "{}\\images\\train".format(folder_path)
if not os.path.exists(path):
    os.makedirs(path)
