import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(y,t):
    dydt = 0
    return dydt

# initial condition
y0 = 1

# time points
t = np.linspace(0,20, 5)

# solve ODE
y = odeint(model,y0,t)

# plot results
plt.plot(t,y, '.')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
