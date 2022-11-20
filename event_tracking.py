#encoding:utf-8
from flask import Flask, render_template
from flask import redirect, url_for, request
import json
from datetime import datetime
import pymysql

db = None
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
        condition = " terminal_type: {0}, dot_key: {1}, start_time: {2}, end_time: {3} versions: " + ', '.join(VERSIONS)
        condition = condition.format(terminal_type, dot_key, data['start_time'], data['end_time'])

        records = [
        ]
        return render_template('index.html',
                               versions=VERSIONS,
                               ths=TABLE_HEADERS,
                               keys=KEYS,
                               records=records,
                               sql_statement=sql_statement,
                               condition=condition)

def init():
    global VERSIONS
    global KEYS
    global TABLE_HEADERS
    VERSIONS = ["v13.7", "v15.6"]
    filename = './static/keys'
    with open(filename) as f:
        KEYS = [line.rstrip() for line in f]
    filename = './static/table_headers'
    with open(filename) as g:
        TABLE_HEADERS = [line.rstrip() for line in g]

if __name__ == '__main__':
    '''
    db = pymysql.connect(host='localhost',
                         user='testuser',
                         password='test123',
                         database='TESTDB')
    '''
    init()
    app.run(debug=True)

    '''
    #!/usr/bin/python3

    import pymysql
    # connect a database
    db = pymysql.connect(host='172.25.11.125', user='client', password='Qnsz@2022', database='sd_dataserver')

    cursor = db.cursor()
    #https://alpha-test.oi.plus/api/log/dot/query/{tracdId}

    sql = """SELECT * FROM sd_log_dot_record WHERE dot_key="createMeeting";"""

    cursor.execute(sql)

    results = cursor.fetchall()
    for item in results:
        print(item)

    # close db
    db.close()

    '''
