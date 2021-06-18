from random import choice
from urllib import request

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/index.html', methods=['GET', 'POST'])
def Index():
    return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def Login():
    return render_template("login.html")


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    return render_template("register.html")


@app.route('/tables.html')
def tables():
    datalist = []
    conn = sqlite3.connect('Web')
    cur = conn.cursor()
    sql = '''
    select * from webchengdu where jobname like '%前端%'
    '''
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template("tables.html", web=datalist)


@app.route('/forms.html')
def forms():
    return render_template("forms.html")


@app.route('/mycharts1.html')
def mycharts1():
    num = []    #存成都
    datalist = []   #存成都
    num1 = []  # 存上海
    datalist1 = []  # 存上海
    num2 = []  # 存北京
    datalist2 = []  # 存北京

    con = sqlite3.connect('Web')
    cur = con.cursor()

    #查询成都
    sql = "select count(providesalarytext) from webchengdu where jobname like '%前端%' and providesalarytext like " \
          "'%6千/月' "
    data = cur.execute(sql)
    for item in data:
        num.append(item)

    sql = "select count(providesalarytext) from webchengdu where jobname like '%前端%' and providesalarytext>0.6 and " \
          "providesalarytext like '%-1万/月' "
    data = cur.execute(sql)
    for item in data:
        num.append(item)

    sql = "select count(providesalarytext) from webchengdu where jobname like '%前端%' and providesalarytext>1 and " \
          "providesalarytext like '%-1.5万/月' "
    data = cur.execute(sql)
    for item in data:
        num.append(item)

    sql = "select count(providesalarytext) from webchengdu where jobname like '%前端%' and providesalarytext>1.5 and " \
          "providesalarytext like '%-2万/月' "
    data = cur.execute(sql)
    for item in data:
        num.append(item)

    sql = "select count(providesalarytext) from webchengdu where jobname like '%前端%' and providesalarytext>2 and " \
          "providesalarytext like '%万/月' "
    data = cur.execute(sql)
    for item in data:
        num.append(item)
    for item in num:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist.append(a)

    #查询上海
    sql = "select count(providesalarytext) from webshanghai where jobname like '%前端%' and providesalarytext like " \
          "'%6千/月' "
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    sql = "select count(providesalarytext) from webshanghai where jobname like '%前端%' and providesalarytext>0.6 and " \
          "providesalarytext like '%-1万/月' "
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    sql = "select count(providesalarytext) from webshanghai where jobname like '%前端%' and providesalarytext>1 and " \
          "providesalarytext like '%-1.5万/月' "
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    sql = "select count(providesalarytext) from webshanghai where jobname like '%前端%' and providesalarytext>1.5 and " \
          "providesalarytext like '%-2万/月' "
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    sql = "select count(providesalarytext) from webshanghai where jobname like '%前端%' and providesalarytext>2 and " \
          "providesalarytext like '%万/月' "
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    for item in num1:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist1.append(a)

    #查询北京
    sql = "select count(providesalarytext) from webbeijing where jobname like '%前端%' and providesalarytext like " \
          "'%6千/月' "
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    sql = "select count(providesalarytext) from webbeijing where jobname like '%前端%' and providesalarytext>0.6 and " \
          "providesalarytext like '%-1万/月' "
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    sql = "select count(providesalarytext) from webbeijing where jobname like '%前端%' and providesalarytext>1 and " \
          "providesalarytext like '%-1.5万/月' "
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    sql = "select count(providesalarytext) from webbeijing where jobname like '%前端%' and providesalarytext>1.5 and " \
          "providesalarytext like '%-2万/月' "
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    sql = "select count(providesalarytext) from webbeijing where jobname like '%前端%' and providesalarytext>2 and " \
          "providesalarytext like '%万/月' "
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    for item in num2:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist2.append(a)
    cur.close()
    con.close()

    return render_template('mycharts1.html', datalist=datalist, datalist1=datalist1, datalist2=datalist2)

