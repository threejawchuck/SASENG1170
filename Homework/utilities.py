import math

def linear_to_dB (x):
	return 10.0 * math.log10(x)

def dB_to_linear (x):
	#return 10.0^(x/10.0)
	return math.pow (10.0, x/10.0)

def freq_to_wavelength (f):
	""" Converts LINEAR frequency into LINEAR wavelenght
	"""
	return TheSpeedOfLight / f;

def freq_to_wavelength_dB (F_dB):
	""" Converts dB frequency into dB wavelenght
	"""
	return TheSpeedOfLight_dB - F_dB;

# Global Values
ThePi = 3.14159265359
TheSpeedOfLight = 299792458.0 # in meters per second
TheSpeedOfLight_dB = linear_to_dB (TheSpeedOfLight)
TheBoltzmanConstant = 1.38064852e-23 # in m^2 * kg * s^-2 * K^-1
TheBoltzmanConstant_dB = linear_to_dB (TheBoltzmanConstant)