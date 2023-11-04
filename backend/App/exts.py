# 1.導入第三方插件
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
# 2.初始化
db = SQLAlchemy()
migrate = Migrate()
api = Api()
# 3.和app對象綁定
def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)
    api.init_app(app=app)