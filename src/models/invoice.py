import os
from datetime import datetime
from config import configs


env = configs.get(os.environ.get('service_env', 'dev'))
db = env.db

class Invoice(db.Model):
    __tablename__ = 'invoice'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    access_key = db.Column(db.String(280), nullable=False)
    value = db.Column(db.String(280), nullable=False)
