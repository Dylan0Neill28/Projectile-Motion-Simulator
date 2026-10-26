import numpy as np
import matplotlib.pyplot as plt
import time

G = 6.6743 * (10 ** (-11))
M = 5.9722 * (10 ** 24)
R = 6.371 * (10 ** 6)

v0 = 7
y0 = 6
d = 45

def get_time(t0):
    if t0 is None:
        return time.time()
    else: 
        return time.time() - t0

def radians(d):
    return d / 180 * np.pi

def x_start_velocity(r):
    return v0 * np.cos(r)

def y_start_velocity(r):
    return v0 * np.sin(r)

def x_t(vx0, t):
    return vx0 * t

def y_t(y0, vy0, t, G):
    return y0 + (vy0 * t) - 1/2 * (G * t ** 2)

def y_velocity(vy0, g, t):
    return vy0 - (g * t)

def gravity(h, G, M, R):
    return (G * M) / ((h + R) ** 2)

r = radians(d)
vx0 = x_start_velocity(r)
vy0 = y_start_velocity(r)

t0 = get_time(0)
t = [0]
g = [gravity(y0, G, M, R)]
x_position = []
y_position = []


while True:
    y_next = y_t(y0, vy0, t[-1], g[-1])
    
    if y_next <= 0:
        break

    t.append(t[-1] + 0.00001)
    g.append(gravity(y_next, G, M, R))

t = np.array(t)
g = np.array(g)

x_position = np.array(x_t(vx0, t))
y_position = np.array(y_t(y0, vy0, t, g))

y = get_time(t0)

print(y)
plt.plot(x_position, y_position)
plt.xlabel("Hotizontle Position")
plt.ylabel("Vertical Position (m)")
plt.title("Projectile Position vs. Hotizontle Position")
plt.show()
