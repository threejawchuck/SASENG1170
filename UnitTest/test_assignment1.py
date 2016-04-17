
import Homework.assignment1 as hw1
import Homework.utilities as utilities
import unittest

# this is a class that has a bunch of tests
class test_assignment1 (unittest.TestCase):
	def setUp (self):
		pass

	def tearDown (self):
		pass

	def test_Q1 (self):
		self.assertAlmostEqual(utilities.linear_to_dB(2.06e-14), hw1.Q1(),3)
		pass		

	def test_Q2 (self):
		self.assertAlmostEqual(utilities.linear_to_dB(7.45e-15), hw1.Q2(),0)
		pass		

	def test_Q3 (self):
		self.assertAlmostEqual(4.42, hw1.Q3(),0)
		pass		

	def test_Q4 (self):
		(a1,a2,a3,a4) = hw1.Q4()
		self.assertAlmostEqual(-129.17, a1,1)
		self.assertAlmostEqual(-129.17, a2,1)
		self.assertAlmostEqual(-118.65, a3,1)
		self.assertAlmostEqual(-119.17, a4,1)
		pass		


# take every test in this class and use it to define a suite
suite = unittest.TestLoader().loadTestsFromTestCase(test_assignment1)

# now register this test suite with the test runner
unittest.TextTestRunner(verbosity=2).run(suite)
