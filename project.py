from unittest import TestCase

__author__ = 'Mark'


def adder(arg1, arg2):
    return arg1 + arg2


class Test(TestCase):
    def test_adder(self):
        self.assertEqual(adder(5, 4), 9)


