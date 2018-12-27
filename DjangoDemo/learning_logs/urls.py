"""
    定义learning_logs的url模式
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #匹配首页
    url(r'^$', views.index, name='index'),
    #匹配所有主题
    url(r'^topics$', views.topics, name='topics'),
    #匹配主题详情
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #匹配新建主题页面
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #匹配新建条目页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #匹配编辑条目页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
