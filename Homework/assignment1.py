from Homework.utilities import *

import math

def linear_and_dB_table (**kwargs):
	print "%16s %16s %16s" % ("Name", "Linear", "dB")
	for key in kwargs:
		print "%16s %16s %16s" % (key, kwargs[key], linear_to_dB(kwargs[key]))

def radar_range_eq (Tp, Gt, Gr, L, S, R):
	# convert the frequency into lamba
	Lsquared = math.pow (L,2)

	# get the 4Pi^3constants
	_K = math.pow (4.0 * ThePi, 3.0)

	# range to the fourth
	Rquad = math.pow (R,4)

	# radar range equation 2.8
	P = (Tp * Gt * Gr * Lsquared * S) / (_K * Rquad)

#	linear_and_dB_table (TransPower=Tp, GainTran=Gt, GranRec=Gr, LambdaSquared=Lsquared, Sigma=S, K=_K, Rquad=Rquad, Power=P)

	return P

def radar_range_eq_dB (Tp_dB, Gt_dB, Gr_dB, L_dB, S_dB, R_dB):

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
	L = freq_to_wavelength(9.4e9) # Converted from Carrier Frequency in Hertz to avoid confusion with F the noise figure
	G_dB = 32 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	S_dB = 0 # Target RCS in dBSM
	R = 5e4 # Target Range in Meters

	# convert where necessary to linear
	G = dB_to_linear (G_dB)
	S = dB_to_linear (S_dB)

	# do the math in dB
	power = radar_range_eq (Tp=Tp, Gt=G, Gr=G, L=L, S=S, R=R)

	# convert where necessary to dB
	Tp_dB = linear_to_dB (Tp)
	L_dB = linear_to_dB (L)
	R_dB = linear_to_dB (R)

	# do the math in dB
	power_dB = radar_range_eq_dB (Tp_dB=Tp_dB, Gt_dB=G_dB, Gr_dB=G_dB, L_dB=L_dB, S_dB=S_dB, R_dB=R_dB)

	return power_dB;	

def receiver_noise_power_dB (F_dB, B_dB):
	# equation 2.10
	T = 290 # The Standard Temperature in Kelvin
	T_dB = linear_to_dB (T)

	return TheBoltzmanConstant_dB + T_dB + F_dB + B_dB

def receiver_noise_power (F, B):
	F_dB = linear_to_dB(F)
	B_dB = linear_to_dB(B) 

	return dB_to_linear (receiver_noise_power_dB (F_dB, B_dB))


def Q2 ():
	"""
	Using equation (2.10), determine the receiver noise power (in dBm) for a receiver having anoise fgure of 2.7 dB and an instantaneous bandwidth of 1 MHz
	"""
	# given
	F_dB=2.7 # noise figure in dB
	B = 1e6 # Instantaneous Bandwidth in Hz

	B_dB = linear_to_dB(B)

	# do the math in dB
	power_dB = receiver_noise_power_dB (F_dB, B_dB)

	return power_dB

def single_pulse_SNR_dB (Tp_dB, Gt_dB, Gr_dB, L_dB, S_dB, R_dB, F_dB, B_dB):

	return radar_range_eq_dB (Tp_dB, Gt_dB, Gr_dB, L_dB, S_dB, R_dB) - receiver_noise_power_dB (F_dB, B_dB)

def Q3():
	# given
	Tp = 100000 #Peak Tranmission power in Watts
	L = freq_to_wavelength(9.4e9) # Converted from Carrier Frequency in Hertz to avoid confusion with F the noise figure
	G_dB = 32 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	S_dB = 0 # Target RCS in dBSM
	R = 5e4 # Target Range in Meters
	F_dB=2.7 # noise figure in dB
	B = 1e6 # Instantaneous Bandwidth in Hz

	# convert where necessary to dB
	Tp_dB = linear_to_dB (Tp)
	L_dB = linear_to_dB (L)
	R_dB = linear_to_dB (R)
	B_dB = linear_to_dB(B)

	return single_pulse_SNR_dB(Tp_dB, G_dB, G_dB, L_dB, S_dB, R_dB, F_dB, B_dB)

def Q4 ():

	# global given
	S_dB = linear_to_dB (1) # Target RCS in dBSM
	R_dB = linear_to_dB (3.6e4) # Target Range in dBMeters

	#radar 1
	Tp_dB = linear_to_dB (2.5e4)  #Peak Tranmission power in dB Watts
	G_dB = 36 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	L_dB = linear_to_dB (freq_to_wavelength(9.4e9)) # Converted from Carrier Frequency in Hertz to avoid confusion with F the noise figure
	a1 = radar_range_eq_dB (Tp_dB=Tp_dB, Gt_dB=G_dB, Gr_dB=G_dB, L_dB=L_dB, S_dB=S_dB, R_dB=R_dB)

	#radar 2
	Tp_dB = linear_to_dB (2.5e5)  #Peak Tranmission power in dB Watts
	G_dB = 31 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	L_dB = linear_to_dB (freq_to_wavelength(9.4e9)) # Converted from Carrier Frequency in Hertz to avoid confusion with F the noise figure
	a2 = radar_range_eq_dB (Tp_dB=Tp_dB, Gt_dB=G_dB, Gr_dB=G_dB, L_dB=L_dB, S_dB=S_dB, R_dB=R_dB)

	#radar 3
	Tp_dB = linear_to_dB (2.5e5)  #Peak Tranmission power in dB Watts
	G_dB = 31 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	L_dB = linear_to_dB (freq_to_wavelength(2.8e9)) # Converted from Carrier Frequency in Hertz to avoid confusion with F the noise figure
	a3 = radar_range_eq_dB (Tp_dB=Tp_dB, Gt_dB=G_dB, Gr_dB=G_dB, L_dB=L_dB, S_dB=S_dB, R_dB=R_dB)

	#radar 4
	Tp_dB = linear_to_dB (2.5e5)  #Peak Tranmission power in dB Watts
	G_dB = 36 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	L_dB = linear_to_dB (freq_to_wavelength(9.4e9)) # Converted from Carrier Frequency in Hertz to avoid confusion with F the noise figure
	a4 = radar_range_eq_dB (Tp_dB=Tp_dB, Gt_dB=G_dB, Gr_dB=G_dB, L_dB=L_dB, S_dB=S_dB, R_dB=R_dB)

	return (a1, a2, a3, a4);

