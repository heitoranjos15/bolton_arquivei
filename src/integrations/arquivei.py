import requests
import os
from config import configs

env = configs.get(os.environ.get('service_env', 'dev'))


def invoices_received():
    invoices = dict()
    headers = {
        'Content-Type': "application/json",
        'x-api-id': "f96ae22f7c5d74fa4d78e764563d52811570588e",
        'x-api-key': "cc79ee9464257c9e1901703e04ac9f86b0f387c2",
    }
    url = f'{env.arquivei_url}/v1/nfe/received?cursor=0&limit=50'
    while True:
        response = requests.get(url, headers=headers).json()
        data = response.get('data')
        if not data:
            break
        for invoice in data:
            invoices.update({invoice.get('access_key'): invoice.get('xml')})
        url = response.get('page').get('next')
    return invoices
