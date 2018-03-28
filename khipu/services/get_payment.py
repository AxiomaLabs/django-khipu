# -*- coding: utf-8 -*-
from collections import OrderedDict

from .protocol import KhipuProtocol


class GetPaymentInfo(KhipuProtocol):
    """
    Obtener la info de un pago mediante un Token que Khipu nos proporciona.
    @Parameters
        notification_token: Token que Khipu nos proporciona en una llamada API.
    @Return Values:
        payment_id:
            String Identificador único del pago, es una cadena alfanumérica de
            12 caracteres
        payment_url:
            String URL principal del pago, si el usuario no ha elegido previamente
            un método de pago se le muestran las opciones
        simplified_transfer_url:
            String URL de pago simplificado
        transfer_url:
            String URL de pago normal
        app_url:
            String URL para invocar el pago desde un dispositivo móvil usando la
            APP de khipu
        ready_for_terminal:
            Boolean Es 'true' si el pago ya cuenta con todos los datos necesarios
            para abrir directamente la aplicación de pagos khipu
        notification_token:
            String Cadena de caracteres alfanuméricos que identifican unicamente
            al pago, es el identificador que el servidor de khipu enviará al
            servidor del comercio cuando notifique que un pago está conciliado
        receiver_id:
            Long Identificador único de una cuenta de cobro
        conciliation_date:
            Date Fecha y hora de conciliación del pago. Formato ISO-8601.
            Ej: 2017-03-01T13:00:00Z
        subject:
            String Motivo del pago
        amount:
            Double
        currency:
            String El código de moneda en formato ISO-4217
        status:
            String Estado del pago, puede ser 'pending' (el pagador aún no comienza a pagar),
            'verifying' (se está verificando el pago) o 'done', cuando el pago ya está confirmado
        status_detail:
            String Detalle del estado del pago, 'pending' (el pagadon aún no comienza a pagar),
            'normal' (el pago fue verificado y fue cancelado por algún medio de pago estandar),
            'marked-paid-by-receiver' (el cobrador marco el cobro como pagado por otro medio),
            'rejected-by-payer' (el pagador declaró que no pagará),
            'marked-as-abuse' (el pagador declaró que no pagará y que el cobro fue no solicitado)
            y 'reversed' (el pago fue anulado por el comercio, el dinero fue devuelto al pagador).
        body:
            String Detalle del cobro
        picture_url:
            String URL de cobro
        receipt_url:
            String URL del comprobante de pago
        return_url:
            String URL donde se redirige al pagador luego que termina el pago
        cancel_url:
            String URL donde se redirige al pagador luego de que desiste hacer el pago
        notify_url:
            String URL del webservice donde se notificará el pago
        notify_api_version:
            String Versión de la api de notificación
        expires_date:
            Date Fecha de expiración del pago. En formato ISO-8601
        attachment_urls:
            array[String] URLs de archivos adjuntos al pago
        bank:
            String Nombre del banco seleccionado por el pagador
        bank_id:
            String Identificador del banco seleccionado por el pagador
        payer_name:
            String Nombre del pagador
        payer_email:
            String Correo electrónico del pagador
        personal_identifier:
            String Identificador personal del pagador
        bank_account_number:
            String Número de cuenta bancaria del pagador
        out_of_date_conciliation:
            Boolean Es 'true' si la conciliación del pago fue hecha luego de la fecha de expiración
        transaction_id:
            String Identificador del pago asignado por el cobrador
        custom:
            String Campo genérico que asigna el cobrador al momento de hacer el pago
        responsible_user_email:
            String Correo electrónico de la persona responsable del pago
        send_reminders:
            Boolean Es 'true' cuando este es un cobro por correo electrónico y khipu enviará recordatorios
        send_email:
            Boolean Es 'true' cuando khipu enviará el cobro por correo electrónico
        payment_method:
            String Método de pago usado por el pagador, puede ser
            'regular_transfer' (transferencia normal),
            'simplified_transfer' (transferencia simplificada) o
            'not_available' (para un pago marcado como realizado por otro medio por el cobrador).
    """

    def __init__(self, receiver_id, secret, service_name, **kwargs):
        super(GetPaymentInfo, self).__init__(
            receiver_id, secret, service_name, **kwargs)
        self.method = 'GET'
        self.path = 'payments'

        self.data = {"notification_token": kwargs.get('notification_token')}

        # Llamar al servicio Khipu
        self.request()
