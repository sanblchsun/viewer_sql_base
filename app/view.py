import logging
import os
import sys
from configparser import ConfigParser
from app import app
from flask import render_template
from models import MYSQLer


@app.route('/')
def index():
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, 'mysql.ini')
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        logging.info('Config mysql not found')
        sys.exit(1)
    host = cfg.get("connect", "host")
    port = int(cfg.get("connect", "port"))
    user = cfg.get("connect", "user")
    password = cfg.get("connect", "password")
    database = cfg.get("connect", "database")

    mysql_object = MYSQLer(host=host,
            port=port,
            user=user,
            password=password,
            database=database)

    rows = mysql_object.read_all()

    columns = rows[0].keys()
    return render_template('index.html', columns=columns, rows=rows)