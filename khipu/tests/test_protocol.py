import mock
import requests

from django.test import TestCase

from ..exceptions import KhipuError
from ..services.protocol import KhipuProtocol


class TestKhipuProtocol(TestCase):

    def test_request(self):
        # Testing Requests con status code != 200
        with mock.patch.object(requests, 'request') as mock_requests,\
                mock.patch.object(KhipuProtocol, 'get_url_service', return_value=''),\
                self.assertRaises(KhipuError):
            mock_requests.return_value.status_code = 403
            kp = KhipuProtocol(receiver_id=111, secret='11212', service_name='Testing')
            kp.request()

            mock_requests.return_value.status_code = 500
            kp = KhipuProtocol(receiver_id=111, secret='11212', service_name='Testing')
            kp.request()