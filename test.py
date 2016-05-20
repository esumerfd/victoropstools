import unittest
import mock

from pull_incidents_from_victor_ops import PullIncidents

class TestPullIncidents(unittest.TestCase):

    def setUp(self):

        self.pull_incidents_from_victor_ops = PullIncidents()

    def test_build_http_headers(self):
        """
        Test building the headers
        """
        voapiid = 'fake-api-id'
        voapikey = 'fake-api-key'
        vo_headers = {
            'X-VO-Api-Id' : voapiid,
            'X-VO-Api-Key' : voapikey
            }

        y = self.pull_incidents_from_victor_ops.build_http_headers(voapiid, voapikey)
        self.assertEqual(y, vo_headers)

    @mock.patch('pull_incidents_from_victor_ops.requests.get')
    def test_get_api_json(self, mock_get_api_json):
        """
        Test a response with a mocked api
        """
        mock_response = mock.Mock()
        """
        load expected json response from file
        """
        f = open('tests/resources/mocked_api_incidents.json', 'r')
        myresponse = f.read()
        f.close()
        MY_HTTP_CODE = '200'
        mock_get_api_json.response.text.return_value = myresponse
        mock_get_api_json.response.status_code.return_value = MY_HTTP_CODE
        APIE = 'api-public/v1/incidents'
        ENDPOINT = '''https://api.victorops.com/{0}'''.format(APIE)
        voapiid = 'fake-api-id'
        voapikey = 'fake-api-key'
        VOH = {
            'X-VO-Api-Id' : voapiid,
            'X-VO-Api-Key' : voapikey
            }

        expected_rt, expected_c = self.pull_incidents_from_victor_ops.get_api_json(vo_headers=VOH,
                api_endpoint=APIE)

        mock_get_api_json.assert_called_once_with(ENDPOINT,
                headers=VOH)
        self.assertEqual(1, mock_get_api_json.call_count)
        #self.assertEqual(str(expected_rt), myresponse)
        imyt = type(expected_c)
        print imyt

if __name__ == "__main__":
        unittest.main()
