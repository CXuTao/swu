from django.shortcuts import render, HttpResponse
from django.http import FileResponse
import os
from django.conf import settings
from django.utils.encoding import escape_uri_path
import cv2

# Create your views here.
def upfile(request):
    return render(request, 'teaching_system/upfile.html')

def savefile(request):
	if request.method == 'POST':
		# 获取资源类型（获取value值）
		resource_type = request.POST.get('resource_type')
		print(resource_type)
		#合成文件夹路径
		if resource_type is not None:
			fileDir = os.path.join(settings.MEDIA_ROOT, resource_type)
			# 取文件
			f = request.FILES['file']
			# 合成文件在服务器端的路径
			filePath = os.path.join(fileDir, f.name)
			with open(filePath, 'wb') as fp:
				for info in f.chunks():
					# f.chunks()文件分块接收
					fp.write(info)
			return HttpResponse('上传成功')
		else:
			return HttpResponse('请选择上传类型')
	else:
		return HttpResponse('上传失败')


def download(request):
	file = open('static/upfile/image/游戏安装教程.png', 'rb')
	the_file_name = file.name
	print(the_file_name)
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename*=utf-8''{}'.format(escape_uri_path(the_file_name))
	return response


def video(request):
	# 0表示使用电脑摄像头
	cap = cv2.VideoCapture(0)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

	while (cap.isOpened()):
		ret, frame = cap.read()
		if ret == True:
			# 视频翻转
			# 1	水平翻转
			# 0	垂直翻转
			# -1	水平垂直翻转
			frame = cv2.flip(frame, 0)

			out.write(frame)
			cv2.imshow('frame', frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			break
	cap.release()
	out.release()
	cv2.destroyAllWindows()