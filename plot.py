import matplotlib.pyplot as plt
import numpy as np
import random_walk

path = random_walk.random_walk(num_steps=1000, initial=np.array([0, 0, 0]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(path[:, 0], path[:, 1], path[:, 2])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.title("Náhodná procházka ve 3D")
plt.show()
