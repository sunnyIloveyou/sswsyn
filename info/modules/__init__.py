
# 从flask这个包中导入蓝图
from flask import Blueprint
# 创建蓝图对象
ssw = Blueprint('ssw',__name__)
from . import views
