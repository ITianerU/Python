from urllib import request
import chardet

if __name__ == "__main__":
    rsp = request.urlopen("https://www.bilibili.com/")
    html = rsp.read()
    #读取页面字符集信息,返回字典
    cs = chardet.detect(html)
    print(cs)
    html = html.decode(cs.get("encoding","utf-8"))
    print(html)