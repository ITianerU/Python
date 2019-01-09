from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    # 默认提供三个选项
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 字段顺序
    # fields = ['pub-date', 'question_text']
    # 字段布局   'classes': ['collapse']设置字段默认不显示
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    # 将选项字段添加到表单中
    inlines = [ChoiceInline]
    # 设置管理页面列表显示列
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 设置检索字段
    list_filter = ['pub_date']
    # 设置搜索
    search_fields = ['question_text']
    # 设置管理页面标题， 同时修改模板并设置该属性，优先以模板为主
    admin.site.site_header = '问题管理'


admin.site.register(Question, QuestionAdmin)
