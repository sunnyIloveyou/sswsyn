from flask import current_app
from flask import session,render_template

from . import ssw
@ssw.route('/')
def hello_world():
    session['name'] = 'python02'
    return render_template('news/detail.html')

@ssw.route('/favicon.ico')
def favicon():
    # 返回小图标使用send_static_file()方法，要用应用上下文current——app调用
    return current_app.send_static_file('news/favicon.ico')

