from problem1 import Wolfe
import numpy as np

rho = 1.23
mu = 17.8e-6
V = 35
S = 11.8
S_wet = 2.05*S
k = 1.2
e = 0.96
W0 = 4940
Nult = 2.5

def CD(x):
    A = x[0]; S = x[1]

    ## C_f
    Re = (rho*V*c)/mu
    C_f = 0.074/(Re**0.2)

    Cd = 0.03062702/S + k*C_f*(S_wet/S) + (C_L**2)/(np.pi*A*e)