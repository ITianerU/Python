from urllib import parse,request

if __name__ == "__main__":
    wd = input("请输入要查询的内容:")
    qs = {
        "wd" : wd
    }
    url = "http://www.baidu.com/s?" + parse.urlencode(qs)
    print(url)
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)