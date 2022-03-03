import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dr_dt(y, t):
    """Integration of the governing vector differential equation.
    d2r_dt2 = -(mu/R^3)*r with d2r_dt2 and r as vecotrs.
    Initial position and velocity are given.
    y[0:2] = position components
    y[3:] = velocity components"""

    G = 6.672*(10**-11)
    M = 5.972*(10**24)
    mu = G*M
    r = np.sqrt(y[0]**2 + y[1]**2 + y[2]**2)

    dy0 = y[3]
    dy1 = y[4]
    dy2 = y[5]
    dy3 = -(mu / (r**3)) * y[0]
    dy4 = -(mu / (r**3)) * y[1]
    dy5 = -(mu / (r**3)) * y[2]
    return [dy0, dy1, dy2, dy3, dy4, dy5]

t = np.arange(0, 100000, 0.1)
y0 = [7.e6, 0., 0., 0., 1.e3, 0.]
y = odeint(dr_dt, y0, t)
plt.plot(y[:,0], y[:,1])
plt.show()
