#encoding:utf-8
from flask import Flask, render_template
from flask import redirect, url_for, request
import json
from datetime import datetime
import pymysql

db = None

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', records=[], sql_statement="")
    else:
        data = json.loads(request.data)
        print(data)
        terminal_type = data['terminal_type']
        dot_key = data['dot_key']
        start_version = data['start_version']
        end_version = data['end_version']
        start_time = None
        if data['start_time']:
            start_time = datetime.timestamp(datetime.fromisoformat(data['start_time']))
        print(start_time)
        end_time = None
        if data['end_time']:
            end_time = datetime.timestamp(datetime.fromisoformat(data['end_time']))
        print(end_time)

        sql_statement = 'SELECT * FROM db_dot_record\n'
        condition = " terminal_type: {0}, dot_key: {1}, start_time: {2}, end_time: {3}, start_version: {4}, end_version: {5}"
        condition = condition.format(terminal_type, dot_key, data['start_time'], data['end_time'], start_version, end_version)

        records = [
            (u'红楼梦', u'曹雪芹', 200),
            (u'水浒传', u'施耐庵', 100),
            (u'三国演义', u'罗贯中', 120),
            (u'西游记', u'吴承恩', 230)
        ]
        return render_template('index.html', records=records, sql_statement=sql_statement, condition=condition)

if __name__ == '__main__':
    '''
    db = pymysql.connect(host='localhost',
                         user='testuser',
                         password='test123',
                         database='TESTDB')
    '''
    app.run(debug=True)

