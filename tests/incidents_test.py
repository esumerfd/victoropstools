import unittest

from victorops.incidents import Incidents

class IncidentsTest(unittest.TestCase):

    def test_get_incidents(self):
        request = Incidents()

        self.assertTrue("api-public/v1/incidents" in request.url())
        self.assertTrue("X-VO-Api-Id" in request.headers())
        self.assertTrue("X-VO-Api-Key" in request.headers())
 
if __name__ == "__main__":
        unittest.main()
