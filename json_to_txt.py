# 将lableme生成json文件转化为yolov8模型训练所需要格式;
# 方法一：可使用如下命令将json文件转化为yolov8模型训练txt格式
# labelme2yolo --json_dir /path/to/labelme_json_dir/
# 方法二：运行如下脚本
import json
import os
from tqdm import tqdm


def convert_label(json_dir, save_dir):
    json_paths = os.listdir(json_dir)
    classes = ["Dangerous_car", "Mini_truck", "Large_bus", "car", "Minibus", "truck", "van"]

    # tqdm是一个快速、可扩展的Python进度条，监测程序运行的进度，运行的时长
    for file in tqdm(json_paths):
        path = os.path.join(json_dir, file)
        with open(path, 'r', encoding='utf-8') as load_f:
            json_dict = json.load(load_f)
        h, w = json_dict['imageHeight'], json_dict['imageWidth']

        # save txt path
        txt_path = os.path.join(save_dir, file.replace('json', 'txt'))
        txt_file = open(txt_path, 'w', encoding='utf-8')

        for shape_dict in json_dict['shapes']:
            label = shape_dict['label']
            label_index = classes.index(label)
            points = shape_dict['points']

            x_data = []
            y_data = []

            for point in points:
                x_data.append(point[0])
                y_data.append(point[1])
            # xp、yp表示目标中心点相对坐标，其中xp等于目标的绝对横坐标除以图像宽度，yp等于目标的绝对纵坐标除以图像高度
            xp = round(((x_data[0] + x_data[1]) / 2 / w), 6)
            yp = round(((y_data[0] + y_data[1]) / 2 / h), 6)
            # wp和hp表示目标的相对宽度和高度，其中wp等于目标的绝对宽度除以图像宽度，hp等于目标的绝对高度除以图像高度
            wp = round(((abs(x_data[0] - x_data[1])) / w), 6)
            hp = round(((abs(y_data[0] - y_data[1])) / h), 6)

            points_nor_list = [xp, yp, wp, hp]

            # 将 points_nor_list数据转化为字符串形式
            points_nor_list = list(map(lambda x: str(x), points_nor_list))
            points_nor_str = ' '.join(points_nor_list)

            label_str = str(label_index) + ' ' + points_nor_str + '\n'
            # writelines 用于向文件中写入一序列的字符串
            txt_file.writelines(label_str)


if __name__ == "__main__":
    json_path = 'D:\\lijianlin\\Software\\Annotations'
    save_path = 'D:\\lijianlin\\Software\\datasets'

    convert_label(json_path, save_path)

