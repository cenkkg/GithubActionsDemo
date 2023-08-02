import unittest
from unit import UnitTest

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
    test_suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(test_suite)

    if test_result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed!")
