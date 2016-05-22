class Incidents(object):
    global VICTOROPS_API_ID
    global VICTOROPS_API_KEY

    VICTOROPS_API_ID = 'VO API ID'
    VICTOROPS_API_KEY = 'VO API KEY'
        
    def url(self):
        return '''https://api.victorops.com/{0}'''.format('api-public/v1/incidents')

    def headers(self):
        return {
            'X-VO-Api-Id' : VICTOROPS_API_ID,
            'X-VO-Api-Key' : VICTOROPS_API_KEY
        }

