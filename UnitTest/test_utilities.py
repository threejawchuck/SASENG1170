import Homework.utilities as u

import unittest

# this is a class that has a bunch of tests
class test_utilities (unittest.TestCase):
	def setUp (self):
		pass

	def tearDown (self):
		pass

	def test_linear_to_dB (self):

		# 1 is 0 dB.  remember that log10 of 1 is zero
		self.assertEqual(0.0, u.linear_to_dB(1.0))

		# factor of 2x is really close to 3dB
		self.assertAlmostEqual(3.0, u.linear_to_dB(2.0), 1)		

		# factor of 10x is 10dB
		self.assertEqual(10.0, u.linear_to_dB(10.0))		

		# factor of .10x is -10dB
		self.assertEqual(-10.0, u.linear_to_dB(.1))		

		# log of multiplication is addition
		a = 12321321.000
		b = 675434.12313
		self.assertEqual (u.linear_to_dB(a*b), u.linear_to_dB(a) + u.linear_to_dB(b))

		# log of division is subtraction
		self.assertAlmostEqual (u.linear_to_dB(a/b), u.linear_to_dB(a) - u.linear_to_dB(b), 10)


	def test_dB_to_linear (self):

		# log10 of 1 is zero
		self.assertEqual(1.0, u.dB_to_linear(0.0))

		# factor of 2x is really close to 3dB
		self.assertAlmostEqual(2.0, u.dB_to_linear(3), 2)		

		# factor of 10x is 10dB
		self.assertEqual(10.0, u.dB_to_linear(10))		

		# factor of .10x is -10dB
		self.assertEqual(.1, u.dB_to_linear(-10))		

		# log of multiplication is addition
		a = 1.23412
		b = 3.234234
		self.assertAlmostEqual (u.dB_to_linear(a+b), u.dB_to_linear(a) * u.dB_to_linear(b), 10)

		# log of division is subtraction
		self.assertAlmostEqual (u.dB_to_linear(a-b), u.dB_to_linear(a) / u.dB_to_linear(b), 10)

	def test_freq_to_wavelength (self):
		# a frequency (in Hz) exactly equal to the speed of light (in m/s) should give me a 1 meter wavelenght
		self.assertEqual(1, u.freq_to_wavelength(u.TheSpeedOfLight))

	def test_freq_to_wavelength_dB (self):
		# pick some crazy freq
		f = 9.236793472e9

		# get the linear wavelength 
		l = u.freq_to_wavelength(f)

		# convert that to dB
		l_dB = u.linear_to_dB(l)

		# convert the freq to dB as well
		f_dB = u.linear_to_dB(f)

		# now run the dB equation
		# not great, but at least it's consistent witht eh linear version
		self.assertAlmostEqual (l_dB, u.freq_to_wavelength_dB (f_dB), 10)


# take every test in this class and use it to define a suite
suite = unittest.TestLoader().loadTestsFromTestCase(test_utilities)

# now register this test suite with the test runner
unittest.TextTestRunner(verbosity=2).run(suite)
