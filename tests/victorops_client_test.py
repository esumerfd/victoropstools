import unittest
import mock

import json
import requests

from victorops.victorops_client import VictorOpsClient

class VictorOpsClientTest(unittest.TestCase):
    incidents_response = '''{
        "incidents": [
          {
            "alertCount": 975,
            "currentPhase": "RESOLVED",
            "entityDisplayName": "lamp::Certifier",
            "entityId": "lamp::Certifier",
            "entityState": "OK",
            "entityType": "SERVICE",
            "host": "mia-ds-2",
            "incidentNumber": "787",
            "lastAlertId": "1bf23700-1214-4e23-a885-9266c2ae6666",
            "lastAlertTime": "2016-05-18T18:45:53Z",
            "service": "lamp::Certifier",
            "startTime": "2016-05-18T11:30:04Z",
            "pagedTeams": [
              "everyone"
            ],
            "pagedUsers": [
              "cgomez",
              "jfidalgo",
              "mpividal",
              "mwalter"
            ],
           "transitions": [
             {
               "name": "ACKED",
               "at": "2016-05-18T11:45:42Z",
               "message": "I DID IT"
             },
             {
               "name": "RESOLVED",
               "at": "2016-05-18T18:45:53Z",
               "by": "lcerezo",
               "manually": true
             }
           ]
         }
       ]
    }'''

    @mock.patch('requests.post')
    def test_retrieve_incident_data(self, mock_post):
        # Define the response from the jsno() method.
        mock_response = mock.Mock()
        mock_response.status_code = requests.codes.ok
        mock_response.json.return_value = json.loads(self.incidents_response)

        # Tell the post method to return the response object that has the json in it.
        mock_post.return_value = mock_response
        
        ops = VictorOpsClient()
        data, status_code = ops.get_incidents()

        self.assertEqual(975, data["incidents"][0]["alertCount"])
        self.assertEqual(requests.codes.ok, status_code)

    @mock.patch('requests.post')
    def test_leave_data_as_empty_dict_when_status_code_not_200(self, mock_post):
        # Define the response from the jsno() method.
        mock_response = mock.Mock()
        mock_response.status_code = requests.codes.unauthorized
        mock_response.json.return_value = json.loads(self.incidents_response)

        # Tell the post method to return the response object that has the json in it.
        mock_post.return_value = mock_response
        
        ops = VictorOpsClient()
        data, status_code = ops.get_incidents()

        self.assertEqual("", data)
        self.assertEqual(requests.codes.unauthorized, status_code)
 
if __name__ == "__main__":
        unittest.main()
