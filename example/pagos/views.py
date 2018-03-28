# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time

from django.shortcuts import render

from khipu.communication import Khipu
from khipu.forms import KhipuCreatePaymentForm


def carro(request):
    """
    Ejemplo de carro de compras
    """
    khipu = Khipu()

    # Obtener los bancos disponibles en Khipu para que el usuario pueda pagar.
    banks_khipu = khipu.service('GetBanks')

    # Crear una orden de compra en Khipu y regresar las URL's para que puedan
    # ser usadas como se quiera
    url_carro_khipu = khipu.service(
        'CreatePaymentURL',
        **{
            'subject': 'Esto es un pago de pruebas',
            'currency': 'CLP',
            'amount': '3000.0000',
            'transaction_id': str(int(time.time()))
        })

    # Crear un formulario Django con los botoner predeterminados para pagar.
    form_payment_khipu = KhipuCreatePaymentForm(**{
        'subject': 'Esto es un pago de pruebas via Django-Form',
        'currency': 'CLP',
        'amount': '6000.0000',
        'picture_url': 'https://www.worksoft.com/wp-content/uploads/2015/07/ariba-logo.png',
        'transaction_id': str(int(time.time()))
    })
    output = {
        'url_carro_khipu': url_carro_khipu, 'banks_khipu': banks_khipu,
        'form_payment_khipu': form_payment_khipu
    }
    return render(request, 'carro.html', output)
