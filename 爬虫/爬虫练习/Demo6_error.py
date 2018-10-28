from urllib import request,error

if __name__ == "__main__":
    try:
        #url = "http://qwebaidu.com"
        url = "https://www.bilibili.com/qwe"
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e.reason)
        print(e)
    except error.URLError as e:
        print(e.reason)
        print(e)
    except Exception as e:
        print(e)
