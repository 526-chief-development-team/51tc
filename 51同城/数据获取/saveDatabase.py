import xlwt  # 进行Excel操作
import sqlite3  # 进行SQLite数据库操
from spider import askUrl, getData
from urllib import parse
from spider import id


def main():
    Cityname = input("请输入查询的一个城市：")
    Cityid = id[Cityname]
    job = input('请输入一个您想查询的职业：')
    keyword = parse.quote(job)
    newKw = parse.quote(keyword)
    saveDapath = 'Web'
    saveDB(saveDapath,Cityid,newKw)


def init_DB(saveDBpath):
    sql = '''
     create table  webshanghai(
     id integer primary key autoincrement,
     jobname varchar,
     companyhref text,
     companyname varchar,
     providesalarytext text,
     jobwelf text,
     workrequest varchar,
     workplace varchar ,
     workminimumDegree varchar,
     workrecruiternum text,
     jobhref text
        )
        '''  # 创建数据表
    conn = sqlite3.connect(saveDBpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()


def saveDB(saveDBpath,Cityid,newKw):
    datalist = getData(Cityid,newKw)
    init_DB(saveDBpath)
    conn = sqlite3.connect(saveDBpath)
    cur = conn.cursor()
    for item in datalist:
        sql = '''
        insert into webshanghai(
        jobname,companyhref,companyname,providesalarytext,jobwelf,workrequest,workplace,workminimumDegree,workrecruiternum,jobhref)
        values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")''' % (
        item[0], item[1], item[2], item[3], item[4], item[6], item[5], item[7], item[8], item[9])
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
