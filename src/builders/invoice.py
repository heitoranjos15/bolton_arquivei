from src.queries.invoice import search_invoice, save_invoice
from src.integrations.arquivei import invoices_received


def get_invoice(access_key):
    invoice = search_invoice(access_key)
    if invoice:
        return invoice.value
    else:
        invoice_from_arquivei = invoices_received().get(access_key)
        if invoice_from_arquivei:
            save_invoice(access_key, invoice_from_arquivei)
            return invoice_from_arquivei
