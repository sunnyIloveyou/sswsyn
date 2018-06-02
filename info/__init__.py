
# 导入session
from flask import Flask
# 导入csrf跨站请求保护
from flask_wtf import CSRFProtect
# 导入数据库
from flask_sqlalchemy import SQLAlchemy

from flask_session import Session
from config import myconfig

db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(myconfig[config_name])
    db.init_app(app)
    CSRFProtect(app)
    Session(app)
    return app