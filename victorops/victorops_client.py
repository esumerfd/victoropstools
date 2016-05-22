import json
import requests

from victorops.incidents import Incidents

class VictorOpsClient(object):
    def get_incidents(self):
        incidents = Incidents()

        response = requests.post(incidents.url, data=incidents.headers)

        data = ""
        if response.status_code == requests.codes.ok:
            data = response.json()

        return data, response.status_code
