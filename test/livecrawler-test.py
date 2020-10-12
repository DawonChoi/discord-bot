import unittest
import sys
sys.path.append("..")

from livecrawler import *

test_summoner = '국밥 이선생'
class TestExampleMethods(unittest.TestCase):

    def test_history(self):
        self.assertEqual(10, 10)

    def test_rating(self):
        self.assertTrue('A'.isupper())
        self.assertFalse('a'.isupper())

    def test_kda(self):
        self.assertTrue(1, 1)


unittest.main()
