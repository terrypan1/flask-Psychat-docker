# __init_.py:初始化文件，創建falsk應用
# 會自動執行
from flask_cors import CORS
from flask import Flask
from .config import *
from .exts import init_exts
from .urls import *
import datetime
#創建app
def create_app():
    app = Flask(__name__)
    # session 配置
    print(app.config)
    #<Config {'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'SECRET_KEY': None, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': None, 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}>
    app.config['SECRET_KEY'] = 'st923420'
    #設置session過期時間 設置過期8天
    app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=8)

    #配置數據庫
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    # 配置跨域
    CORS(app, cors_allowed_origins="*")
    #初始化插件
    init_exts(app=app)
    return app