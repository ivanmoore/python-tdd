import unittest

from app.sample import Thing


class SampleTest(unittest.TestCase):
    def test_returns_correct_result(self):
        t = Thing()
        result = t.increment(1)
        self.assertEqual(2, result)

    def test_can_only_increment_int(self):
        self.assertRaises(ValueError, Thing().increment, 1.0)
