from django.urls import path, re_path, include
from . import views

app_name = 'teaching_system'
urlpatterns = [
    re_path(r'^upfile/$', views.upfile, name='upfile'),
    re_path(r'^savefile/$', views.savefile, name='savefile'),
    re_path(r'^download/$', views.download, name='download'),
    re_path(r'^video/$', views.video, name='video'),
]