class Config(object):
    HOST = "localhost"
    PORT = 3306
    USER = "root"
    PASSWORD = ""
    DB = "db_books"
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
