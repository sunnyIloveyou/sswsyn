# 导入session
from flask import Flask,session
# 导入csrf跨站请求保护
from flask_wtf import CSRFProtect
# 导入数据库
from flask_sqlalchemy import SQLAlchemy
# 导入管理器
from flask_script import Manager
# 导入迁移框架
from flask_migrate import Migrate, MigrateCommand

from flask_session import Session
from config import myconfig
app = Flask(__name__)
db = SQLAlchemy(app)
# 使用迁移框架
Migrate(app,db)
# 实例化管理器对象
manager = Manager(app)
# 绑定迁移命令
manager.add_command('db',MigrateCommand)
app.config.from_object(myconfig['development'])
Session(app)
CSRFProtect(app)
@app.route('/')
def hello_world():
    session['name'] = 'python02'
    return 'hello_world'
if __name__ == '__main__':
    manager.run()