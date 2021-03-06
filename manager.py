# 导入管理器
from flask_script import Manager
# 导入迁移框架
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db

app = create_app('development')
# 使用迁移框架
Migrate(app,db)
# 实例化管理器对象
manager = Manager(app)
# 绑定迁移命令
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()