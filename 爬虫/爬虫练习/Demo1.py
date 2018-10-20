from urllib import request

if __name__ == "__main__":
    url = 'https://www.bilibili.com/'
    #打开url并将相应的页面代码返回
    rsp = request.urlopen(url)
    #读取返回结果,并解码
    html = rsp.read().decode()
    print(html)



