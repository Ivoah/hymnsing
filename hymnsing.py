import io
import csv
import pymysql
import operator
import collections

import matplotlib.pyplot as plt

from bottle import get, default_app, template, static_file, response

import auth

with open('hymns.csv') as hymns_file:
    hymns = list(csv.DictReader(hymns_file))

@get('/')
def root():
    return template('templates/main.tpl', hymns=hymns)

@get('/history')
def history():
    db = pymysql.connect(*auth)
    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM history ORDER BY date DESC')
        history = cursor.fetchall()
    db.close()
    return template('templates/history.tpl', hymns=hymns, history=history)

@get('/history.png')
def history_png():
    db = pymysql.connect(*auth)
    with db.cursor() as cursor:
        cursor.execute('SELECT hymns FROM history')
        rows = cursor.fetchall()
    db.close()

    counter = collections.Counter(hymn for hymns in rows for hymn in hymns[0].strip('|').split('|'))
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
    db = pymysql.connect(*auth)
    with db.cursor() as cursor:
        cursor.execute('SELECT date FROM history WHERE hymns LIKE \'%%|%s|%%\' ORDER BY date DESC', hymn)
        history = cursor.fetchall()
    db.close()
    return template('templates/hymn.tpl', hymn=hymn, hymns=hymns, history=history)


application = default_app()

if __name__ == '__main__':
    from bottle import run

    get('/static/<filename>')(lambda filename: static_file(filename, root='static/'))
    get('/audio/<filename>')(lambda filename: static_file(filename, root='audio/'))

    run(app=application, host='127.0.0.1', port=8080, debug=True, reloader=True)
