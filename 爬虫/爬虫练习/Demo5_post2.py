from urllib import request,parse
import json

if __name__ == "__main__":
    while True:
        text = input("请输入想要查询的单词:")
        url = "https://fanyi.baidu.com/sug"

        data = {
            "kw": text
        }
        data = parse.urlencode(data).encode()
        headers = {
            "Content-Length": len(data)
        }

        req = request.Request(url=url, data=data,method="POST")
        rsp = request.urlopen(req)

        json_data = rsp.read().decode("utf-8")
        #将返回的json转换为dict,使用loads不是load
        json_data = json.loads(json_data)
        print(json_data)
        for item in json_data['data']:
          print(item['k'], "--", item['v'])

