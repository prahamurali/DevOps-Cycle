import unittest

from app import dbconn


class TestdbConn(unittest.TestCase):
    def test_dbconn(self):
        res = dbconn()
        self.assertEqual(res, True)
        return "Test Passed"


if __name__ == '__main__':
    unittest.main()
