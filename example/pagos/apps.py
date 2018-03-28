# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class PagosConfig(AppConfig):
    name = 'pagos'

    def ready(self):
        # import signal handlers
        from pagos.signals import khipu_handler
