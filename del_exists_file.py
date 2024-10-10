import os
import re


# 输入文件夹地址
dst_path = r'C:\\Users\\cgn12\\Desktop\\New folder1\\20240907\\'
src_path = r'D:\\lijianlin\\项目\\软件\\API\\数据\\img\\img\\20240901\\'

# 取路径下的文件名，生成列表
src_file_names = os.listdir(src_path)
dst_file_names = os.listdir(dst_path)

# compile 函数用于编译正则表达式，生成一个 Pattern 对象
pattern_json = re.compile(r'.*\.json')
pattern_jpg = re.compile(r'.*\.jpg')

src_json_file = [file for file in src_file_names if pattern_json.match(file)]
src_jpg_file = [file for file in src_file_names if pattern_jpg.match(file)]

dst_json_file = [file for file in dst_file_names if pattern_json.match(file)]
dst_jpg_file = [file for file in dst_file_names if pattern_jpg.match(file)]

# 集合set 无序的不重复元素序列
common_jsons = set(src_json_file) & set(dst_json_file)
print("两个文件夹下存在共同的json文件:", common_jsons)

common_jpgs = set(src_jpg_file) & set(dst_jpg_file)
print("两个文件夹下存在共同的jpg文件:", common_jpgs)

for file in common_jsons:
    test_file = dst_path + file
    if os.path.exists(test_file):
        os.remove(test_file)
        print("删除共同json文件：", test_file)

for file in common_jpgs:
    test_file = dst_path + file
    if os.path.exists(test_file):
        os.remove(test_file)
        print("删除共同jpg文件：", test_file)
