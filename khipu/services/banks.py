from .protocol import KhipuProtocol


class GetBanks(KhipuProtocol):

    def __init__(self, receiver_id, secret, service_name, **kwargs):
        super(GetBanks, self).__init__(receiver_id, secret, service_name, **kwargs)
        self.method = 'GET'
        self.path = 'banks'

        # Llamar al servicio Khipu
        self.request()
