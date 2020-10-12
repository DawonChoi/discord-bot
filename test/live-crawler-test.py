import unittest

class TestExampleMethods(unittest.TestCase):

    def test_one(self):
        self.assertEqual(10, 10)

    def test_two(self):
        self.assertTrue('A'.isupper())
        self.assertFalse('a'.isupper())


if __name__ == '__main__':
    unittest.main()
