"""
salt : "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
sign: n.md5("fanyideskweb" + e + salt + "6x(ZHw]mwzX#u0V7@yfwK")
"""

from urllib import request,parse
import time,random,hashlib
#获取salt
def getSalt():
    salt = int(time.time()*1000) + random.randint(0,10)
    return salt


#获取sign
def getSign(t,salt):

    sign = 'fanyideskweb' + t + str(salt) + '6x(ZHw]mwzX#u0V7@yfwK'

    md5 = hashlib.md5()

    md5.update(sign.encode())

    return md5.hexdigest()

def youdao(t):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    salt = getSalt()
    sign = getSign(t,salt)
    data = {
        "i": t,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }

    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        #"Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1548144101@10.168.8.76;JSESSIONID=aaaTLWzfvp5Hfg9mAhFkw;OUTFOX_SEARCH_USER_ID_NCOO=1999296830.4784973;___rl__test__cookies=1523100789517",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0( X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36 X-Requested-With: XMLHttpRequest"
    }

    req = request.Request(url,data=data,headers=headers)
    rsp = request.urlopen(req)
    print(rsp.read().decode())

if __name__ == "__main__":
    youdao("girl")

