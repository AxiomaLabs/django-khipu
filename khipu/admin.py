from django.contrib import admin

from .constants import PAYMENT_STATUS_DETAIL
from .models import Payment


class KhipuAdmin(admin.ModelAdmin):
    """
    Modelo de administracion de Khipu
    """
    list_display = ("payment_id", "transaction_id", "get_status", "subject", "amount")
    search_fields = ["payment_id", "transaction_id"]
    list_per_page = 100

    readonly_fields = [
        'payment_id', 'notification_token', 'status', 'receiver_id'
    ]

    def get_status(self, instance):
        return dict(PAYMENT_STATUS_DETAIL)[instance.status_detail] if instance.status_detail else 'Sin status'
    get_status.short_description = 'Estatus'

admin.site.register(Payment, KhipuAdmin)
