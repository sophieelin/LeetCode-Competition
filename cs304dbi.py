# Drop-in replacement for the CS304 dbi module, for hosting outside the
# CS304 server (e.g. Vercel). Connection settings come from environment
# variables instead of ~/.my.cnf.
import os
import pymysql


def conf(db=None):
    """Kept for compatibility; returns the configured database name."""
    return os.environ.get('DB_NAME', db)


def connect():
    """Return a new connection to the MySQL database."""
    ssl = None
    if os.environ.get('DB_SSL'):
        ca = os.environ.get('DB_SSL_CA')
        ssl = {'ca': ca} if ca else {}
    return pymysql.connect(
        host=os.environ['DB_HOST'],
        port=int(os.environ.get('DB_PORT', 3306)),
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME'],
        ssl=ssl,
        autocommit=False,
    )


def dict_cursor(conn):
    return conn.cursor(pymysql.cursors.DictCursor)


def cursor(conn):
    return conn.cursor()
