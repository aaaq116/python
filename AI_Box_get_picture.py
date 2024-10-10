import requests
import time
import datetime
from io import BytesIO
import os
import PIL.Image


from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

BLOCK_SIZE = 16  # AES 块大小为 16 字节


# 登录鉴权
def login(username, password):
    encrypted_password = "JAUGqzyXgfRhu3/rRP3sjA=="
    url = f"http://192.168.2.223/v1/rbac/token?username={username}&password={encrypted_password}"
    response = requests.post(url)
    if response.status_code == 200:
        token = response.json().get("Data")
        return token
    else:
        raise Exception("登录失败")


# 登录保活
def keep_alive(token):
    url = "http://192.168.2.223/v1/rbac/token"
    # HTTP请求头部（Request Header），可以在前面那里修改名称，它通常用于在客户端与服务器之间传递身份验证令牌（Token）
    headers = {"X-Token": token}
    response = requests.put(url, headers=headers)
    if response.status_code == 200:
        new_token = response.json().get('Data', {}).get('Token')
        return new_token
    else:
        raise Exception("登录保活失败")

# # 加密密码
# def encrypt_password(password, aes_key):
#     cipher = AES.new(aes_key.encode(), AES.MODE_CBC)
#     padding_size = BLOCK_SIZE - len(password) % BLOCK_SIZE
#     padding = chr(padding_size) * padding_size  # 使用 PKCS#7 填充方式
#     padded_password = password + padding
#     encrypted_password = base64.b64encode(cipher.encrypt(padded_password.encode())).decode()
#     print("encrypted_password:", encrypted_password)
#     return encrypted_password


# 获取照片
def get_pictures(token, ids):
    for id in ids:
        # url = "http://192.168.2.223/v1/image/data?id={id}&type=4"
        url = "http://192.168.2.223/v1/image/data?id={}&type=0".format(id)
        headers = {"X-Token": token}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # 将响应内容转换为BytesIO对象,BytesIO存储图片视频等Bytes数据
            image_data = BytesIO(response.content)
            # 使用PIL打开图片 Image接受的参数是一个文件对象，或者类文件对象。所以要么是磁盘上的文件，要么是内存中的BytesIO
            image = PIL.Image.open(image_data)
            # 文件路径
            save_path = "D:\\lijianlin\\项目\\软件\\API\\数据\\0515\\"
            time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            # 文件名
            file_name = (
                    save_path + f'_{time_now}_image{id}.jpg')
            # 将图片保存到本地文件
            image.save(file_name)
            print('{} Image saved successfully.'.format(file_name))
        else:
            raise Exception("获取照片失败")


# 智能检索-机动车
def get_motor_vehicle(token):
    url = ("http://192.168.2.223/v1/analyse/motorVehicle?startTime=2024-05-17 17:40:01&endTime=2024-05-18 19:20:01"
           "&count=500&offset=0&vehicleClass[]=5&vehicleClass[]=6&vehicleClass[]=7&vehicleClass[]=8&vehicleClass[]=14")
    headers = {"X-Token": token}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # id[] = response.json().get('Data', [{}]).get('Base', {}).get('ID')
        # ids = [item.get('FullImage') for item in response.json().get('Data', {})]
        ids = [item.get('FullImage') for item in response.json().get('Data', {})]
        # ids = [item.get('Base', {}).get('ID') for item in response.json().get('Data', [])]
        print("response.json():", response.json().get('Data'))
        return ids
    else:
        raise Exception("智能检索-机动车失败")


# 预警事件
def get_warning_events(token):
    url = ("http://192.168.2.223/v1/warning/events?startTime=2024-04-09 09:32:23&endTime=2024-04-10 18:35:29"
           "&count=500&offset=0&ruleName=&warnType=0")
    headers = {"X-Token": token}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        ids = [item.get('FullImage') for item in response.json().get('Data').get('Info', [])]
        print(len(ids))
        print("response.json():", response.json().get('Data').get('Info', []))
        return ids
    else:
        raise Exception("智能检索-机动车失败")


# 示例用法
username = "admin"
password = "admin"
token = login(username, password)
print("登录成功，Token:", token)

ids = get_motor_vehicle(token)
# ids = get_warning_events(token)

get_pictures(token, ids)

# 每 30 秒调用一次登录保活接口更新 Token
while True:
    try:
        token = keep_alive(token)
        print("Token 更新成功:", token)
        time.sleep(30)  # 休眠 30 秒
    except Exception as e:
        print("登录保活失败:", str(e))
        break
