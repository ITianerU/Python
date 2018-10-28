from urllib import request,error

if __name__=="__main__":
    url = "http://www.baidu.com"
    #设置代理地址
    proxy = {'http':'123.57.76.102:80'}
    #创建proxy handler
    proxy_handler = request.ProxyHandler(proxy)
    #创建opener
    opener = request.build_opener(proxy_handler)
    #安装opener
    request.install_opener(opener)

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)