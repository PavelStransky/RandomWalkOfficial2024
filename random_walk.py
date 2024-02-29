import numpy as np
import matplotlib.pyplot as plt

def random_walk_2d(num_steps=100, step_size=1, x0=0, y0=0):
    " Generuje náhodnou procházku ve 2D "
    x = x0
    y = y0

    xs = [x]
    ys = [y]

    for _ in range(num_steps):
        phi = 2 * np.pi * np.random.random()
        step_x = np.cos(phi)
        step_y = np.sin(phi)

        x += step_x
        y += step_y

        xs.append(x)
        ys.append(y)

    return xs, ys

xs, ys = random_walk_2d()

plt.plot(xs, ys)
plt.xlabel("x")
plt.ylabel("y")
plt.show()