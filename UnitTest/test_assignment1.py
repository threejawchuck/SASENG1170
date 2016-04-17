
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




# take every test in this class and use it to define a suite
suite = unittest.TestLoader().loadTestsFromTestCase(test_assignment1)

# now register this test suite with the test runner
unittest.TextTestRunner(verbosity=2).run(suite)
