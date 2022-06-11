import os
import cv2
import subprocess
str = 'mqpka89045321@#$%^&*()_=||||}'	# 字符表
video = cv2.VideoCapture(os.path.abspath(os.path.dirname(__file__)) + '/jljt.mp4') 	# 读取视频
ret, frame = video.read()	# 读取帧
while ret:	# 逐帧读取
  str_img = ''	# 字符画
  grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)	# 灰度转换
  grey = cv2.resize(grey, (100, 40))	# 该表大小
  for i in grey:	# 遍历每个像素点
    for j in i:
      index = int(j / 256 * len(str))	# 获取字符坐标
      str_img += str[index]	# 将字符添加到字符画中
    str_img += '\n'
  os.system('cls')	# 清除上一帧输出的内容
  print(str_img)	# 输出字符画
  ret, frame = video.read()	# 读取下一帧
  cv2.waitKey(5)

def extractMP3(videofile):
	subprocess.call('ffmpeg -i %s -f mp3 cache.mp3' % videofile, shell=True)
	return True
