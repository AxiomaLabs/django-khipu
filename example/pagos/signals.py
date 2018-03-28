import logging

from django.dispatch import receiver

from khipu.signals import payment_successful

logging.basicConfig()
log = logging.getLogger(__name__)


@receiver(payment_successful)
def khipu_handler(sender, **kwargs):
    log.info('Esta accediendo a mis logs')
