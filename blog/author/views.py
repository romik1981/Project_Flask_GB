from flask import render_template, Blueprint
from flask_login import login_required

from blog.models.author import Author

author = Blueprint('author', __name__, url_prefix='/authors', static_folder='../static')

@author.route('/')
# @login_required
def author_list():
    authors = Author.query.all()
    return render_template('authors/list.html',
                           authors=authors
                           )
