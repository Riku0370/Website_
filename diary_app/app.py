from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = 'diary.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS diary(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     title TEXT NOT NULL,
                     content TEXT NOT NULL,
                     created_at TEXT NOT NULL
                     )''')

@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.execute('SELECT id, title, created_at FROM diary ORDER BY created_at DESC')
    diaries = cursor.fetchall()
    return render_template('index.html', diaries = diaries)

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method=='POST':
        title = request.form['title']
        content = request.form['content']
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute('INSERT INTO diary (title, content, created_at) VALUES (?, ?, ?)',
                         (title, content, now))
        return redirect(url_for('index'))
    return render_template('form.html')

@app.route('/detail/<int:diary_id>')
def detail(diary_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.execute('SELECT id, title, content, created_at FROM diary WHERE id = ?', (diary_id,))
    diary = cursor.fetchone()
    conn.close()
    return render_template('detail.html', diary=diary)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)