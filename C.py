from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

y0 = [1.0]

def func(t, y):
    return [1.0]

t_span = [0, 10]
sol1 = solve_ivp(func, t_span, y0)
print("sol1.t: {}".format(sol1.t))
