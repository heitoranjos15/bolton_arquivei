import json
import responses
from src.tests.helper.base_test import BaseTestCase
from config import configs

env = configs.get('test')


class TestInvoiceRoute(BaseTestCase):
    def test_invoice_from_db(self):
        payload = json.dumps({"access_key": "123"})
        response = self.client.post('/invoice', data=payload)
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data.get('xml_value') == 'xml'

    def test_invoice_send_no_access_key(self):
        response = self.client.post('/invoice')
        assert response.status_code == 400

    @responses.activate
    def test_invoice_from_arquivei(self):
        mock_body = dict()
        with open('src/tests/mock/invoice_arquivei.json') as json_file:
            mock_body = json.load(json_file)
        responses.add(responses.POST, f'{env.arquivei_url}/v1/nfe/received?cursor=0&limit=50', body=mock_body)
        payload = json.dumps({"access_key": "35140330290824000104550010003715421390782397"})
        response = self.client.post('/invoice', data=payload)
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data.get('xml_value') == mock_body.get('data')[0].get('xml')

    @responses.activate
    def test_invoice_when_db_and_arquivei_is_not_found(self):
        mock_body = dict()
        with open('src/tests/mock/invoice_arquivei.json') as json_file:
            mock_body = json.load(json_file)
        responses.add(responses.POST, f'{env.arquivei_url}/v1/nfe/received?cursor=0&limit=50', body=mock_body)
        payload = json.dumps({"access_key": "qwe"})
        response = self.client.post('/invoice', data=payload)
        assert response.status_code == 404
