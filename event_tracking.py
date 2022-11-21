#encoding:utf-8
from flask import Flask, render_template
from flask import redirect, url_for, request
import json
from datetime import datetime
import pymysql

DB = None
KEYS = None
VERSIONS = None
TABLE_HEADERS = None

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html',
                               versions=VERSIONS,
                               keys=KEYS,
                               records=[],
                               sql_statement="")
    else:
        data = json.loads(request.data)
        print(data)
        terminal_type = data['terminal_type']
        dot_key = data['dot_key']
        versions = data['versions']
        #start_time = datetime.timestamp(datetime.fromisoformat(data['start_time']))
        #end_time = datetime.timestamp(datetime.fromisoformat(data['end_time']))
        start_time = data['start_time']
        end_time = data['end_time']

        sql_statement = \
            'SELECT * FROM sd_log_dot_record WHERE (terminal_type="{0}") AND (dot_key="{1}") AND (gmt_create >= "{2}" AND gmt_create <= "{3}")'.format(terminal_type, dot_key, start_time, end_time)
        if len(versions):
            versions = [version[1:] for version in versions]  # erase 'v'
            versions = list(map(lambda s: '"' + s + '"', versions))
            str_versions = ', '.join(versions)
            sql_statement += ' AND terminal_version IN({0})'.format(str_versions)

        print(sql_statement)

        global DB
        cursor = DB.cursor()
        cursor.execute(sql_statement);
        results = cursor.fetchall()
        #for item in results:
        #print(item)
        records = results
        total_count = len(records)

        condition = " terminal_type: {0}, dot_key: {1}, start_time: {2}, end_time: {3} versions: " + ', '.join(VERSIONS)
        condition = condition.format(terminal_type, dot_key, data['start_time'], data['end_time'])
        return render_template('index.html',
                               versions=VERSIONS,
                               ths=TABLE_HEADERS,
                               keys=KEYS,
                               total_count=total_count,
                               records=records,
                               sql_statement=sql_statement,
                               condition=condition)

def init():
    global VERSIONS
    global KEYS
    global TABLE_HEADERS
    VERSIONS = ["v13.7", "v15.2"]
    filename = './static/keys'
    with open(filename) as f:
        KEYS = [line.rstrip() for line in f]
    filename = './static/table_headers'
    with open(filename) as g:
        TABLE_HEADERS = [line.rstrip() for line in g]


    global DB
    DB = pymysql.connect(host='172.25.11.125', user='client', password='Qnsz@2022', database='sd_dataserver')

if __name__ == '__main__':
    '''
    db = pymysql.connect(host='localhost',
                         user='testuser',
                         password='test123',
                         database='TESTDB')
    '''
    init()
    #app.run(debug=True)
    app.run(host="0.0.0.0", debug=True)

