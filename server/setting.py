import os


DEBUG = True

_default_db_data = {
    'user':  'admin', 
    'password':  '', 
    'host':  'db', 
    'port':  '5432', 
    'name':  'CADB'
}

def get_db_setting(default=_default_db_data):
    DATABASE = {
        'dbms': 'postgresql',
        'driver': 'psycopg2',
    }

    db_keys = (
        ('DATABASE_NAME', 'name'),
        ('DATABASE_HOST', 'host'),
        ('DATABASE_PORT', 'port'),
        ('DATABASE_USER', 'user'),
        ('DATABASE_PASSWORD', 'password')
    )

    for (envkey, dictkey) in db_keys:
        if envkey in os.environ:
            DATABASE[dictkey] = os.environ[envkey]
        else:
            DATABASE[dictkey] = default[dictkey]

    return DATABASE
