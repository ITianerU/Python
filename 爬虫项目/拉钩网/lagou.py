import requests
from bs4 import BeautifulSoup
import json
import time

def main():
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false"
    headers = {
        "Host": "www.lagou.com",
        "Origin": "https://www.lagou.com",
        "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "X-Anit-Forge-Code": "0",
        "X-Anit-Forge-Token": None,
        "X-Requested-With": "XMLHttpRequest"
    }
    page = 1
    for i in range(3):
        data = {
            "first": "true",
            "pn": page,
            "kd": "python"
        }

        rsp = requests.post(url, headers=headers, data=data)
        dict_data = json.loads(rsp.text)
        for work in dict_data["content"]["positionResult"]["result"]:
            print("职位：", work["positionName"])
            print("工作年限:", work["workYear"])
            print("学历:", work["education"])
            print("工作性质:", work["jobNature"])
            print("薪资：", work["salary"])
            print("城市：", work["city"])
            print("公司性质：", work["industryField"])
            print("福利待遇：", work["positionAdvantage"])
            print("公司规模：", work["companySize"])
            print("公司名称：", work["companyFullName"])
            print("详细信息：", getXiangXi(work["positionId"]))
            print("*"*50)
            time.sleep(1)

        page += 1
        time.sleep(20)

def getXiangXi(num):
    url = "https://www.lagou.com/jobs/{}.html".format(num)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "_ga=GA1.2.1951582401.1542034754; user_trace_token=20181112225913-84da7cfe-e68b-11e8-889a-5254005c3644; LGUID=20181112225913-84da8534-e68b-11e8-889a-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167086f817731c-03f566305921e-162a1c0b-2073600-167086f81783af%22%2C%22%24device_id%22%3A%22167086f817731c-03f566305921e-162a1c0b-2073600-167086f81783af%22%7D; hasDeliver=0; index_location_city=%E6%9D%AD%E5%B7%9E; JSESSIONID=ABAAABAAAGFABEFB4CEA03F8D647E755EADCB240CAD039C; _putrc=4E3FA7F45BB0D0D2123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B70660; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; WEBTJ-ID=20181113212755-1670d41cd7bcea-066b0139404a3e-162a1c0b-2073600-1670d41cd7d617; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542034776,1542115673,1542115676,1542116449; gate_login_token=416b347a644c6c3254c199af57927a795290d0cce1f792d3cd1154302dd6eeef; LGSID=20181113225426-03b242bb-e754-11e8-9d9b-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F5219979.html; _gat=1; SEARCH_ID=e768885e358e412ca09a6a419eccf609; TG-TRACK-CODE=search_code; LGRID=20181113232002-97608448-e757-11e8-9d9f-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542122402",
        "Host": "www.lagou.com",
        "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }
    rsp = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(rsp.text, "lxml")
    dl = bs.find("dd", attrs={"class": "job_bt"})
    if dl == None:
        return "无"
    return dl.text








if __name__ == "__main__":
    main()