import sqlite3


def main():
    init_dB();
    saveinDb();


def init_dB():
    sql = '''
         create table count(
         id integer primary key autoincrement,
         place character(20),
         number character(20)
            )
            '''  # 创建数据表
    conn = sqlite3.connect("../Web")
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()


def saveinDb():
    num = []
    conn = sqlite3.connect('../Web')
    cur = conn.cursor()
    cur1 = conn.cursor()
    sql = '''
        select workplace,count(workplace) from webconutry where workplace not like '%异地%' group by  workplace
        '''
    data = cur.execute(sql)

    for item in data:
        datalist = []
        place = item[0]
        place = str(place)
        place = place[:2]
        datalist.append(place)
        datalist.append(item[1])
        num.append(datalist)
    for item in num:
        sql1 = '''
        insert into count(place,number)values("%s","%s")
        ''' % (item[0], item[1])
        cur1.execute(sql1)
        conn.commit()
    cur.close()
    cur1.close()
    conn.close()

if __name__ == '__main__':
    main();
