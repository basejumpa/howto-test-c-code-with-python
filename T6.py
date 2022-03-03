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
t = []
t_i = 0
dt = 0.1 
t_end = 20.0


Uc = []
Uc_i = 1.0

i = []
while t_i <= t_end:
    t.append(t_i)
    Uc.append(Uc_i)
    
    i_i = C*dUc_dt(t_i, Uc_i)
    i.append(i_i)

    Uc_i = Uc_i + dt*dUc_dt(t_i, Uc_i)
    
    t_i += dt


# Plot results

plt.subplot(2,1,1)
plt.plot(t, Uc, '.', label="Voltage at Capacitor")
plt.xlabel("t [s]")
plt.ylabel("Uc [V]")
plt.legend(loc='best')


plt.subplot(2,1,2)
plt.plot(t, i, '.', label="Current")
plt.xlabel("t [s]")
plt.ylabel("i [A]")
plt.legend(loc='best')

plt.show()
