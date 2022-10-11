import requests
import re
import csv

num = 0

while num < 226:


    url = "https://movie.douban.com/top250?start={}".format(num)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"
    }

    resp = requests.get(url , headers=headers)

    page_content = resp.text

    o = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                   r'</span>.*?<div class="bd">.*?<br>(?P<year>.*?)&nbsp;.*?<span'
                   r' class="rating_num" property="v:average">(?P<grade>.*?)'
                   r'</span>.*?<span>(?P<number>.*?)</span>',re.S)

    result = o.finditer(page_content)

    f = open("Top250.csv",mode="a")

    come = csv.writer(f)

    num += 25

    for i in result:
        # print(i.group("name"))
        # print(i.group("year").strip()+"年")
        # print(i.group("grade")+"分")
        # print(i.group("number"))
        dic = i.groupdict()
        dic['year'] = dic['year'].strip()
        come.writerow(dic.values())


f.close()
print("top250已打印")