@app.route('/mycharts2.html')
def mycharts2():
    num = []    #存成都
    datalist = []   #存成都
    num1 = []  # 存上海
    datalist1 = []  # 存上海
    num2 = []  # 存北京
    datalist2 = []  # 存北京

    con = sqlite3.connect('Web')
    cur = con.cursor()

    #查询成都
    sql = "select count(providesalarytext) from webchengdu where jobname like '%前端%' and providesalarytext like " \
          "'%6千/月' "
    data = cur.execute(sql)
    for item in data:
        num.append(item)

    sql = "select count(providesalarytext) from webchengdu where jobname like '%前端%' and providesalarytext>0.6 and " \
          "providesalarytext like '%-1万/月' "
    data = cur.execute(sql)
    for item in data:
        num.append(item)

    sql = "select count(providesalarytext) from webchengdu where jobname like '%前端%' and providesalarytext>1 and " \
          "providesalarytext like '%-1.5万/月' "
    data = cur.execute(sql)
    for item in data:
        num.append(item)

    sql = "select count(providesalarytext) from webchengdu where jobname like '%前端%' and providesalarytext>1.5 and " \
          "providesalarytext like '%-2万/月' "
    data = cur.execute(sql)
    for item in data:
        num.append(item)

    sql = "select count(providesalarytext) from webchengdu where jobname like '%前端%' and providesalarytext>2 and " \
          "providesalarytext like '%万/月' "
    data = cur.execute(sql)
    for item in data:
        num.append(item)
    for item in num:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist.append(a)

    #查询上海
    sql = "select count(providesalarytext) from webshanghai where jobname like '%前端%' and providesalarytext like " \
          "'%6千/月' "
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    sql = "select count(providesalarytext) from webshanghai where jobname like '%前端%' and providesalarytext>0.6 and " \
          "providesalarytext like '%-1万/月' "
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    sql = "select count(providesalarytext) from webshanghai where jobname like '%前端%' and providesalarytext>1 and " \
          "providesalarytext like '%-1.5万/月' "
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    sql = "select count(providesalarytext) from webshanghai where jobname like '%前端%' and providesalarytext>1.5 and " \
          "providesalarytext like '%-2万/月' "
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    sql = "select count(providesalarytext) from webshanghai where jobname like '%前端%' and providesalarytext>2 and " \
          "providesalarytext like '%万/月' "
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    for item in num1:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist1.append(a)

    #查询北京
    sql = "select count(providesalarytext) from webbeijing where jobname like '%前端%' and providesalarytext like " \
          "'%6千/月' "
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    sql = "select count(providesalarytext) from webbeijing where jobname like '%前端%' and providesalarytext>0.6 and " \
          "providesalarytext like '%-1万/月' "
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    sql = "select count(providesalarytext) from webbeijing where jobname like '%前端%' and providesalarytext>1 and " \
          "providesalarytext like '%-1.5万/月' "
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    sql = "select count(providesalarytext) from webbeijing where jobname like '%前端%' and providesalarytext>1.5 and " \
          "providesalarytext like '%-2万/月' "
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    sql = "select count(providesalarytext) from webbeijing where jobname like '%前端%' and providesalarytext>2 and " \
          "providesalarytext like '%万/月' "
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    for item in num2:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist2.append(a)
    cur.close()
    con.close()

    return render_template('mycharts2.html', datalist=datalist, datalist1=datalist1, datalist2=datalist2)

@app.route('/mycharts3.html')
def mycharts3():
    return render_template('mycharts3.html')

@app.route('/mycharts4.html')
def mycharts4():
    num1 = []  # 存“五险一金”
    datalist1 = []
    num2 = []  # 存“年终奖金”
    datalist2 = []
    num3 = []  # 存“周末双休”
    datalist3 = []
    num4 = []  # 存“生活补贴”
    datalist4 = []
    num5 = []  # 存“定期体检”
    datalist5 = []

    con = sqlite3.connect('Web')
    cur = con.cursor()

    # 查询"五险一金"
    sql = "select count(jobwelf) from webchengdu where jobwelf like '%五险一金%'"
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    sql = "select count(jobwelf) from webshanghai where jobwelf like '%五险一金%'"
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    sql = "select count(jobwelf) from webbeijing where jobwelf like '%五险一金%'"
    data = cur.execute(sql)
    for item in data:
        num1.append(item)

    for item in num1:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist1.append(a)

    # 查询"年终奖金"
    sql = "select count(jobwelf) from webchengdu where jobwelf like '%年终奖金%'"
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    sql = "select count(jobwelf) from webshanghai where jobwelf like '%年终奖金%'"
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    sql = "select count(jobwelf) from webbeijing where jobwelf like '%年终奖金%'"
    data = cur.execute(sql)
    for item in data:
        num2.append(item)

    for item in num2:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist2.append(a)

    # 查询"周末双休"
    sql = "select count(jobwelf) from webchengdu where jobwelf like '%周末双休%' or '做五休二'"
    data = cur.execute(sql)
    for item in data:
        num3.append(item)

    sql = "select count(jobwelf) from webshanghai where jobwelf like '%周末双休%' or '做五休二'"
    data = cur.execute(sql)
    for item in data:
        num3.append(item)

    sql = "select count(jobwelf) from webbeijing where jobwelf like '%周末双休%' or '做五休二'"
    data = cur.execute(sql)
    for item in data:
        num3.append(item)

    for item in num3:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist3.append(a)

    # 查询"年终奖金"
    sql = "select count(jobwelf) from webchengdu where jobwelf like '%年终奖金%'"
    data = cur.execute(sql)
    for item in data:
        num4.append(item)

    sql = "select count(jobwelf) from webshanghai where jobwelf like '%年终奖金%'"
    data = cur.execute(sql)
    for item in data:
        num4.append(item)

    sql = "select count(jobwelf) from webbeijing where jobwelf like '%年终奖金%'"
    data = cur.execute(sql)
    for item in data:
        num4.append(item)

    for item in num4:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist4.append(a)

    # 查询"生活补贴"
    sql = "select count(jobwelf) from webchengdu where jobwelf like '%补贴%'"
    data = cur.execute(sql)
    for item in data:
        num4.append(item)

    sql = "select count(jobwelf) from webshanghai where jobwelf like '%补贴%'"
    data = cur.execute(sql)
    for item in data:
        num4.append(item)

    sql = "select count(jobwelf) from webbeijing where jobwelf like '%补贴%'"
    data = cur.execute(sql)
    for item in data:
        num4.append(item)

    for item in num4:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist4.append(a)

    # 查询"定期体检"
    sql = "select count(jobwelf) from webchengdu where jobwelf like '%定期体检%'"
    data = cur.execute(sql)
    for item in data:
        num5.append(item)

    sql = "select count(jobwelf) from webshanghai where jobwelf like '%定期体检%'"
    data = cur.execute(sql)
    for item in data:
        num5.append(item)

    sql = "select count(jobwelf) from webbeijing where jobwelf like '%定期体检%'"
    data = cur.execute(sql)
    for item in data:
        num5.append(item)

    for item in num5:
        item1 = str(item)
        item1 = item1.replace('(', "").replace(')', "").replace(",", "")
        a = int(item1)
        datalist5.append(a)
    cur.close()
    con.close()

    return render_template("mycharts4.html", datalist1=datalist1, datalist2=datalist2, datalist3=datalist3, datalist4=datalist4, datalist5=datalist5)

