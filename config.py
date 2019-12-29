import os
from flask_sqlalchemy import SQLAlchemy


class Development:

    def __init__(self):
        self.db = SQLAlchemy()
        self.enviroment = 'dev'
        self.db_host = 'sqlite:///bolton.db'
        self.arquivei_url = 'https://sandbox-api.arquivei.com.br'


class Production:

    def __init__(self):
        self.db = SQLAlchemy()
        self.enviroment = 'prd'
        self.db_host = 'sqlite:///bolton.db'
        self.arquivei_url = 'https://sandbox-api.arquivei.com.br'


class Testing:

    def __init__(self):
        self.db = SQLAlchemy()
        self.enviroment = 'testing'
        self.db_host = 'sqlite://'
        self.arquivei_url = 'https://test-api.arquivei.com.br'


configs = {
    'dev': Development(),
    'prd': Production(),
    'test': Testing()
}
