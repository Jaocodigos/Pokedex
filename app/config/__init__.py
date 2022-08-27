from os import environ


class Config(object):
    def __init__(self):
        self.TESTING = False
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.SECRET_KEY = environ['SECRET_KEY']
        self.ADMIN_USERNAME = environ['ADMIN_USERNAME']
        self.ADMIN_PASSWORD = environ['ADMIN_PASSWORD']


class TestConfig(Config):
    def __init__(self):
        super().__init__()
        self.TESTING = True
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
        self.SQLALCHEMY_ECHO = True
        self.SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(Config):
    def __init__(self):
        super().__init__()
        self.MYSQL_USER = environ['MYSQL_USER']
        self.MYSQL_PASSWORD = environ['MYSQL_PASSWORD']
        self.MYSQL_HOST = environ['MYSQL_HOST']
        self.MYSQL_DATABASE = environ['MYSQL_DATABASE']
        self.SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{self.MYSQL_USER}:' \
                                       f'{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}/' \
                                       f'{self.MYSQL_DATABASE}'
        self.SQLALCHEMY_ECHO = True


def get_config(env):
    if env == "development":
        return DevConfig()
    elif env == "testing":
        return TestConfig()
