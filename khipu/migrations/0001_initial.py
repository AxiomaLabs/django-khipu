# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=200, verbose_name=b'ID de la compra')),
                ('subject', models.CharField(max_length=500, verbose_name=b'Subject')),
                ('currency', models.CharField(max_length=20, verbose_name=b'Currency')),
                ('amount', models.CharField(max_length=100, verbose_name=b'Amount')),
                ('transaction_id', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Transaction ID')),
                ('custom', models.CharField(blank=True, max_length=500, null=True, verbose_name=b'Custom')),
                ('body', models.TextField(blank=True, null=True, verbose_name=b'Body')),
                ('bank', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Bank nombre')),
                ('bank_id', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Bank ID')),
                ('payment_url', models.URLField(blank=True, null=True, verbose_name=b'Payment URL')),
                ('simplified_transfer_url', models.URLField(blank=True, null=True, verbose_name=b'Simplified URL')),
                ('transfer_url', models.URLField(blank=True, null=True, verbose_name=b'Transfer URL')),
                ('app_url', models.URLField(blank=True, null=True, verbose_name=b'App URL')),
                ('return_url', models.URLField(blank=True, null=True, verbose_name=b'Return URL')),
                ('cancel_url', models.URLField(blank=True, null=True, verbose_name=b'Cancel URL')),
                ('picture_url', models.URLField(blank=True, null=True, verbose_name=b'Picture URL')),
                ('notify_url', models.URLField(blank=True, null=True, verbose_name=b'Notify URL')),
                ('contract_url', models.URLField(blank=True, null=True, verbose_name=b'Contract URL')),
                ('notify_api_version', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'API Version notify')),
                ('expires_date', models.DateTimeField(blank=True, null=True, verbose_name=b'Expires')),
                ('send_email', models.BooleanField(default=False, verbose_name=b'Send email')),
                ('payer_name', models.CharField(blank=True, max_length=300, null=True, verbose_name=b'Payer name')),
                ('payer_email', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Payer email')),
                ('send_reminders', models.BooleanField(default=False, verbose_name=b'Reminders')),
                ('responsible_user_email', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Responsable del pago')),
                ('personal_identifier', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Identificador personal pagador')),
                ('fixed_payer_personal_identifier', models.CharField(blank=True, max_length=30, null=True, verbose_name=b'Identificador personal')),
                ('integrator_fee', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Comision integrador')),
                ('ready_for_terminal', models.BooleanField(default=False, verbose_name=b'Redy for terminal')),
                ('notification_token', models.CharField(blank=True, max_length=400, null=True, verbose_name=b'Token verificacion Khipu')),
                ('receiver_id', models.IntegerField(blank=True, null=True, verbose_name=b'Receiver ID')),
                ('conciliation_date', models.DateTimeField(blank=True, null=True, verbose_name=b'Concilation date')),
                ('status', models.CharField(blank=True, choices=[(b'pending', b'Pagador a\xc3\xban no paga'), (b'veryfing', b'Se est\xc3\xa1 verificando el pago'), (b'done', b'El pago ya est\xc3\xa1 confirmado'), (b'amount_error', b'El pago tiene un monto que no es v\xc3\xa1lido'), (b'receiver_error', b'El pago tiene un receiver_id que no es v\xc3\xa1lido')], max_length=50, null=True, verbose_name=b'Status payment')),
                ('status_detail', models.CharField(blank=True, choices=[(b'pending', b'El pagador a\xc3\xban no comienza a pagar'), (b'normal', b'El pago fue verificado y cancelado por alg\xc3\xban medio de pago estandar'), (b'marked-paid-by-payer', b'El pagador declar\xc3\xb3 que no pagar\xc3\xa1'), (b'marked-as-abuse', b'El pagador declar\xc3\xb3 que no pagar\xc3\xa1 y que el cobro fue no solicitado'), (b'reversed', b'El pago fue anulado por el comercio, el dinero fue devuelto al pagador')], max_length=50, null=True, verbose_name=b'Status payments detail')),
                ('receipt_url', models.URLField(blank=True, null=True, verbose_name=b'URL comprobante')),
                ('attachment_urls', models.TextField(blank=True, null=True, verbose_name=b'URL archivos adjuntos al pago')),
                ('bank_account_number', models.CharField(blank=True, max_length=400, null=True, verbose_name=b'Bank account number')),
                ('out_of_date_conciliation', models.BooleanField(default=False, verbose_name=b'Pago fuera de la expiracion')),
                ('payment_method', models.CharField(blank=True, choices=[(b'regular_transfer', b'Transferencia normal'), (b'simplified_transfer', b'Transferencia simplificada'), (b'not_available', b'Para un pago marcado como realizado por otro medio por el cobrador')], max_length=50, null=True, verbose_name=b'Status payment')),
            ],
            options={
                'db_table': 'payment',
                'verbose_name': 'Ordenes de compra Khipu',
            },
        ),
    ]
