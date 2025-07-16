from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from diary import diary_bp
from datetime import datetime

DB_NAME = 'diary/diary.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS diary(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     title TEXT NOT NULL,
                     content TEXT NOT NULL,
                     created_at TEXT NOT NULL
                     )''')

@diary_bp.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.execute('SELECT id, title, created_at FROM diary ORDER BY created_at DESC')
    diaries = cursor.fetchall()
    return render_template('diary_index.html', diaries = diaries)

@diary_bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method=='POST':
        title = request.form['title']
        content = request.form['content']
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute('INSERT INTO diary (title, content, created_at) VALUES (?, ?, ?)',
                         (title, content, now))
        return redirect(url_for('diary.index'))
    return render_template('diary_form.html')

@diary_bp.route('/detail/<int:diary_id>')
def detail(diary_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.execute('SELECT id, title, content, created_at FROM diary WHERE id = ?', (diary_id,))
    diary = cursor.fetchone()
    conn.close()
    return render_template('diary_detail.html', diary=diary)
