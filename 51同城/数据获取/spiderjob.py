import json

import re  # 正则表达式，进行文字匹配
import sqlite3
import urllib.request  # 制定url，获取网页数据
import ssl

from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    Dbpath = 'Web'
    getData(Dbpath)
    # saveDb(Dbpath)


def askUrl(url):
    headers = {
        "User-Agent": "Mozilla / 5.0(Macintosh; Intel Mac OS X 10_15_6) AppleWebKit / 605.1 .15(KHTML, like Gecko) Version / 14.0 .3 Safari / 605.1 .15 }"
    }
    html = ''
    try:
        req = urllib.request.Request(url=url, headers=headers, method='GET')
        response = urllib.request.urlopen(req)
        html = response.read().decode('gbk')
    except Exception as e:
        if hasattr(e, "code"):
            print(e)
        if hasattr(e, "reason"):
            print(e)
    return html


def getData(Dbpath):
    #init_DB(Dbpath)
    data = []
    sql = '''
    select jobhref from webchengdu where jobname like '%前端%'
    '''
    conn = sqlite3.connect(Dbpath)
    cur = conn.cursor()
    cur1 = conn.cursor()
    href = cur.execute(sql)
    for item in href:
        baseurl = "".join(item)
        url = baseurl
        html = askUrl(url)
        soup = BeautifulSoup(html, "html.parser")
        for a in soup.find_all('div', class_='bmsg job_msg inbox'):
            text = a.text
            s = text.replace("微信", "").replace("分享", "").replace("邮件", "").replace(
                "\t", "").replace("\n", "").replace('\xa0', " ").strip()
            data.append(s)
            sql1 = '''
               insert into requirements(jobrequirements)values('%s')
               ''' % (s)
            cur1.execute(sql1)
            conn.commit()



    # for item in data:
    #     print(item)
    cur.close()
    conn.close()
    return data


def init_DB(Dbpath):
    sql = '''
    create table requirements(
    id integer primary key autoincrement,
    jobrequirements text
    )
    '''
    conn = sqlite3.connect(Dbpath)
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.close()


def saveDb(Dbpath):
    conn = sqlite3.connect(Dbpath)
    cur = conn.cursor()
    # init_DB(Dbpath)
    item = getData()
    for text in item:
        sql = '''
    insert into requirements(jobrequirements)values("%s")
    ''' % (text[0])
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
