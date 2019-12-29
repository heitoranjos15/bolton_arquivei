import os
from config import configs
from src.models.invoice import Invoice


env = configs.get(os.environ.get('service_env', 'dev'))
db = env.db


def save_invoice(access_key, value):
    invoice = Invoice(access_key=access_key, value=value)
    db.session.add(invoice)
    db.session.commit()
    return invoice


def search_invoice(access_key):
    return db.session.query(Invoice).filter(
        Invoice.access_key == access_key
    ).first()
