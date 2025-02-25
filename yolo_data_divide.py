import os
import random
import shutil

# 输入文件夹路径和划分比例
folder_path = input("请输入文件夹路径：")
train_ratio = float(input("请输入训练集比例："))

# 检查文件夹是否存在
if not os.path.exists(folder_path):
    print("文件夹不存在！")
    exit()

# 获取所有jpg和txt文件
jpg_files = [file for file in os.listdir(folder_path) if file.endswith(".jpg")]
txt_files = [file for file in os.listdir(folder_path) if file.endswith(".json")]

# 检查文件数量是否相等
if len(jpg_files) != len(txt_files):
    print("图片和标签数量不匹配！")
    exit()

# 打乱文件顺序
random.shuffle(jpg_files)

# 划分训练集和验证集
train_size = int(len(jpg_files) * train_ratio)
train_jpg = jpg_files[:train_size]
train_txt = [file.replace(".jpg", ".json") for file in train_jpg]
val_jpg = jpg_files[train_size:]
val_txt = [file.replace(".jpg", ".txt") for file in val_jpg]

# 创建文件夹和子文件夹
if not os.path.exists("{}\\images\\train".format(folder_path)):
    os.makedirs("{}\\images\\train".format(folder_path))
if not os.path.exists("{}\\images\\val".format(folder_path)):
    os.makedirs("{}\\images\\val".format(folder_path))
if not os.path.exists("{}\\labels\\train".format(folder_path)):
    os.makedirs("{}\\labels\\train".format(folder_path))
if not os.path.exists("{}\\labels\\val".format(folder_path)):
    os.makedirs("{}\\labels\\val".format(folder_path))

# 复制文件到目标文件夹
for file in train_jpg:
    shutil.copy(os.path.join(folder_path, file), "{}\\images\\train".format(folder_path))
for file in train_txt:
    shutil.copy(os.path.join(folder_path, file), "{}\\labels\\train".format(folder_path))
for file in val_jpg:
    shutil.copy(os.path.join(folder_path, file), "{}\\images\\val".format(folder_path))
for file in val_txt:
    shutil.copy(os.path.join(folder_path, file), "{}\\labels\\val".format(folder_path))

print("处理完成！")
