import matplotlib.pyplot as plt
import random_walk

path = random_walk.random_walk_2d()

plt.plot(path[:, 0], path[:, 1])
plt.xlabel("a")
plt.ylabel("b")
plt.show()