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

    def _validate_name(self, name):
        if len(name) < 2:
            raise Exception(
                f'[ERROR][VALIDATE NAME] Invalid name: {name}'
            )
        for letter in name:
            if letter.isdigit():
                raise Exception(
                    f'[ERROR][VALIDATE NAME] Invalid name: {name}'
                )

