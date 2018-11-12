import requests
from lxml import etree
import os
import time
from concurrent import futures

if __name__=="__main__":
    url = "http://www.doutula.com/"
    headers = {
        #跨域下载，部分网站会识别从哪个网站进行下载
        "Referer": "http://www.doutula.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }
    rsp = requests.get(url, headers=headers)
    html = etree.HTML(rsp.text)
    #创建线程池
    threads = futures.ThreadPoolExecutor(20)
    #判断该页面是否有下一页按钮
    def get_page(html):
        next_button = html.xpath(".//a[@rel='next']")
        return next_button

    def download_img(srcs, num):
        print("新线程创建**************")
        for i in srcs:
            filename = i.split("/")[-1]
            img = requests.get(url=i, headers=headers)
            with open(("imgs/{}/"+filename).format(num), 'wb') as file:
                #img.content是图片的内容
                file.write(img.content)
            print(filename)
            # print(i)

    url2 = "http://www.doutula.com/article/list/?page={}"
    num = 1
    while True:
        srcs = html.xpath('.//img/@data-original')
        if not os.path.exists('imgs/{}'.format(num)):
            os.mkdir('imgs/{}'.format(num))

        threads.submit(download_img, srcs, num)

        if get_page(html):
            num += 1
            url3 = url2.format(num)
            rsp = requests.get(url3, headers=headers)
            html = etree.HTML(rsp.text)
            if num == 3:
                break
        else:
            break

    print("end")