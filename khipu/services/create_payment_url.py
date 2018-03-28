# -*- coding: utf-8 -*-
from collections import OrderedDict

from .protocol import KhipuProtocol, KHIPU_API_VERSION
from ..models import Payment


class CreatePaymentURL(KhipuProtocol):
    """
    Crear pago obtener la URL Khipu para usarse por los pagadores.
    @Parameters
        subject: el asunto del cobro. Con un máximo de 255 caracteres.
        currency: Parámetro de formulario — El código de moneda en formato ISO-4217
        amount: el monto del cobro.
        transaction_id:
            en esta variable puedes enviar un identificador propio de tu
            transacción, como un número de factura.
        custom:
            en esta variable puedes enviar información personalizada de la
            transacción, como por ejemplo, instrucciones de preparación
            o dirección de envio.
        body: descripción del cobro.
        bank_id:
            el código del banco.
            Puedes obtener los códigos usando la llamada GetBanks
        return_url:
            la dirección URL a donde enviar al cliente cuando el pago está
            siendo verificado
        cancel_url:
            la dirección URL a donde enviar al cliente si se arrepiente
            de hacer la transacción
        picture_url:
            una dirección URL de una foto de tu producto o servicio
            para mostrar en la página del cobro
        notify_url:
            Parámetro de formulario — La dirección del web-service que
            utilizará khipu para notificar cuando el pago esté conciliado
        contract_url:
            Parámetro de formulario — La dirección URL del archivo PDF con el
            contrato a firmar mediante este pago.
            El cobrador debe estar habilitado para este servicio y el campo
            'fixed_payer_personal_identifier' es obgligatorio
        notify_api_version:
            Parámetro de formulario — Versión de la API de notifiaciones para
            recibir avisos por web-service
        expires_date:
            fecha de expiración del cobro. Pasada esta fecha el cobro es inválido.
            Formato Unix timestamp. Debe corresponder a una fecha en el futuro.
        send_email:
            Parámetro de formulario — Si es 'true', se enviará una solicitud
            de cobro al correo especificado en 'payer_email'
        payer_name:
            Parámetro de formulario — Nombre del pagador.
            Es obligatorio cuando send_email es 'true'
        payer_email:
            Parámetro de formulario — Correo del pagador.
            Es obligatorio cuando send_email es 'true'
        send_reminders:
            Parámetro de formulario — Si es 'true', se enviarán recordatorios de cobro.
        responsible_user_email:
            Parámetro de formulario — Correo electrónico del responsable de este
            cobro, debe corresponder a un usuario khipu con permisos para cobrar
            usando esta cuenta de cobro
        fixed_payer_personal_identifier:
            Parámetro de formulario — Identificador personal. Si se especifica,
            solo podrá ser pagado usando ese identificador
        integrator_fee:
            Parámetro de formulario — Comisión para el integrador. Sólo es válido
            si la cuenta de cobro tiene una cuenta de integrador asociada
    @Return Values
        payment_id:
            String Identificador único del pago, es una cadena alfanumérica de 12 caracteres
        payment_url:
            String URL principal del pago, si el usuario no ha elegido previamente
            un método de pago se le muestran las opciones
        simplified_transfer_url:
            String URL de pago simplificado
        transfer_url:
            String URL de pago normal
        app_url:
            String URL para invocar el pago desde un dispositivo móvil usando la APP de khipu
        ready_for_terminal:
            Boolean Es 'true' si el pago ya cuenta con todos los datos necesarios
            para abrir directamente la aplicación de pagos khipu
    """
    def __init__(self, receiver_id, secret, service_name, **kwargs):
        super(CreatePaymentURL, self).__init__(
            receiver_id, secret, service_name, **kwargs)
        self.method = 'POST'
        self.path = 'payments'
        fields = [
            'subject', 'currency', 'amount', 'transaction_id', 'custom',
            'body', 'bank_id', 'return_url', 'cancel_url', 'picture_url',
            'notify_url', 'contract_url', 'notify_api_version',
            'expires_date', 'send_email', 'payer_name', 'payer_email',
            'send_reminders', 'responsible_user_email',
            'fixed_payer_personal_identifier', 'integrator_fee'
        ]
        fields.sort()
        self.data = OrderedDict()
        for field in fields:
            if kwargs.get(field):
                if type(kwargs.get(field)) == bool:
                    self.data[field] = str(kwargs.get(field)).lower()
                else:
                    self.data[field] = kwargs.get(field)

        # Llamar al servicio Khipu
        self.request()

        # Con la data respuesta creamos data en el modelo.
        data_to_model = self.data.copy()
        data_to_model.update(self.data_response)
        Payment.objects.create(**data_to_model)
