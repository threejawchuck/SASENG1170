
import Homework.assignment2 as hw2
import Homework.utilities as utilities
import unittest

# this is a class that has a bunch of tests
class test_assignment2 (unittest.TestCase):
	"""

	"""
	def setUp (self):
		self.tolerance = 4
		pass

	def tearDown (self):
		pass

	def test_Q1 (self):
		a,b,c = hw2.Q1()
		self.assertAlmostEqual(-60.9921, a, self.tolerance)
		self.assertAlmostEqual(-60.9921, b, self.tolerance)
		self.assertAlmostEqual(42, c, self.tolerance)
		pass		

	def test_Q2 (self):
		a,b = hw2.Q2()
		self.assertAlmostEqual(189.7242692, a, self.tolerance)
		self.assertAlmostEqual(634.8297775, b, self.tolerance)
		pass		

	def test_Q3 (self):
		self.assertAlmostEqual(-1, hw2.Q3(), self.tolerance)
		pass		

	def test_Q3 (self):
		self.assertAlmostEqual(-1, hw2.Q4(), self.tolerance)
		pass		

	def test_Q4 (self):
		self.assertAlmostEqual(-1, hw2.Q4(), self.tolerance)
		pass		

	def test_Q5 (self):
		self.assertAlmostEqual(-1, hw2.Q5(), self.tolerance)
		pass		

	def test_Q6 (self):
		self.assertAlmostEqual(-1, hw2.Q6(), self.tolerance)
		pass		

	def test_Q7 (self):
		self.assertAlmostEqual(-1, hw2.Q7(), self.tolerance)
		pass		

	def test_Q8 (self):
		self.assertAlmostEqual(-1, hw2.Q8(), self.tolerance)
		pass		

	def test_Q9 (self):
		self.assertAlmostEqual(-1, hw2.Q9(), self.tolerance)
		pass		

# take every test in this class and use it to define a suite
suite = unittest.TestLoader().loadTestsFromTestCase(test_assignment2)

# now register this test suite with the test runner
unittest.TextTestRunner(verbosity=2).run(suite)
