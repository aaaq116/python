import os
import sys
import json


# 文件名增加指定字符
# os.walk方法：在父文件夹下，将所有某种类型的文件（无论其在子文件夹里还是子文件夹外）加上前缀
def modify_files_data(file_path):
    buffer = dict()
    # 取路径下的文件名，生成列表
    file_names = os.listdir(file_path)
    # 遍历列表下的文件名
    for file_name in file_names:
        # 代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
        if file_name != sys.argv[0]:
            # 当文件名以.jpg后缀结尾时
            if file_name.endswith('.json'):
                with open(os.path.join(path, file_name), 'r') as f:
                    content = json.load(f)
                    for i in range(len(content['shapes'])):
                        # 类别0 truck
                        if content['shapes'][i]['label'] in ["Crane", "Truck_head"]:
                            content['shapes'][i]['label'] = "truck"
                        # 类别1 van
                        if content['shapes'][i]['label'] in ["Commercial_car", "Mini_van",
                                                             "Escort_vehicle"]:
                            content['shapes'][i]['label'] = "van"
                        # 类别2 mini_truck
                        if content['shapes'][i]['label'] in ["pickup_truck", "Engineering_repair_car", "mixer_truck",
                                                             "Sanitation_truck", "motor_home", "Pickup_truck", "pickup"]:
                            content['shapes'][i]['label'] = "Mini_truck"
                        # 类别3 car
                        if content['shapes'][i]['label'] in ["suv"]:
                            content['shapes'][i]['label'] = "car"
                        # 类别3 Minibus
                        if content['shapes'][i]['label'] in ["breakdown_van"]:
                            content['shapes'][i]['label'] = "Minibus"
                buffer = content
                with open(os.path.join(path, file_name), 'w') as write_f:
                    json.dump(buffer, write_f, indent=4, ensure_ascii=False)
                write_f.close()


def get_files_content_num(file_path):
    car_nums = 0
    van_nums = 0
    Mini_truck_nums = 0
    truck_nums = 0
    Dangerous_car_nums = 0
    Minibus_nums = 0
    Large_bus_nums = 0
    person_nums = 0

    # 取路径下的文件名，生成列表
    file_names = os.listdir(file_path)
    # 遍历列表下的文件名
    for file_name in file_names:
        # 代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
        if file_name != sys.argv[0]:
            # 当文件名以.jpg后缀结尾时
            if file_name.endswith('.json'):
                with open(os.path.join(path, file_name), 'r') as f:
                    content = json.load(f)
                    for i in range(len(content['shapes'])):
                        # 类别0 truck
                        if content['shapes'][i]['label'] not in ["car", "van", "Mini_truck", "truck", "person",
                                                                 "Dangerous_car", "Minibus", "Large_bus"]:
                            print(file_name, content['shapes'][i]['label'])
                        if content['shapes'][i]['label'] == "car":
                            car_nums += 1
                        if content['shapes'][i]['label'] == "van":
                            van_nums += 1
                        if content['shapes'][i]['label'] == "Mini_truck":
                            Mini_truck_nums += 1
                        if content['shapes'][i]['label'] == "truck":
                            truck_nums += 1
                        if content['shapes'][i]['label'] == "Dangerous_car":
                            Dangerous_car_nums += 1
                        if content['shapes'][i]['label'] == "Minibus":
                            Minibus_nums += 1
                        if content['shapes'][i]['label'] == "Large_bus":
                            Large_bus_nums += 1
                        if content['shapes'][i]['label'] == "person":
                            person_nums += 1
                f.close()
    print("car label nums:", car_nums)
    print("van label nums:", van_nums)
    print("Mini_truck label nums:", Mini_truck_nums)
    print("truck label nums:", truck_nums)
    print("Dangerous_car label nums:", Dangerous_car_nums)
    print("Minibus label nums:", Minibus_nums)
    print("Large_bus label nums:", Large_bus_nums)
    print("person label nums:", person_nums)


if __name__ == '__main__':
    # 输入文件夹地址
    path = r'D:\\lijianlin\\项目\\软件\\API\\数据集\\两客一危\\0711'
    # modify_files_data(path)
    get_files_content_num(path)
