import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


## Circuit T_1

R=1.0
C=1.0
u=0.0

# initial condition
y0_0 = 1.0
y1_0 = 1.0

y0 = [y0_0, y1_0]

# function that returns dy/dt
def model(y,t):
    dydt_1 = -1/(R*C)*y[0] + 1/(R*C)*u
    dydt_2 = 0
    return [dydt_1, dydt_2]


# time points
t = np.arange(0, 10, 0.1)

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