@app.route('/result', methods=['GET', 'POST'])
def result():  # 注册函数
    account_1 = request.form.get('registerUsername')
    mail_1 = request.form.get('registerEmail')
    print(account_1, mail_1)
    password_1 = request.form.get('registerPassword')
    conn = sqlite3.connect("identifier.sqlite")
    c = conn.cursor()
    sql = '''insert into Users(account,mailbox,password)values( '%s','%s','%s' ) ;''' % (account_1, mail_1, password_1)
    c.execute(sql)  # 执行sql语句
    conn.commit()  # 提交sql语句
    conn.close()  # 关闭数据库连接
    # win32api.MessageBox(0, "注册成功！", "提醒", win32con.MB_ICONASTERISK)
    return render_template("Login.html")


@app.route('/result_1', methods=['GET', 'POST'])
def result1():  # 登录函数
    account_2 = request.form.get('loginUsername')
    password_2 = request.form.get('loginPassword')
    print(account_2, password_2)
    conn = sqlite3.connect("identifier.sqlite")
    c = conn.cursor()
    sql = '''
    select * from Users
    '''
    data = c.execute(sql)
    for item in data:
        if (item[0] == account_2 and item[2] == password_2):
            return render_template("index.html")
        else:
            continue
    # win32api.MessageBox(0, "账号或密码输入错误！", "提醒", win32con.MB_ICONASTERISK)
    return render_template("login.html")


@app.route('/result_2', methods=['GET', 'POST'])  # 修改密码函数
def result2():
    account_3 = request.form.get('account_1')  # 账户
    password_3 = request.form.get('password')  # 原密码
    password_4 = request.form.get('newPassword')  # 现密码
    print(account_3, password_3, password_4)
    conn = sqlite3.connect("identifier.sqlite")
    c = conn.cursor()
    sql = '''
    select * from Users
    '''
    data = c.execute(sql)
    for item in data:
        if (item[0] == account_3 and item[2] == password_3):
            sql_1 = '''update Users set password = %s where account = %s ''' % (password_4, account_3)
            c.execute(sql_1)
            conn.commit()  # 提交sql语句
            conn.close()  # 关闭数据库连接
            return render_template("login.html")
        else:
            continue
    return render_template("cw.html")


