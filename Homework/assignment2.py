from Homework.utilities import *
"""
(Class 3 Slide Presentation - Slide 41) 
Homework 
 POMR Section 9.11 problems 1 to 9
"""

def Q1 ():
	""" Assume an isotropic antenna has been invented that can transmit 10 watts. 
	(a) Assume there is a 20dBm2 target 1km away. What is the power
	    density at this target?
	(b) Assumealargeclutterobject (RCS of 30 dBm2) is located at the same range 
	    as the target but 20 degrees away. Calculatethe power density at the clutter 
	    location. 
	(c) Why would this be a problem for the radarsystem?
	"""
	Pt = 10.0 # Transmit power in Watts
	Pt_dB = linear_to_dB (Pt) # Transmit power in dB Watts

	# (a)
	Trcs_dB = 20 # Target RCS in db meters squared

	# power density is the power divided by the surface area of the sphere whose
	# radius is defined by the transmitter and the targer

	radius = 1e3 # radius in meters
	surface_area_of_sphere_dB = linear_to_dB (4.0 * ThePi * radius * radius)

	# that's not a very big number!
	# also not that the size of the target has nothing to do with this
	# this is a power density, nothing more.  we aren't tryingt to find out
	# how much energy is incident on the target
	power_density_dB = Pt_dB - surface_area_of_sphere_dB

	#(b)
	# hey mcfly!  it's an isotropic array!  no directivity
	# answer is the same as problem (a)

	#(c)
	# this is a problem because 
	## you have to put out a lot of power to get any power on target
	## as indicated by parts (a) and (b) you can't distinguish target
	## returns from clutter returns using angular resolution (though you might
	## be able to do so with doppler).  in other words, you can't point it
	## so everything get radiated and you hear everything too

	return power_density_dB, power_density_dB, 42

def Q2 ():
	"""Consider a radar antenna that has an aperture 3.0 m high by 3.5 m wide. 
	Imagine a 10 GHz plane wave arriving from an angle of elevation=0 degrees and 
	azimuth=15 degrees. 
	(a) What is the total phase gradient across the aperture surface? 
	(b) What if the azimuth angle is changed to 60 degrees
	"""
	freq = 10e9
	wavelength = freq_to_wavelength (freq)

	# (a)
	# this is basically a right triangle with the hyp of 3.5m and a 15 degree 
	# angle.  we are trying to figure out the length of the side opposite the
	# 15 degree angle.  to convert this to phase, we need to know the wavelength.
	# you get 2pi radians of phase per wave length so multiply by 2Pi/lambda
	total_phase_gradient_a = 3.5 * math.sin (15 * ThePi / 180.0) * (2.0 * ThePi / wavelength)

	# (b)
	# same thing with a different angle
	total_phase_gradient_b = 3.5 * math.sin (60 * ThePi / 180.0) * (2.0 * ThePi / wavelength)


	return total_phase_gradient_a, total_phase_gradient_b


def Q3 ():
	return -1

def Q4 ():
	return -1

def Q5 ():
	return -1

def Q6 ():
	return -1

def Q7 ():
	return -1

def Q8 ():
	return -1

def Q9 ():
	return -1
