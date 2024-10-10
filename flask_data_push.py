# 订阅通知:设备作为服务端，数据接收者作为客户端，数接收者主动连接设备推送端口接收数据，通信链路为websocket
# 主动推送:设备作为客户端，数据接收者作为服务端，设备主动连接数据接收者服务端口推送数据， 通信链路有websocket、http两种方式
# 一般情况下，设备与接收者处于同一内网环境时，可选择主动推送或订阅通知任意一种方案； 设备处于局域网，接收者处于公网环境时，建议使用主动推送方案
# import flask
# import json
# from flask import request
from flask import jsonify
#
# # 推送
# server = flask.Flask(__name__)
#
#
# @server.route('/login', methods=['GET', 'POST'])
# def login():
#
#     info = {'Code': 200, 'Message': 'msg: success', 'Translate': "操作成功", 'Detail': "", "Data": ""}
#     # 将字典转换为json串, json是字符串
#     print(info)
#     return json.dumps(info, ensure_ascii=False)
#
#
# @server.route('/alarm_data', methods=['GET', 'POST'])
# def get_data():
#
#     print(data)
#     return jsonify({'message': 'Data received successfully'})
#
#
# if __name__ == "__main__":
#     server.run(host='192.168.12.208', port=8000, debug=True)


from flask import Flask, request
import os
app = Flask(__name__)


@app.route('/alarm_data', methods=['POST'])
def index():
    # file = request.files['file']
    # if file is None:
    #     return {'message': '文件发送失败'}
    header = request.headers.get('Content-Type')
    print(header)
    # to_dict函数将数据框数据转换为字典形式
    data = request.values.to_dict()
    print("data_to dict:", data)
    # 设置了Content - Type: application / json的Body数据只能通过request.json
    # data = request.get_json()

    # file_path = os.path.join('images', data['full_path'])
    # file_dir = os.path.dirname(file_path)
    # os.makedirs(file_dir, exist_ok=True)
    # file.save(file_path)
    return jsonify({'message': 'Data received successfully'})


if __name__ == '__main__':
    app.run(host='192.168.12.208', port=8000, debug=True)

    # request 属性：
    # 1、values:内容是form和args;
    # 2、headers:请求头,字典类型;
    # 3、data:包含了请求的数据，并转换为字符串;
    # 4、json:mimetype是application/json,这个参数将会解析JSON数据,如果不是则返回None,可以使用这个替代get_json()方法;
    # 5、files:MultiDict，带有通过POST或PUT请求上传的文件;

    # Content-Type 实体头部用于指示资源的MIME类型media type, 告诉客户端实际返回的内容的内容类型
    # multipart/form-data 可用于HTML表单从浏览器发送信息给服务器
