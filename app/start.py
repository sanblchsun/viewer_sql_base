from flask import Flask
from config import Configuration

app_run = Flask(__name__)
app_run.config.from_object(Configuration)
