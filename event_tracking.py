#encoding:utf-8
from flask import Flask, render_template
from flask import redirect, url_for, request
import json
from datetime import datetime
import pymysql

db = None

app = Flask(__name__)
books=[
    {
        'name' :u'红楼梦',
        'author':u'曹雪芹',
        'price':200
    },
    {
        'name': u'水浒传',
        'author': u'施耐庵',
        'price': 100
    },
    {
        'name': u'三国演义',
        'author': u'罗贯中',
        'price': 120
    },
    {
        'name': u'西游记',
        'author': u'吴承恩',
        'price': 230
    }
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html',books=[], sql_statement="")
    else:
        #print(request)
        #print(request.data)
        data = json.loads(request.data)
        print(data)
        terminal_type = data['terminal_type']
        dot_key = data['dot_key']
        start_time = None
        if data['start_time']:
            start_time = datetime.timestamp(datetime.fromisoformat(data['start_time']))
        print(start_time)
        end_time = None
        if data['end_time']:
            end_time = datetime.timestamp(datetime.fromisoformat(data['end_time']))
        print(end_time)
        start_version = data['start_version']
        end_version = data['end_version']

        sql_statement = 'SELECT * FROM db_dot_record\n'
        condition = " terminal_type: {0}, dot_key: {1}, start_time: {2}, end_time: {3}, start_version: {4}, end_version: {5}"
        condition = condition.format(terminal_type, dot_key, data['start_time'], data['end_time'], start_version, end_version)
        return render_template('index.html',books=books, sql_statement=sql_statement, condition=condition)

if __name__ == '__main__':
    '''
    db = pymysql.connect(host='localhost',
                         user='testuser',
                         password='test123',
                         database='TESTDB')
    '''
    app.run(debug=True)

