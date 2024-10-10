import cv2
from ultralytics import YOLO
from cv2 import getTickCount, getTickFrequency
# 加载 YOLOv8 模型
model = YOLO("runs/detect/train4/weights/best.onnx")

# 获取摄像头内容，参数 0 表示使用默认的摄像头
url = ('rtsp://111.59.214.91:12345/live/cnRzcDovL2FkbWluOmhjd2YyMjg1ODc1QDQ1LjcyLjIxMC40OjU1NC9oMjY0L2NoMS9t'
       'YWluL2F2X3N0cmVhbQ')
cap = cv2.VideoCapture(url)
# cap = cv2.VideoCapture(0)

while cap.isOpened():
    # getTickCount返回从操作系统启动到当前所经过的毫秒数，常常用来判断某个方法执行的时间，其函数原型是DWORD
    loop_start = getTickCount()
    # cap.read()按帧读取视频，ret, frame是获cap.read()方法的两个返回值。 其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，
    # 它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。
    success, frame = cap.read()  # 读取摄像头的一帧图像

    if success:
        # 对当前帧进行目标检测并显示结果
        results = model.predict(source=frame)
    annotated_frame = results[0].plot()

    # 中间放自己的显示程序
    loop_time = getTickCount() - loop_start
    total_time = loop_time / (getTickFrequency())
    FPS = int(1 / total_time)
    # 在图像左上角添加FPS文本
    fps_text = f"FPS: {FPS:.2f}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    # 红色
    text_color = (0, 0, 255)
    # 左上角位置
    text_position = (10, 30)

    cv2.putText(annotated_frame, fps_text, text_position, font, font_scale, text_color, font_thickness)
    cv2.imshow('img', annotated_frame)
    # 等待键盘输入，通过按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
# 关闭OpenCV窗口
cv2.destroyAllWindows()
