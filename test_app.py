import unittest

from app import dbconn


class TestdbConn(unittest.TestCase):
    def test_dbconn(self):
        res = dbconn()
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
