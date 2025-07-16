from flask import Flask
from top import top_bp
from diary import diary_bp
from diary.routes import init_db

app = Flask(__name__)
app.register_blueprint(top_bp, url_prefix='/')
app.register_blueprint(diary_bp, url_prefix='/diary')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)