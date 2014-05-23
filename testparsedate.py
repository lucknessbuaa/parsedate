import unittest
import datetime
from parseDate import parseDatetime

class testParseDate(unittest.TestCase):

	def testToday(self):
		date1=datetime.datetime.today().replace(hour=0,minute=0,second=0,microsecond=0)
		date2=parseDatetime('today')
		self.assertEqual(date1,date2)

	def testYestoday(self):
		date1=datetime.datetime.today().replace(hour=0,minute=0,second=0,microsecond=0)-datetime.timedelta(days=1)
		date2=parseDatetime('yestoday')
		self.assertEqual(date1,date2)

	def testTime(self):
		date1=datetime.datetime.strptime('2013-09-09','%Y-%m-%d')
		date2=parseDatetime('2013-09-09')
		self.assertEqual(date1,date2)

if __name__=='__main__':
	unittest.main()
