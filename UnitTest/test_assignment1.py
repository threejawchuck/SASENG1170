
import Homework.assignment1 as hw1
import Homework.utilities as utilities
import unittest

# this is a class that has a bunch of tests
class test_assignment1 (unittest.TestCase):
	def setUp (self):
		self.tolerance = 4
		pass

	def tearDown (self):
		pass

	def test_Q1 (self):
		self.assertAlmostEqual(utilities.linear_to_dB(2.06290e-14), hw1.Q1(), self.tolerance)
		pass		

	def test_Q2 (self):
		self.assertAlmostEqual(utilities.linear_to_dB(7.45207e-15), hw1.Q2(), self.tolerance)
		pass		

	def test_Q3 (self):
		self.assertAlmostEqual(4.42200, hw1.Q3(), self.tolerance)
		pass		

	def test_Q4 (self):
		(a1,a2,a3,a4) = hw1.Q4()
		self.assertAlmostEqual(-129.1691278, a1, self.tolerance)
		self.assertAlmostEqual(-129.1691278, a2, self.tolerance)
		self.assertAlmostEqual(-118.6497314, a3, self.tolerance)
		self.assertAlmostEqual(-119.1691278, a4, self.tolerance)
		pass		

	def test_Q5 (self):
		(a1,a2,a3,a4) = hw1.Q5()
		self.assertAlmostEqual(1.6081013, a1, self.tolerance)
		self.assertAlmostEqual(1.6081013, a2, self.tolerance)
		self.assertAlmostEqual(12.6274978, a3, self.tolerance)
		self.assertAlmostEqual(11.6081013, a4, self.tolerance)
		pass		

	def test_Q6_linear (self):
		a = hw1.Q6_linear()
		self.assertAlmostEqual(3.317494E-01, a[0], self.tolerance)
		self.assertAlmostEqual(3.317494E-01, a[1], self.tolerance)
		self.assertAlmostEqual(4.195172E+00, a[2], self.tolerance)
		self.assertAlmostEqual(3.317494E+00, a[3], self.tolerance)
		pass		

	def test_Q6 (self):
		a = hw1.Q6()
		self.assertAlmostEqual(-4.79190, a[0], self.tolerance)
		self.assertAlmostEqual(-4.79190, a[1], self.tolerance)
		self.assertAlmostEqual(6.22750, a[2], self.tolerance)
		self.assertAlmostEqual(5.20810, a[3], self.tolerance)

		#convince ourselves that the linear and dB solutions are consistent	
		a = hw1.Q6_linear()
		self.assertAlmostEqual(-4.79190, utilities.linear_to_dB(a[0]), self.tolerance)
		self.assertAlmostEqual(-4.79190, utilities.linear_to_dB(a[1]), self.tolerance)
		self.assertAlmostEqual(6.22750, utilities.linear_to_dB(a[2]), self.tolerance)
		self.assertAlmostEqual(5.20810, utilities.linear_to_dB(a[3]), self.tolerance)
		pass

	def test_Q7 (self):
		a = hw1.Q7()
		self.assertAlmostEqual(-9.1118986852, a[0], self.tolerance)
		self.assertAlmostEqual(-9.1118986852, a[1], self.tolerance)
		self.assertAlmostEqual(1.9074977599, a[2], self.tolerance)
		self.assertAlmostEqual(0.8881013148, a[3], self.tolerance)


# take every test in this class and use it to define a suite
suite = unittest.TestLoader().loadTestsFromTestCase(test_assignment1)

# now register this test suite with the test runner
unittest.TextTestRunner(verbosity=2).run(suite)
