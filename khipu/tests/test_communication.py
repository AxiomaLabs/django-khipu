from django.conf import settings
from django.test import TestCase

from ..communication import Khipu
from ..exceptions import KhipuError


class TestCommunication(TestCase):

    def test_service(self):
        # Testing that the service does not exist
        with self.assertRaises(KhipuError):
            khipu = Khipu()
            khipu.service('estoesuntesting')

        # Testing auth Does not exist
        with self.assertRaises(KhipuError):
            settings.KHIPU_RECEIVER_ID = None
            khipu = Khipu()
            khipu.service('GetBanks')

        settings.KHIPU_RECEIVER_ID = '148653'

        # Testing result ok
        khipu = Khipu()
        result = khipu.service('GetBanks')
        self.assertTrue('banks' in result)

        # Testing boolean fields in CreatePaymentURL service
        khipu = Khipu()
        result = khipu.service('CreatePaymentURL', **{
            'subject': 'Testing subject',
            'currency': 'CLP',
            'amount': '3000',
            'payer_name': True
        })
        self.assertTrue('payment_id' in result)

        # Testing GetPayment service, the key does not exist
        with self.assertRaises(KhipuError):
            khipu = Khipu()
            result = khipu.service('GetPaymentInfo', **{'notification_token': 'testing_token'})
            self.assertTrue(result.status_code == 400)