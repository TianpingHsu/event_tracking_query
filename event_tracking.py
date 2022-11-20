#encoding:utf-8
from flask import Flask, render_template
from flask import redirect, url_for, request
import json
from datetime import datetime
import pymysql

db = None
VERSIONS = ["v13.7", "v15.6"]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', records=[], versions=VERSIONS, sql_statement="")
    else:
        data = json.loads(request.data)
        print(data)
        terminal_type = data['terminal_type']
        dot_key = data['dot_key']
        versions = data['versions']
        print(versions)
        start_time = None
        if data['start_time']:
            start_time = datetime.timestamp(datetime.fromisoformat(data['start_time']))
        print(start_time)
        end_time = None
        if data['end_time']:
            end_time = datetime.timestamp(datetime.fromisoformat(data['end_time']))
        print(end_time)

        sql_statement = 'SELECT * FROM db_dot_record'
        condition = " terminal_type: {0}, dot_key: {1}, start_time: {2}, end_time: {3}"
        condition = condition.format(terminal_type, dot_key, data['start_time'], data['end_time'])

        records = [
        ]
        return render_template('index.html',
                               records=records,
                               versions=VERSIONS,
                               sql_statement=sql_statement,
                               condition=condition)

if __name__ == '__main__':
    '''
    db = pymysql.connect(host='localhost',
                         user='testuser',
                         password='test123',
                         database='TESTDB')
    '''
    app.run(debug=True)

