# Name : Utkarsh Dubey
# Roll No : 2019213
# Group : 6

import unittest
from a1 import changeBase

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_change_base(self):
		self.assertEqual(changeBase(1, "INR", "GBP", "2014-10-25"),0.01018280504195388 )
		self.assertEqual(changeBase(1, "MYR", "USD", "2018-12-22"),0.23974962191228366 )
		self.assertEqual(changeBase(1, "CAD", "KRW", "2019-02-28"), 851.6620130301822 )
		self.assertAlmostEqual(changeBase(1, "CAD", "KRW", "2019-02-28"), 851.6, delta = 0.1)
		self.assertEqual(changeBase(1, "SGD", "THB", "2017-04-25"),24.711272247857618 )
		self.assertEqual(changeBase(1, "JPY", "USD", "2019-09-09"), 0.009349207694263197 )
		self.assertAlmostEqual(changeBase(1, "JPY", "USD", "2019-09-09"), 0.01, delta = 0.1)
		
		# these are just sample values. You have to add testcases (and edit these) for various dates.
		# (don't use the current date as the json would keep changing every 4 minutes)
		# you have to hard-code the 2nd parameter of assertEquals by calculating it manually
		# on a particular date and checking whether your changeBase function returns the same
		# value or not.



if __name__=='__main__':
	unittest.main()