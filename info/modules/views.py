from flask import session
from . import ssw
@ssw.route('/')
def hello_world():
    session['name'] = 'python02'
    return 'hello_world'