from urllib import request

if __name__ == "__main__":
    url = "http://baidu.com"
    # headers={}
    # headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
    req = request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36")
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)