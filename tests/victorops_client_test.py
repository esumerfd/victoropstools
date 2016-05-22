import unittest

from victorops.victorops_client import VictorOpsClient

class VictorOpsClientTest(unittest.TestCase):

    def test_get_incidents(self):
        ops = VictorOpsClient()
        self.assertEqual("incidents", ops.get_incidents())
 
if __name__ == "__main__":
        unittest.main()
