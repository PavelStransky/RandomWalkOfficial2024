# Výsledek série následujících dotazů na ChatGPT:
# 1. Napiš kód v Pythonu na náhodnou procházku v rovině s krokem délky D.
# 2. Uprav kód, aby byl kód prováděn do libovolného směru v rovině.
# 3. Rozšiř kód pro náhodnou procházku v prostoru.
# 4. Uprav kód, aby pravděpodobnost kroku do libovolného směru nezávisela na směru.

import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def random_walk_3D(steps, step_length):
    # Počáteční pozice
    x, y, z = 0, 0, 0

    # Seznamy pro ukládání souřadnic
    x_coords = [x]
    y_coords = [y]
    z_coords = [z]

    # Náhodná procházka
    for _ in range(steps):
        # Náhodné úhly
        azimuth = random.uniform(0, 2 * math.pi)
        elevation = math.acos(random.uniform(-1, 1))  # Rozložení pravděpodobnosti kroku do libovolného směru

        # Výpočet změn x, y a z souřadnic
        dx = step_length * math.sin(elevation) * math.cos(azimuth)
        dy = step_length * math.sin(elevation) * math.sin(azimuth)
        dz = step_length * math.cos(elevation)

        # Přidání nových souřadnic do seznamů
        x += dx
        y += dy
        z += dz
        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)

    return x_coords, y_coords, z_coords

# Počet kroků
steps = 1000
# Délka kroku
step_length = 1

# Provedeme náhodnou procházku
x_coords, y_coords, z_coords = random_walk_3D(steps, step_length)

# Vykreslení výsledku
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_coords, y_coords, z_coords)
ax.set_title(f"Náhodná procházka v 3D s {steps} kroky a délkou kroku {step_length}")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
