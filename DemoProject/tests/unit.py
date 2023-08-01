import unittest
from utils import get_daily_data, get_weekly_data

class UnitTest(unittest.TestCase):
    def testApiCallDailyData(self):
        self.assertIsNotNone(get_daily_data(),"Api call return no values")

    def testApiCallWeeklyData(self):
        self.assertIsNotNone(get_weekly_data(),"Api call return no values")
   
if __name__ == '__main__':
   unittest.main()