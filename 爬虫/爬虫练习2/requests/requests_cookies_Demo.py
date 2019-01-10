
import requests

r = requests.get("https://www.baidu.com")
print(r.cookies)
for k, v in r.cookies.items():
    print(k + '=>' + v)

headers = {
    'cookies': '_zap=d364ccbf-0714-4289-b8fd-defb2325fecf; d_c0="ALAi8HFtkg6PTsulhdFmAbaN1gJd0rCmXjs=|1543124753"; '
               'q_c1=3406cf760704469e8a7facc9de975d13|1543124754000|1543124754000; '
               'z_c0="2|1:0|10:1543135470|4:z_c0|92'
               ':Mi4xbF92b0F3QUFBQUFBc0NMd2NXMlNEaVlBQUFCZ0FsVk43cTduWEFBbi0wLVRNS2l1ZTlObG1tZVViSlpjc2tONFVB'
               '|032df540daf08390fbf1c30a6b08cc0c4e0e78a456fef4cfb84933e7ba94d7c4"; '
               'tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d; _xsrf=bo8Uk9mNvFYyiFcoZrPh8Iv37LPhuBlR; '
               '__gads=ID=4542841cf6fb2d1f:T=1547131888:S=ALNI_MYS8zNrw_ZwNFzRWgxVevVqrxVUtw ',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 '
                  'Safari/537.36x-requested-with: Fetch '
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)

