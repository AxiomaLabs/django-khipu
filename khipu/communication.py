# -*- coding: utf-8 -*-
import logging

from django.conf import settings

from . import services
from .exceptions import KhipuError

logger = logging.getLogger(__name__)


class Khipu(object):
    """
    Centralizar todos los servicios que presta Khipu
    """

    def __init__(self):
        self.services = [
            'GetBanks',
            'CreatePaymentURL',
            'GetPaymentInfo',
        ]

    def service(self, service_name, **kwargs):
        """
        Carga el servicio requerido.
        @Parameters
            service_name: Nombre del servicio requerido de Khipu.
            kwargs: Dict con data que necesita el servicio.
        @Return
            Objeto Request con la data que responde Khipu.
        """
        if service_name in self.services:
            if settings.KHIPU_RECEIVER_ID and settings.KHIPU_SECRET_KEY:
                service = getattr(
                    services, service_name
                )(settings.KHIPU_RECEIVER_ID, settings.KHIPU_SECRET_KEY, service_name, **kwargs)
                return service.response()
            else:
                msg = "The authentication is necessary for the service {} {} {} ".format(service_name, settings.KHIPU_SECRET_KEY, settings.KHIPU_RECEIVER_ID)
                logger.error(msg)
                raise KhipuError(msg)
        else:
            msg = "The service does not exist {}".format(service_name)
            logger.error(msg)
            raise KhipuError(msg)
