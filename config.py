# StrictRedis 对象方法 用python与redis相互的时候都需要导入这个模块
from redis import StrictRedis

class Config(object):
    DEBUG = True
    # 使用session 要设置密
    SECRET_KEY = '7ovxKULnydmrdknfXFfOWRNWflMD5OuFzMdoz5S3uiA='
    # 链接数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/syn'
    #配置数据库动态追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 配置ridis基本信息
    SESSION_TYPE = 'redis'
    # 对session信息是否加密
    SESSION_USE_SIGNER = True
    # redis对象
    SESSION_REDIS = StrictRedis(host='localhost',port=6379)
    #制定session过期时间以秒为单位
    PERMANENT_SESSION_LIFETIME = 86400



