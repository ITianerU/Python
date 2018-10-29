from urllib import request
import ssl

if __name__ == "__main__":
    #使用非认证上下文环境替换认证上下文环境
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://www.12306.cn"
    req = request.Request(url)
    rsp = request.urlopen(req)
    print(rsp.read().decode())
