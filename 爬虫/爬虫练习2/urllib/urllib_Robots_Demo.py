
from urllib.robotparser import RobotFileParser
from urllib import request

# 判断该url是否被允许爬取
rp = RobotFileParser()
rp.set_url('https://www.douban.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'https://movie.douban.com/chart'))
print(rp.can_fetch('*', 'https://movie.douban.com/subject_search?search_text=234&cat=1002'))

rp2 = RobotFileParser()
rp2.parse(request.urlopen('https://www.douban.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp2.can_fetch('*', 'https://movie.douban.com/chart'))
print(rp2.can_fetch('*', 'https://movie.douban.com/subject_search?search_text=234&cat=1002'))
