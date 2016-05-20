#!/bin/env python2.7
"""
This is to pull Victor Ops Alert details assoicated with a specific alert number.
https://portal.victorops.com/public/api-docs.html
"""

import json
import requests

class PullIncidents(object):
    """
    This only exists as a class for mock and unittest
    """

    def build_http_headers(self, victorops_api_id, victorops_api_key):
        """ Build http headers for Victor Ops API endpoint"""
        myvictoropsheaders = {
            'X-VO-Api-Id' : victorops_api_id,
            'X-VO-Api-Key' : victorops_api_key
            }
        return myvictoropsheaders
 
    def get_api_json(self, vo_headers, api_endpoint):
        """ get json from endpoint """
        try:
            apiurl = '''https://api.victorops.com/{0}'''.format(api_endpoint)
            response = requests.get(apiurl, headers=vo_headers)
            return response.text, response.status_code
        except requests.exceptions.ConnectionError, err:
            error = '''Connection error, error was : {0}'''.format(err)
            raise SystemExit(error)
        except Exception, err:
            post_error = '''Error posting to VictorOps {0} \n\nresponse was {1}\n
            HTTP code was {2}\n\n'''.format(
                err,
                response.text,
                response.status_code)
        raise SystemExit(post_error)


if __name__ == "__main__":
    VICTOROPS_API_ID = 'VO API ID'
    VICTOROPS_API_KEY = 'VO API KEY'
    VICTOROPS_API_ENDPOINT_ALERTS = 'api-public/v1/alerts/'
    VICTOROPS_API_ENDPOINT_INCIDENTS = 'api-public/v1/incidents'
    try:
        REPORTS = PullIncidents()
        VICTOR_OPS_HEADERS = REPORTS.build_http_headers(VICTOROPS_API_ID, VICTOROPS_API_KEY)
        MY_INCIDENTS, MYC = REPORTS.get_api_json(VICTOR_OPS_HEADERS,
                                                 VICTOROPS_API_ENDPOINT_INCIDENTS)
        JSON_INCIDENTS = json.dumps(MY_INCIDENTS)
        print MY_INCIDENTS
    except Exception, err:
        print '''something broke {0}'''.format(err)

