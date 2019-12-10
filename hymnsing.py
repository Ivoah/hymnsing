import io
import csv
import time
import pymysql
import datetime
import collections

import matplotlib.pyplot as plt

from uuid import uuid4
from bottle import get, post, request, response, template, redirect, static_file, default_app

import auth

LOGIN_TIME = 60*15 # Keep admins logged in for 15 minutes

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

logins = {}
def get_uuid():
    uuid = request.get_cookie('uuid')
    if not uuid:
        uuid = str(uuid4())
    response.set_cookie('uuid', uuid, path='/', max_age=60*60*24*365.25*10) # Set cookie to expire in ~10 years

    db = pymysql.connect(autocommit=True, **auth.auth)
    with db.cursor() as cursor:
        agent = request.headers.get('User-Agent')
        cursor.execute(
            'INSERT INTO visitors (uuid, last_visit, user_agent) VALUES (%s, now(), %s) ON DUPLICATE KEY UPDATE last_visit=now(), user_agent=%s',
            (uuid, agent, agent)
        )
    db.close()

    return uuid, uuid in logins and time.time() < logins[uuid]

@get('/')
def root():
    uuid, is_admin = get_uuid()
    db = pymysql.connect(**auth.auth)
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT * FROM hymns LEFT JOIN (SELECT num, COUNT(*) likes FROM likes GROUP BY num) likes USING(num) ORDER BY num ASC')
        hymns = cursor.fetchall()
        cursor.execute('SELECT num FROM likes WHERE uuid=%s', uuid)
        likes = [like['num'] for like in cursor.fetchall()]
    return template('templates/main.tpl', sections=group(hymns, 'section', 'subsection'), likes=likes, is_admin=is_admin)

@get('/history')
def history():
    uuid, is_admin = get_uuid()
    db = pymysql.connect(**auth.auth)
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT date, num, title, likes FROM history NATURAL JOIN hymns LEFT JOIN (SELECT num, COUNT(*) likes FROM likes GROUP BY num) likes USING(num) ORDER BY date DESC, idx ASC')
        history = cursor.fetchall()
        cursor.execute('SELECT num FROM likes WHERE uuid=%s', uuid)
        likes = [like['num'] for like in cursor.fetchall()]
    db.close()
    return template('templates/history.tpl', history=group(history, 'date'), likes=likes, is_admin=is_admin)

@get('/history.csv')
def history_csv():
    db = pymysql.connect(**auth.auth)
    with db.cursor() as cursor:
        cursor.execute('SELECT title, count(*) FROM history NATURAL JOIN hymns GROUP BY num HAVING count(*) >= 5 ORDER BY count(*) DESC')
        rows = cursor.fetchall()
    db.close()

    response.content_type = 'text/csv'
    return 'hymn,count\n' + '\n'.join(','.join(f'"{c}"' for c in row) for row in rows)

@get('/login')
def get_login():
    uuid, is_admin = get_uuid()
    if is_admin:
        del logins[uuid]
        redirect('/')
    return template('templates/login.tpl', is_admin=is_admin)

@post('/login')
def post_login():
    uuid, is_admin = get_uuid()
    if request.forms.get('password') == auth.auth['password']:
        logins[uuid] = time.time() + LOGIN_TIME
    else:
        response.status = 401

@get('/<num:int>')
def hymn(num):
    uuid, is_admin = get_uuid()
    db = pymysql.connect(**auth.auth)
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT date FROM history WHERE num=%s ORDER BY date DESC', num)
        history = cursor.fetchall()
        cursor.execute('SELECT * FROM hymns WHERE num=%s', num)
        hymn = cursor.fetchone()
    db.close()
    return template('templates/hymn.tpl', hymn=hymn, history=history, is_admin=is_admin)

@post('/like/<num:int>')
def like(num):
    uuid, is_admin = get_uuid()
    db = pymysql.connect(autocommit=True, **auth.auth)
    with db.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO likes VALUES (%s, %s)', (uuid, num))
        except pymysql.err.IntegrityError:
            response.status = 409
    db.close()

@post('/unlike/<num:int>')
def unlike(num):
    uuid, is_admin = get_uuid()
    db = pymysql.connect(autocommit=True, **auth.auth)
    with db.cursor() as cursor:
        rows = cursor.execute('DELETE FROM likes WHERE uuid=%s AND num=%s', (uuid, num))
        if rows == 0: response.status = 409
    db.close()

@post('/addHymn')
def addHymn():
    uuid, is_admin = get_uuid()
    if not is_admin:
        response.status = 401
        return '<html><body><h1>401 Unauthorized</h1></body></html>'
    try:
        print(request.forms.get('date'))
        date = datetime.date(*map(int, request.forms.get('date').split('-')))
    except (ValueError, TypeError):
        response.status = 400
        return '<html><body><h1>400 Bad Request</h1></body></html>'
    hymn = request.forms.get('hymn')
    db = pymysql.connect(autocommit=True, **auth.auth)
    with db.cursor() as cursor:
        cursor.execute('SELECT count(*) FROM history WHERE date=%s', date)
        next_idx = cursor.fetchone()[0]
        cursor.execute('INSERT INTO history (date, idx, num) VALUES (%s, %s, %s)', (date, next_idx, hymn))

application = default_app()

if __name__ == '__main__':
    from bottle import run

    get('/audio/<filename>')(lambda filename: static_file(filename, root='audio/'))
    get('/css/<filename:path>')(lambda filename: static_file(filename, root='css/'))
    get('/js/<filename:path>')(lambda filename: static_file(filename, root='js/'))

    run(app=application, host='127.0.0.1', port=8080, debug=True, reloader=True)
