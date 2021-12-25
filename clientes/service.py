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

    def create_client(self, name, phone):
        try:
            self._validate_name(name)
            self._validate_phone(phone)
        except Exception as e:
            print(e)
            return
        client = Cliente.objects.create(name=name, phone=phone)
        client.save()
        self.client = client
        return client

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

    def _validate_phone(self, phone):
        if len(phone) != 11 or phone[2] != '9':
            raise Exception(
                f'[ERROR][VALIDATE NUMBER] Invalid phone: {phone}'
            )

    def update_phone(self, phone):
        if self.client.phone == phone:
            raise Exception(
                f'[ERROR][UPDATE PHONE] The new phone must be different from the current phone ({self.client.phone}).'
            )
        try:
            self._validate_phone(phone)
        except Exception as e:
            print(e)
            return
        self.client.phone = phone
        self.client.save()

