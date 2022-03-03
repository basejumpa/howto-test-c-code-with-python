import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(y,t):
    dydt = 1
    return dydt

# initial condition
y0 = 1.0

# time points
t = np.arange(0, 10, 1)

# solve ODE
y = odeint(model,y0,t)

# print results
print(t)
print(y)

# plot results
plt.plot(t,y, '.')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
