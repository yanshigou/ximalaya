# encoding: utf-8
import requests
import re
import sys
import random

sep = '\n'
sep1 = '*'*50 + '\n'
sep2 = '\n' + '*'*50 + '\n\n'

# url = 'https://www.ximalaya.com/youshengshu/4202564/'
Agent = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
         "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
         "Mozilla/5.0 "
         "(Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
         "Mozilla/5.0 "
         "(Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10"
         ]


def randomAgent():
    headers = {'User-Agent': random.choice(Agent)}
    # print(headers)
    return headers


def xima(url):
    headers = randomAgent()
    r = requests.session().get(url, headers=headers)

    fout = open("ximalaya_ID.txt", 'a+', encoding='utf-8')

    # <div class="text rC5T"><a title="《飞翔的秘密》[澳大利亚]伊莎·贾德" href="/youshengshu/4202564/134753995">《飞翔的秘密》[澳大利亚]伊莎·贾德</a></div>
    result = re.findall(r'<div class="text rC5T"><a title=".*?" href="(.*?)">(.*?)</a></div>', r.text, re.S)
    trackIds_list = []
    # print(result)
    for i in result:
        # 每个音频的地址
        second_url = i[0]
        # 每个音频的 title
        # print(second_url, i[1])

        res = re.findall(r'(?<=/)\d+$', i[0], re.S)
        for x in res:
            print(x)

        # break

        # fout.write("%s,%s" % (second_url, i[1]) + sep)
        fout.write("%s, %s" % (x, i[1]) + sep)

    fout.close()


if __name__ == '__main__':
    # url = sys.argv[1]
    xima('https://www.ximalaya.com/youshengshu/4202564/')