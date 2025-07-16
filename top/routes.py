from flask import render_template
from top import top_bp

@top_bp.route('/')
def index():
    return render_template('index.html')  # top/templates/index.html を表示