@app.route('/jsondatachengdu', methods=['POST', 'GET'])
def infoschengdu():
    global limit, offset
    datalist = []
    conn = sqlite3.connect('Web')
    cur = conn.cursor()
    sql = '''
        select * from  webchengdu
        '''
    data1 = cur.execute(sql)
    for item in data1:
        a = {}
        a['id'] = item[0]
        a['jobname'] = item[1]
        a['companyname'] = item[3]
        a['salary'] = item[4]
        a['jobwelf'] = item[5]
        a['workrequest'] = item[6]
        a['workplace'] = item[7]
        a['workminimumDegree'] = item[8]
        a['workrecruiternum'] = item[9]
        datalist.append(a)
    cur.close()
    conn.close()
    """
     请求的数据源，该函数模拟数据库中存储的数据，返回以下这种数据的列表：
    {'name': '香蕉', 'id': 1, 'price': '10'}
    {'name': '苹果', 'id': 2, 'price': '10'}
    """
    if request.method == 'POST':
        print('post')
    if request.method == 'GET':
        info = request.values
        limit = info.get('limit', 10)  # 每页显示的条数
        offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点
        print('get', limit)
    print('get  offset', offset)
    return jsonify({'total': len(datalist), 'rows': datalist[int(offset):(int(offset) + int(limit))]})
    # 注意total与rows是必须的两个参数，名字不能写错，total是数据的总长度，rows是每页要显示的数据,它是一个列表
    # 前端根本不需要指定total和rows这俩参数，他们已经封装在了bootstrap table里了


@app.route('/cw.html', methods=['GET', 'POST'])
def cw():
    return render_template("cw.html")


@app.route('/jsondatabeijing', methods=['POST', 'GET'])
def infosbeijing():
    global limit, offset
    datalist = []
    conn = sqlite3.connect('Web')
    cur = conn.cursor()
    sql = '''
        select * from webbeijing
        '''
    data1 = cur.execute(sql)
    for item in data1:
        a = {}
        a['id'] = item[0]
        a['jobname'] = item[1]
        a['companyname'] = item[3]
        a['salary'] = item[4]
        a['jobwelf'] = item[5]
        a['workrequest'] = item[6]
        a['workplace'] = item[7]
        a['workminimumDegree'] = item[8]
        a['workrecruiternum'] = item[9]
        datalist.append(a)
    cur.close()
    conn.close()
    """
     请求的数据源，该函数模拟数据库中存储的数据，返回以下这种数据的列表：
    {'name': '香蕉', 'id': 1, 'price': '10'}
    {'name': '苹果', 'id': 2, 'price': '10'}
    """
    if request.method == 'POST':
        print('post')
    if request.method == 'GET':
        info = request.values
        limit = info.get('limit', 10)  # 每页显示的条数
        offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点
        print('get', limit)
    print('get  offset', offset)
    return jsonify({'total': len(datalist), 'rows': datalist[int(offset):(int(offset) + int(limit))]})
    # 注意total与rows是必须的两个参数，名字不能写错，total是数据的总长度，rows是每页要显示的数据,它是一个列表
    # 前端根本不需要指定total和rows这俩参数，他们已经封装在了bootstrap table里了


@app.route('/jsondatashanghai', methods=['POST', 'GET'])
def infosshanghai():
    global limit, offset
    datalist = []
    conn = sqlite3.connect('Web')
    cur = conn.cursor()
    sql = '''
        select * from webshanghai
        '''
    data1 = cur.execute(sql)
    for item in data1:
        a = {}
        a['id'] = item[0]
        a['jobname'] = item[1]
        a['companyname'] = item[3]
        a['salary'] = item[4]
        a['jobwelf'] = item[5]
        a['workrequest'] = item[6]
        a['workplace'] = item[7]
        a['workminimumDegree'] = item[8]
        a['workrecruiternum'] = item[9]
        datalist.append(a)
    cur.close()
    conn.close()
    """
     请求的数据源，该函数模拟数据库中存储的数据，返回以下这种数据的列表：
    {'name': '香蕉', 'id': 1, 'price': '10'}
    {'name': '苹果', 'id': 2, 'price': '10'}
    """
    if request.method == 'POST':
        print('post')
    if request.method == 'GET':
        info = request.values
        limit = info.get('limit', 10)  # 每页显示的条数
        offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点
        print('get', limit)
    print('get  offset', offset)
    return jsonify({'total': len(datalist), 'rows': datalist[int(offset):(int(offset) + int(limit))]})
    # 注意total与rows是必须的两个参数，名字不能写错，total是数据的总长度，rows是每页要显示的数据,它是一个列表
    # 前端根本不需要指定total和rows这俩参数，他们已经封装在了bootstrap table里了


@app.route('/chengdu.html')
def chengdu():
    return render_template('chengdu.html')


@app.route('/beijing.html')
def beijing():
    return render_template('beijing.html')


@app.route('/shanghai.html')
def shanghai():
    return render_template('shanghai.html')

@app.route('/mycharts5.html')
def mycharts5():
    num = []
    conn = sqlite3.connect('Web')
    cur = conn.cursor()
    sql = '''
    select place,sum(number) from count group by place
    '''
    data = cur.execute(sql)
    for item in data:
        a = {'name':item[0],"value":item[1]}
        num.append(a)
    print(num)
    cur.close()
    conn.close()
    return render_template('mycharts5.html', data=num)



if __name__ == '__main__':
    app.run(debug=True)
