
from pyquery import PyQuery
import requests

html = """
    <div>
        <ul>
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span>third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
"""

result = PyQuery(html)
print(result("li"))

html = requests.get(url="https://www.baidu.com")
html.encoding = "utf-8"
result = PyQuery(html.text)
print(result("title"))
