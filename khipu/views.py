import logging
import traceback

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .communication import Khipu
from .exceptions import KhipuError
from .models import Payment

logger = logging.getLogger(__name__)


def set_khipu_model(**kwargs):
    """
    Setear todos los nuevos valores que tenemos del modelo.
    @Params
        kwargs:
            Todos los valores enviados por parte de Khipu
    """
    payment = Payment.objects.get(payment_id=kwargs.get('payment_id'))
    if payment.amount == kwargs.get('amount'):
        if settings.KHIPU_RECEIVER_ID == kwargs.get('receiver_id'):
            payment.save(**kwargs)
        else:
            payment.status = 'receiver_error'
            payment.notification_token = kwargs.get('notification_token')
            payment.save()
    else:
        payment.status = 'amount_error'
        payment.notification_token = kwargs.get('notification_token')
        payment.save()

    # Enviamos los signlas para que la Django App sea capaz de procesar
    payment.send_signals()

    return payment


@csrf_exempt
@require_POST
def verificacion(request):
    """
    Vista para validar el estatus de un pago. Se recibira por metodo POST un
    Token por parte de Khipu y se verificara en un servicio de Khipu el status
    del pago.
    """
    logger.debug("Informacion con lo que nos envia Khipu {}".format(request.POST))
    api_version = request.POST.get('api_version')
    notification_token = request.POST.get('notification_token')
    khipu = Khipu()
    result = khipu.service('GetPaymentInfo', **{'notification_token': notification_token})
    logger.debug("Informacion que nos envia el servicio de Khipu GetPaymentInfo {}".format(result))
    try:
        # Guardar todos los valores que Khipu nos envia.
        set_khipu_model(**result)
    except Payment.DoesNotExist:
        logger.error("Payment does not exist. Data {}".format(result))
        return HttpResponse(status=400)
    except Exception, e:
        msg = "An error ocurred. Exception: {} Trace: {}".format(e, traceback.format_exc())
        logger.error(msg)
    return HttpResponse()