def Q5 ():
	# global given
	S_dB = linear_to_dB (1) # Target RCS in dBSM
	R_dB = linear_to_dB (3.6e4) # Target Range in dBMeters
	B_dB = linear_to_dB (10e6) # Bandwidth in dBHz
	F_dB = [3.2, 3.2, 2.7, 3.2] # Noise figure for the four radars GHz system

	#radar 1
	Tp_dB = linear_to_dB (2.5e4)  #Peak Tranmission power in dB Watts
	G_dB = 36 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	L_dB = linear_to_dB (freq_to_wavelength(9.4e9)) # Converted from Carrier Frequency in Hertz to avoid confusion with F the noise figure
	a1 = single_pulse_SNR_dB(Tp_dB, G_dB, G_dB, L_dB, S_dB, R_dB, F_dB[0], B_dB)

	#radar 2
	Tp_dB = linear_to_dB (2.5e5)  #Peak Tranmission power in dB Watts
	G_dB = 31 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	L_dB = linear_to_dB (freq_to_wavelength(9.4e9)) # Converted from Carrier Frequency in Hertz to avoid confusion with F the noise figure
	a2 = single_pulse_SNR_dB(Tp_dB, G_dB, G_dB, L_dB, S_dB, R_dB, F_dB[1], B_dB)

	#radar 3
	Tp_dB = linear_to_dB (2.5e5)  #Peak Tranmission power in dB Watts
	G_dB = 31 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	L_dB = linear_to_dB (freq_to_wavelength(2.8e9)) # Converted from Carrier Frequency in Hertz to avoid confusion with F the noise figure
	a3 = single_pulse_SNR_dB(Tp_dB, G_dB, G_dB, L_dB, S_dB, R_dB, F_dB[2], B_dB)

	#radar 4
	Tp_dB = linear_to_dB (2.5e5)  #Peak Tranmission power in dB Watts
	G_dB = 36 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	L_dB = linear_to_dB (freq_to_wavelength(9.4e9)) # Converted from Carrier Frequency in Hertz to avoid confusion with F the noise figure
	a4 = single_pulse_SNR_dB(Tp_dB, G_dB, G_dB, L_dB, S_dB, R_dB, F_dB[3], B_dB)

	return [a1, a2, a3, a4];


def Q6_linear ():
	# the text is recommending that the calculation be done in linear though i can't image why it matters.  
	# global given
	S_dB = linear_to_dB (1) # Target RCS in dBSM
	R_dB = linear_to_dB (3.6e4) # Target Range in dBMeters
	B_dB = linear_to_dB (10e6) # Bandwidth in dBHz
	F_dB = [3.2, 3.2, 2.7, 3.2] # Noise figure for the four radars GHz system

	#radar 1
	Tp_dB = linear_to_dB (2.5e4)  #Peak Tranmission power in dB Watts
	G_dB = 36 # Antenna Gain in dB, used for both transmission and receiving (i.e. monostatic)
	L_dB = linear_to_dB (freq_to_wavelength(9.4e9)) # Converted from Carrier Frequency in Hertz to avoid confusion with F the noise figure
	Pn = receiver_noise_power (dB_to_linear(F_dB[0]), dB_to_linear(B_dB)) # the power of the noise
	Pr = radar_range_eq (dB_to_linear(Tp_dB), dB_to_linear(G_dB), dB_to_linear(G_dB), dB_to_linear(L_dB), dB_to_linear(S_dB), dB_to_linear(R_dB))
	print Pn
	print Pr

	Ltx_dB = 2.1
	Lrx_dB = 4.3
	Ls_dB =  Lrx_dB + Ltx_dB
	print Ls_dB
	print dB_to_linear (Ls_dB)

	Ltx = dB_to_linear (Ltx_dB)
	print "-------------"
	print Ltx
	Lrx = dB_to_linear (Lrx_dB)
	print Lrx
	Ls = Ltx * Lrx
	print Ls
	print Ltx + Lrx
	print linear_to_dB (Ls)

	answers = [-1, -1, -1, -1]
	print "-------------"
	a1 = (Pr/Pn) * (1.0/Ls)
	print a1
	a1_dB = linear_to_dB (a1)
	print a1_dB
	print '************'

	
	answers = [-1,-1,-1,-1]
	return answers


def Q6 ():
	SNR = Q5()
	print SNR
	#answer = answer - (2.1 + 4.3)
	answers = []
	print answers
	for a in SNR:
		answers.append(a - (2.1 + 4.3))

	print answers 

	return answers;


























