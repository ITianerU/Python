from django.db import models

class Topic(models.Model):
    """
        用户学习主题
    """
    text = models.CharField(max_length=200)
    #自动添加创建时间
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """
        主题的具体内容
    """
    #on_delete=models.CASCADE 设置级联删除，可让删除主数据时子数据也一起删除
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    #管理员模型管理页面显示的菜单名称，如果不设置，默认显示模型名首字母大写加s
    class Meta:
        verbose_name_plural = 'entries'

    #管理员模型管理页面显示添加的数据内容，不设置默认展示模型名+object
    def __str__(self):
        if len(self.text)>30:
            return self.text[:30] + "..."
        return self.text