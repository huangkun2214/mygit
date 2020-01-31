from .main import main
from .users import users

DEFAULT_BLUEPRINT = (
    (main, ''),
    (users,'/users')

)


# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint1, prefix in DEFAULT_BLUEPRINT:
        print (type(blueprint1))
        app.register_blueprint(blueprint1, url_prefix=prefix)
