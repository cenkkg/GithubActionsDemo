import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from utils import get_daily_data, get_weekly_data

class UnitTest(unittest.TestCase):
    def testApiCallDailyData(self):
        self.assertIsNotNone(get_daily_data(),"Api call return no values")

    def testApiCallWeeklyData(self):
        self.assertIsNotNone(get_weekly_data(),"Api call return no values")
   
if __name__ == '__main__':
   unittest.main()