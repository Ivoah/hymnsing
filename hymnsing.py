import io
import csv
import pymysql
import operator
import collections

import matplotlib.pyplot as plt

from uuid import uuid4
from bottle import get, default_app, template, static_file, response, request

import auth

def get_login():
    uuid = request.get_cookie("uuid")
    if not uuid:
        uuid = uuid4()
        response.set_cookie("uuid", str(uuid), max_age=60*60*24*365.25*10) # Set cookie to expire in 10 years
    return uuid

@get('/')
def root():
    uuid = get_login()
    db = pymysql.connect(**auth.auth)
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT * FROM hymns LEFT JOIN (SELECT num, COUNT(*) likes FROM likes GROUP BY num) likes USING(num) ORDER BY num ASC')
        hymns = cursor.fetchall()
    return template('templates/main.tpl', hymns=hymns, uuid=uuid)

@get('/history')
def history():
    uuid = get_login()
    db = pymysql.connect(**auth.auth)
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT * FROM history ORDER BY date DESC')
        history = cursor.fetchall()
        cursor.execute('SELECT * FROM hymns LEFT JOIN (SELECT num, COUNT(*) likes FROM likes GROUP BY num) likes USING(num) ORDER BY num ASC')
        hymns = cursor.fetchall()
    db.close()
    return template('templates/history.tpl', hymns=hymns, history=history)

@get('/history.png')
def history_png():
    db = pymysql.connect(**auth.auth)
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT hymns FROM history')
        rows = cursor.fetchall()
        cursor.execute('SELECT * FROM hymns LEFT JOIN (SELECT num, COUNT(*) likes FROM likes GROUP BY num) likes USING(num) ORDER BY num ASC')
        hymns = cursor.fetchall()
    db.close()

    counter = collections.Counter(hymn for hymns in rows for hymn in hymns['hymns'].strip('|').split('|'))
    xs, ys = zip(*counter.most_common())
    names = [hymns[int(num) - 1]['title'] for num in xs]

    plt.figure(figsize=(15, 8))
    plt.xticks(rotation='vertical')
    plt.subplots_adjust(0.05, 0.5, 0.95, 0.95)
    plt.bar(names, ys)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    response.content_type = 'image/png'
    return img.getvalue()

@get('/<hymn:int>')
def hymn(hymn):
    uuid = get_login()
    db = pymysql.connect(**auth.auth)
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT date FROM history WHERE hymns LIKE \'%%|%s|%%\' ORDER BY date DESC', hymn)
        history = cursor.fetchall()
        cursor.execute('SELECT * FROM hymns LEFT JOIN (SELECT num, COUNT(*) likes FROM likes GROUP BY num) likes USING(num) ORDER BY num ASC')
        hymns = cursor.fetchall()
    db.close()
    return template('templates/hymn.tpl', hymn=hymn, hymns=hymns, history=history)

application = default_app()

if __name__ == '__main__':
    from bottle import run

    get('/audio/<filename>')(lambda filename: static_file(filename, root='audio/'))
    get('/css/<filename:path>')(lambda filename: static_file(filename, root='css/'))
    get('/font/<filename:path>')(lambda filename: static_file(filename, root='font/'))
    get('/img/<filename:path>')(lambda filename: static_file(filename, root='img/'))
    get('/js/<filename:path>')(lambda filename: static_file(filename, root='js/'))
    get('/scss/<filename:path>')(lambda filename: static_file(filename, root='scss/'))

    run(app=application, host='127.0.0.1', port=8080, debug=True, reloader=True)
