from urllib import request

if __name__=="__main__":
    url = 'http://space.bilibili.com/6765452/#/'
    headers={
        'Cookie': '填写cookie'
    }
    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    with open("bilibili.html","w") as f:
        f.write(html)