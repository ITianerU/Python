"""
    定义users的url模式
"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    #登录页
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    #注销
    url(r'^logout/$', views.logout_view, name='logout'),
    #注册
    url(r'^register/$', views.register, name='register'),
]
