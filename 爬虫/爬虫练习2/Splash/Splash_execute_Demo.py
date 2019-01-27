
import requests

from urllib.parse import quote

lua = """
    function main(splash)
        return 'hello'
    end
"""

url = "http://localhost:8050/execute?lua_source=" + quote(lua)
rsp = requests.get(url)
print(rsp.text)


lua = """
    function main(splash, args)
        local treat = require("treat")
        local response = splash:http_get("http://httpbin.org/get")
            return {
                html = treat.as_string(response.body),
                url = response.url,
                status = response.status
            }
    end
"""
url = "http://localhost:8050/execute?lua_source=" + quote(lua)
rsp = requests.get(url)
print(rsp.text)