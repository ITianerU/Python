from django.shortcuts import render
from django.http import  HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required

def index(request):
    """学习笔记的主页"""
    #会自动在templates中寻找模板，所以模板路径不需要templates
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    #让用户只获取到自己的数据
    topics = Topic.objects.filter(owner=request.user).order_by('date_add')
    #topics = Topic.objects.order_by('date_add')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """
        现实单个主题所有数据
        -date_addedb表示添加日期降序排列
    :param request:
    :param topic_id:
    :return:
    """
    topic = Topic.objects.get(id=topic_id)
    #确认请求的主题是否属于当前用户
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """
    添加新主题
    :param request:
    :return:
    """
    #判断请求类型，不是post则返回空表单
    if request.method != "POST":
        #创建空表单
        form = TopicForm()
    else:
        #将用户输入的数据存到表单中
        form = TopicForm(request.POST)
        #校验数据是否有效
        if form.is_valid():
            #将数据存到数据库
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            #form.save()
            #对页面进行重定向，reverse指定重定向的url
            return HttpResponseRedirect(reverse('learning_logs:topic'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """
    在指定主题中添加新条目
    :param request:
    :return:
    """
    #从特定的主题中添加新条目
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """
    编辑条目
    :param request:
    :return:
    """
    #取出条目数据
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #使用当前数据填充表单
        form = EntryForm(instance=entry)
    else:
        #覆盖掉默认加载的已有数据
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)