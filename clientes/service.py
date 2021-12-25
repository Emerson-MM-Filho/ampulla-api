from clientes.models import Cliente


class ClientService:

    def __init__(self, client_id=None):
        if client_id:
            try:
                client = Cliente.objects.get(id=client_id)
                self.client = client
            except Exception:
                raise Exception(
                    f'[ERROR][CLIENT SERVICE] Client does not exists. ({client_id=})'
                )

