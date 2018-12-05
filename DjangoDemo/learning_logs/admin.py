from django.contrib import admin
from learning_logs.models import Topic, Entry

#将创建的模型注册到管理网站
admin.site.register(Topic)
admin.site.register(Entry)
