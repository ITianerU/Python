from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    #内嵌Meta类，表示根据哪个model创建表单
    class Meta:
        model = Topic
        #表单字段
        fields = ['text']
        #设置字段无标签
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        #默认文本框，widgets覆盖掉默认控件
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}