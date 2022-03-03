import numpy as np
import matplotlib.pyplot as plt


# initial value of t, y
k,t,y=1,0.0,5.0
y0=y
tt,yy=[],[]

tf=10 # final value of x
dt=0.01 # step length

# defining function
def f(t,y,k):
    return -k*y

# implementation of Euler method
while t<=tf:
    tt.append(t)
    yy.append(y)
    y=y+dt*f(t,y,k)
    t+=dt

#calculation of exact result
tt=np.array(tt)
exact=y0*np.exp(-k*tt)

# Plotting solution with exact result
plt.subplot(2,1,1)
plt.plot(tt,yy,'k--',label="dt=%.4f"%(dt))
plt.plot(tt, y0*np.exp(-k*tt),'k',label="Exact solution")
plt.xlabel("time")
plt.ylabel("y")
plt.legend(loc='best')

# Plotting absolute error
diff=exact-yy
plt.subplot(2,1,2)
plt.plot(tt,diff,'k.',label="Absolute error")
plt.xlabel("time")
plt.ylabel("Error")
plt.legend(loc='best')
plt.title("ODE by Euler method")
#plt.savefig("decay-euler.png")
plt.show()
