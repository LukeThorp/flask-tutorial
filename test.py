"""test.py"""
ENVIRONMENT = 'development'
DB = {
    'development': {
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite3',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    },
    'production': {
        'SQLALCHEMY_DATABASE_URI': 'mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}'.format(
            username="",
            password="",
            hostname="",
            databasename=""),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_POOL_RECYCLE': 299,
    }
}