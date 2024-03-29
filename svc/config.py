import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_ENABLE_CSRF = True
    # CKEDITOR_FILE_UPLOADER = 'admin.upload_image'

    # MAIL_SERVER = os.getenv('MAIL_SERVER')
    # MAIL_PORT = 465
    # MAIL_USE_SSL = True
    # MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    # MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    # MAIL_DEFAULT_SENDER = ('Bluelog Admin', MAIL_USERNAME)

    # BLUELOG_EMAIL = os.getenv('BLUELOG_EMAIL')
    # BLUELOG_POST_PER_PAGE = 10
    # BLUELOG_MANAGE_POST_PER_PAGE = 15
    # BLUELOG_COMMENT_PER_PAGE = 15
    # # ('theme name', 'display name')
    # BLUELOG_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    # BLUELOG_SLOW_QUERY_THRESHOLD = 1

    # BLUELOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    # BLUELOG_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


class DevelopmentConfig(BaseConfig):
    SECRET_KEY = '123456789012345678901234'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:s@localhost/fizzse?charset=utf8'
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:s@localhost/fizzse?charset=utf8'


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:s@localhost/fizzse?charset=utf8'


class ProductionConfig(BaseConfig):
    SECRET_KEY = '123456789012345678901234'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:s@localhost/fizzse?charset=utf8'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}