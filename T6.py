import numpy as np
import matplotlib.pyplot as plt

# Parameters
R=1.0
C=1.0

# Input function
def U_in(t):
    if t < 5.0:
        return 0.0
    else:
        return 1.0

# Voltage at Capacitor

def dUc_dt(t, Uc):
    return -1/(R*C)*Uc + 1/(R*C)*U_in(t)

# Simulate with integration according Euler method
t_i = 0
dt = 0.1 
t_end = 20.0

t = []
Uc = []
Uc_i = 1.0
while t_i <= t_end:
    t.append(t_i)
    Uc.append(Uc_i)

    Uc_i = Uc_i + dt*dUc_dt(t_i, Uc_i)
    
    t_i += dt

# Plotting solution with exact result
plt.plot(t, Uc, '.')
plt.show()
