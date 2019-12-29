from src.views.invoice import Invoice


def add_routes(api):
    api.add_resource(
        Invoice,
        '/invoice',
        endpoint="get_invoice"
    )
