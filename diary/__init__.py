from flask import Blueprint

diary_bp = Blueprint(
    'diary',
    __name__,
    template_folder='templates', 
    static_folder='static',
    static_url_path='/diary/static'
    )

from diary import routes