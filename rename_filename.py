import os
import sys
import datetime


# 文件名增加指定字符
# os.walk方法：在父文件夹下，将所有某种类型的文件（无论其在子文件夹里还是子文件夹外）加上前缀
def rename_files_add_char(file_path):
    time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # 用os.walk方法取得path路径下的文件夹路径，子文件夹名，所有文件名
    for foldName, subfolders, filenames in os.walk(file_path):
        # 遍历列表下的文件名
        for filename in filenames:
            # 代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
            if filename != sys.argv[0]:
                # 当文件名以.jpg后缀结尾时
                if filename.endswith('.jpg'):
                    # 重命名文件
                    id = id - 1
                    mark = f'{time_now}_image{id}.jpg'
                    os.rename(os.path.join(foldName, filename), os.path.join(foldName, mark))
                    print(filename, "has been renamed successfully! New name is: ", mark)


# os.listdir方法，只修改父文件夹下的某种类型文件名，子文件夹里的同种类型文件不受影响。
# def rename_files_add_char():
#     # 准备添加的前缀内容
#     mark = '5_daxinghuoche_'
#     # 取路径下的文件名，生成列表
#     old_names = os.listdir(path)
#     # 遍历列表下的文件名
#     for old_name in old_names:
#         # 代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
#         if old_name != sys.argv[0]:
#             # 当文件名以.jpg后缀结尾时
#             if old_name.endswith('.jpg'):
#                 # 重命名文件
#                 os.rename(os.path.join(path, old_name), os.path.join(path, mark+old_name))
#                 print(old_name, "has been renamed successfully! New name is: ", mark+old_name)


# 删除文件名称中特定字符
def rename_files_remove_char(file_path):
    files = os.listdir(file_path)
    # 输出所有文件名
    for file in files:
        print(file)
    # 获取旧名和新名
    i = 0
    for file in files:
        # old 旧名称的信息
        old = path + os.sep + files[i]
        # new是新名称的信息，删除字符
        new = path + os.sep + file.replace('new_', '')
        # 新旧替换
        os.rename(old, new)
        i += 1


if __name__ == '__main__':
    # 输入文件夹地址
    path = r'C:\Users\cgn12\Desktop\New folder1\塌陷\隧道坍塌'
    rename_files_add_char(path)
    # rename_files_remove_char(path)
