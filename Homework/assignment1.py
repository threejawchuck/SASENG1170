from Homework.utilities import *

import math

def linear_and_dB_table (**kwargs):
	print "%16s %16s %16s" % ("Name", "Linear", "dB")
	for key in kwargs:
		print "%16s %16s %16s" % (key, kwargs[key], linear_to_dB(kwargs[key]))

def radar_range_eq (Tp, Gt, Gr, F, S, R):
	# convert the frequency into lamba
	Lsquared = math.pow (freq_to_wavelength (F),2)

	# get the 4Pi^3constants
	_K = math.pow (4.0 * ThePi, 3.0)

	# range to the fourth
	Rquad = math.pow (R,4)

	# radar range equation 2.8
	P = (Tp * Gt * Gr * Lsquared * S) / (_K * Rquad)

#	linear_and_dB_table (TransPower=Tp, GainTran=Gt, GranRec=Gr, LambdaSquared=Lsquared, Sigma=S, K=_K, Rquad=Rquad, Power=P)

	return P

def radar_range_eq_dB (Tp_dB, Gt_dB, Gr_dB, F_dB, S_dB, R_dB):
	# convert the frequency into lamba
	L_dB = freq_to_wavelength_dB (F_dB)

	# get the 4Pi^3constants in dB form
	_K_dB = linear_to_dB (math.pow (4.0 * ThePi, 3.0))

	# radar range equation 2.8
	# remember that the linear form has an L^2 and R^4 so we need a 2*L and 4*R in this version
	P_dB = Tp_dB + Gt_dB + Gr_dB + 2*L_dB + S_dB - _K_dB - 4.0*R_dB
	
	return P_dB



def Q1 ():
	"""
	Target received power: Using equation (2.8), determine the single-pulse received power levelfrom a target for a radar system having the following characteristics:Transmitter: 100 kilowatt peakFrequency: 9.4 GHzAntenna Gain: 32 dBTarget RCS: 0 dBsmTarget Range: 50 k
	"""

	Tp = 100000 #Peak Tranmission power in Watts
	F = 9.4e9 # Carrier Frequency in Hertz
	G_dB = 32 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	S_dB = 0 # Target RCS in dBSM
	R = 5e4 # Target Range in Meters

	# convert where necessary to linear
	G = dB_to_linear (G_dB)
	S = dB_to_linear (S_dB)

	# do the math in dB
	power = radar_range_eq (Tp=Tp, Gt=G, Gr=G, F=F, S=S, R=R)

	# convert where necessary to dB
	Tp_dB = linear_to_dB (Tp)
	F_dB = linear_to_dB (F)
	R_dB = linear_to_dB (R)

	# do the math in dB
	power_dB = radar_range_eq_dB (Tp_dB=Tp_dB, Gt_dB=G_dB, Gr_dB=G_dB, F_dB=F_dB, S_dB=S_dB, R_dB=R_dB)

	return power_dB;	