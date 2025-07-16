from flask import Blueprint

top_bp = Blueprint(
    'top',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/top/static'  # これが無ければtop.staticを開くことができない
)

from top import routes  # routes.py内にルート定義がある場合