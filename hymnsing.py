import io
import csv
import pymysql
import collections

import matplotlib.pyplot as plt

from uuid import uuid4
from bottle import *

import auth

def group(l, *ks):
    ol = []
    il = []
    ck = None
    for e in l:
        if ck != {k: e[k] for k in ks}:
            ol.append((ck, il))
            il = []
            ck = {k: e[k] for k in ks}
        il.append({k: v for k, v in e.items() if k not in ks})
    return ol[1:]

def get_login():
    uuid = request.get_cookie("uuid")
    if not uuid:
        uuid = str(uuid4())
    response.set_cookie("uuid", uuid, path='/', max_age=60*60*24*365.25*10) # Set cookie to expire in ~10 years

    db = pymysql.connect(autocommit=True, **auth.auth)
    with db.cursor() as cursor:
        cursor.execute('INSERT INTO visitors (uuid, last_visit) VALUES (%s, now()) ON DUPLICATE KEY UPDATE last_visit=now()', uuid)
    db.close()

    return uuid

@get('/')
def root():
    uuid = get_login()
    db = pymysql.connect(**auth.auth)
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT * FROM hymns LEFT JOIN (SELECT num, COUNT(*) likes FROM likes GROUP BY num) likes USING(num) ORDER BY num ASC')
        hymns = cursor.fetchall()
        cursor.execute('SELECT num FROM likes WHERE uuid=%s', uuid)
        likes = [like['num'] for like in cursor.fetchall()]
    return template('templates/main.tpl', sections=group(hymns, 'section', 'subsection'), likes=likes)

@get('/history')
def history():
    uuid = get_login()
    db = pymysql.connect(**auth.auth)
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT date, num, title, likes FROM history NATURAL JOIN hymns LEFT JOIN (SELECT num, COUNT(*) likes FROM likes GROUP BY num) likes USING(num) ORDER BY date DESC, idx ASC')
        history = cursor.fetchall()
        cursor.execute('SELECT num FROM likes WHERE uuid=%s', uuid)
        likes = [like['num'] for like in cursor.fetchall()]
    db.close()
    return template('templates/history.tpl', history=group(history, 'date'), likes=likes)

@get('/history.png')
def history_png():
    db = pymysql.connect(**auth.auth)
    with db.cursor() as cursor:
        cursor.execute('SELECT title, count(*) FROM history NATURAL JOIN hymns GROUP BY num ORDER BY count(*) DESC')
        rows = cursor.fetchall()
    db.close()

    xs, ys = zip(*rows)

    plt.figure(figsize=(15, 8))
    plt.xticks(rotation='vertical')
    plt.subplots_adjust(0.05, 0.5, 0.95, 0.95)
    plt.bar(xs, ys)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    response.content_type = 'image/png'
    return img.getvalue()

@get('/<num:int>')
def hymn(num):
    uuid = get_login()
    db = pymysql.connect(**auth.auth)
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT date FROM history WHERE num=%s ORDER BY date DESC', num)
        history = cursor.fetchall()
        cursor.execute('SELECT * FROM hymns WHERE num=%s', num)
        hymn = cursor.fetchone()
    db.close()
    return template('templates/hymn.tpl', hymn=hymn, history=history)

@post('/like/<num:int>')
def like(num):
    uuid = get_login()
    db = pymysql.connect(autocommit=True, **auth.auth)
    with db.cursor() as cursor:
        cursor.execute('INSERT IGNORE INTO likes VALUES (%s, %s)', (uuid, num))
    db.close()

@post('/unlike/<num:int>')
def unlike(num):
    uuid = get_login()
    db = pymysql.connect(autocommit=True, **auth.auth)
    with db.cursor() as cursor:
        cursor.execute('DELETE FROM likes WHERE uuid=%s AND num=%s', (uuid, num))
    db.close()

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
