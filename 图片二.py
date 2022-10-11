import  requests
from bs4 import BeautifulSoup
import time
url = "http://www.netbian.com/"
w = 2
while w < 106:
    main_url = "http://www.netbian.com/dongman/index_{}.htm".format(w)  #组合获得新的网页

    main_resp = requests.get(main_url)
    main_resp.encoding = "gbk"

    main_page = BeautifulSoup(main_resp.text,"html.parser")

    alist = main_page.find('div', class_='list').find_all("a")

    list=[]
    # print(alist)
    for a in alist:

        list.append(a.get("href"))
    while 'http://pic.netbian.com/' in list:
        list.remove('http://pic.netbian.com/')
    for i in range(len(list)):
        new_url = url + list[i]
        new_resp = requests.get(new_url)
        new_resp.encoding = "gbk"
        new_page = BeautifulSoup(new_resp.text,"html.parser")
        alist1 = new_page.find("div",class_="pic").find_all("img")
        # print(alist1)
        for j in alist1:
            src = j.get("src")
        # print(src)
        img_down = requests.get(src)
        img_name = src.split("/")[-1]
        with open("图片/"+img_name,mode = "wb")as f:
            f.write(img_down.content)
        print('over',img_name)
        time.sleep(1)
    w += 1
