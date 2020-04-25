import unittest
from my_test_classes import A
from my_test_classes import B
from my_test_classes import C


def suite():
    suite = unittest.TestSuite()
    suite.addTest(A('test_A1'))
    suite.addTest(A('test_A2'))
    suite.addTest(B('test_B2'))
    suite.addTest(C('test_C3'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
