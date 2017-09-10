from urllib.request import urlopen
import urllib.error
import json
import sqlite3
import ssl


def run_sql():

    PTT_JSON = 'data.json'

    conn = sqlite3.connect('ptt.sqlite')
    cur = conn.cursor()

    cur.execute('''
                CREATE TABLE IF NOT EXISTS Beauty
                (title TEXT, liked INTEGER, Href TEXT)''')


    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE



    with open(PTT_JSON, 'r') as f:
        js = json.load(f)


    countnew = 0
    countold = 0
    for u in js:
        title=u['tilte']
        liked=u['liked']
        href=u['href']

        try:
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
                        (count+1, friend))
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Beauty (title, liked, href)
                        VALUES (?, ?, ?)''', (title,liked,href ))
            countnew = countnew + 1
        print('New accounts=', countnew, ' revisited=', countold)
        conn.commit()
    cur.close()
