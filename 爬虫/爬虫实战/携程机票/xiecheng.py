"""
爬取携程机票数据
"""
import requests
import json

def download(start_code, end_code, date):
    """
    下载器
    :param start_code:
    :param end_code:
    :param date:
    :return:
    """

    url = "https://flights.ctrip.com/international/search/api/search/batchSearch"
    headers = {
        "authority": "flights.ctrip.com",
        "method": "POST",
        "path": "/international/search/api/search/batchSearch?v=0.42273149253414455",
        "scheme": "https",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q = 0.9",
        "cache-control": "no-cache",
        "content-length": "823",
        "Content-Type": "application/json;charset=UTF-8",
        "cookie": 'DomesticUserHostCity=HGH|%ba%bc%d6%dd; _abtest_userid=5eeda2e5-7fd8-41bc-8c1a-191e59c76b66; _RSG=8ta.4xSXek1_6eQ298XZjB; '
                  '_RDG=2874e8301b303f27ed2b1f64355b8d4f98; _RGUID=1ba885ce-c4fa-4dc8-bb63-8482426a81bf; _ga=GA1.2.1229655091.1552547610; '
                  'MKT_Pagesource=PC; gad_city=78a2062d1790b42fa1a75f591a7869b2; Session=SmartLinkCode=U155947&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; '
                  '_RF1=58.100.14.51; Union=OUID=cuoP&AllianceID=4897&SID=155947&SourceID=&Expires=1553655238526; MKT_OrderClick=ASID=4897155947&CT=1553050438529&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155947%26allianceid%3D4897%26ouid%3DcuoP%26gclid%3DCLfN1Nvbj-ECFYFLvAodTEIOGw%26gclsrc%3Dds&VAL={"pc_vid":"1552547606872.2400i"}; _gid=GA1.2.944836021.1553050439; _gcl_dc=GCL.1553050439.CLfN1Nvbj-ECFYFLvAodTEIOGw; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1553050923912%7D%5D; '
                  '__zpspc=9.2.1553050438.1553050923.2%232%7Cwww.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _jzqco=%7C%7C%7C%7C1553050924347%7C1.1488530110.1552547609733.1553050438661.1553050923943.1553050438661.1553050923943.undefined.0.0.3.3; _bfi=p1%3D10320672927%26p2%3D100101991%26v1%3D5%26v2%3D4; FlightIntl=Search=[%22BJS|%E5%8C%97%E4%BA%AC(BJS)|1|BJS|480%22%2C%22TYO|%E4%B8%9C%E4%BA%AC(TYO)|228|TYO|540%22%2C%222019-04-01%22]; _bfa=1.1552547606872.2400i.1.1553050435565.1553053611362.3.6; _bfs=1.1',
        "origin": "https://flights.ctrip.com",
        "referer": "https://flights.ctrip.com/international/search/oneway-bjs-tyo?depdate=2019-04-01&cabin=y_s&adult=1&child=0&infant=0&directflight=&airline=all",
        "sign": "4ac7561164f2f37b9ad87c0ce4f86768",
        #"sign": "4edbf570d55f04ff230b5d9666c4380f",
        "transactionid": "a9eb0f04a50a4f80bd78fa42975db67f",
        #"transactionid": "056762a5295c4211b08d8fb7034b1bee",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    }
    request_payload = {
        "adultCount": 1,
        "arrivalCityId": 228,
        "arrivalCountryName": "日本",
        "arrivalProvinceId": 11079,
        "cabin": "Y_S",
        "cabinEnum": "Y_S",
        "childCount": 0,
        "departCountryName": "中国",
        "departProvinceId": 1,
        "departureCityId": 1,
        "directFlight": False,
        "extensionAttributes": {},
        "flightSegments": [{
            "arrivalCityCode": end_code,
            "arrivalCityId": 228,
            "arrivalCityName": "东京",
            "arrivalCityTimeZone": 540,
            "arrivalCountryId": 78,
            "arrivalCountryName": "日本",
            "arrivalProvinceId": 11079,
            "departureCityCode": start_code,
            "departureCityId": 1,
            "departureCityName": "北京",
            "departureCityTimeZone": 480,
            "departureCountryId": 1,
            "departureCountryName": "中国",
            "departureDate": date,
            "departureProvinceId": 1,
            "timeZone": 480,
        }],
        "flightWay": "S",
        "flightWayEnum": "OW",
        "infantCount": 0,
        "isMultiplePassengerType": 0,
        "segmentNo": 1,
        "transactionID": "a9eb0f04a50a4f80bd78fa42975db67f",
    }
    # request_payload = {
    #     "adultCount": 1,
    #     "arrivalCityId": 274,
    #     "arrivalCountryName": "韩国",
    #     "arrivalProvinceId": 0,
    #     "cabin": "Y_S",
    #     "cabinEnum": "Y_S",
    #     "childCount": 0,
    #     "departCountryName": "中国",
    #     "departProvinceId": 1,
    #     "departureCityId": 1,
    #     "directFlight": False,
    #     "extensionAttributes": {},
    #     "flightSegments": [{
    #         "arrivalCityCode": end_code,
    #         "arrivalCityId": 274,
    #         "arrivalCityName": "首尔",
    #         "arrivalCityTimeZone": 540,
    #         "arrivalCountryId": 42,
    #         "arrivalCountryName": "韩国",
    #         "arrivalProvinceId": 0,
    #         "departureCityCode": start_code,
    #         "departureCityId": 1,
    #         "departureCityName": "北京",
    #         "departureCityTimeZone": 480,
    #         "departureCountryId": 1,
    #         "departureCountryName": "中国",
    #         "departureDate": date,
    #         "departureProvinceId": 1,
    #         "timeZone": 480,
    #     }],
    #     "flightWay": "S",
    #     "flightWayEnum": "OW",
    #     "infantCount": 0,
    #     "isMultiplePassengerType": 0,
    #     "segmentNo": 1,
    #     "transactionID": "056762a5295c4211b08d8fb7034b1bee",
    # }
    rsp = requests.post(url, headers=headers, data=json.dumps(request_payload)).text
    parse(rsp)

def parse(rsp):
    """
    解析json
    :param rsp:
    :return:
    """
    rsp = json.loads(rsp)
    list = rsp.get("data").get("flightItineraryList")
    airdict = {"北京-东京": []}
    for i in list:
        j = i["flightSegments"][0]["flightList"][0]
        l = [j["marketAirlineName"], j["flightNo"], j["aircraftName"],
            j["departureDateTime"] + "(" + j["departureAirportName"] + j["departureTerminal"] + ")----"+j["arrivalDateTime"] + "(" + j["arrivalAirportName"] + j["arrivalTerminal"] + ")"]

        print(l)
        for m in i["priceList"]:
            if m["cabin"] == "Y":
                price = "经济舱票价", str(m["adultPrice"]+m["adultTax"])+"元"
                l.append(price)
                print(price, end=" ")
            elif m["cabin"] == "S":
                price = "超级经济舱票价", str(m["adultPrice"] + m["adultTax"]) + "元"
                l.append(price)
                print(price, end=" ")
        print()
        airdict["北京-东京"].append(l)

    with open("航班信息.json", 'a', encoding="utf8") as file:
        file.write(str(airdict))

if __name__ == '__main__':
    #start_location = input("请输入出发地点:")
    # start_code = input("请输入出发地点机场三位代码:")
    # #end_location = input("请输入到达地点:")
    # end_code = input("请输入到达地点机场三位代码:")
    # date = input("请输入日期")
    #download("BJS", "TYO", "2019-04-01")
    download("BJS", "TYO", "2019-04-01")
