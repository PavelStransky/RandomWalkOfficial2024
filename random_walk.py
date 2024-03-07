import numpy as np

def unit_vector_random_direction():
    " Jednotkový vektor mířící do náhodného směru "
    phi = np.random.uniform(0, 2 * np.pi)
    return np.array([np.cos(phi), np.sin(phi)])

def random_walk_2d(num_steps=100, step_size=1, initial=np.array([0, 0])):
    " Generuje náhodnou procházku ve 2D "
    position = initial
    path = [position]

    for _ in range(num_steps):
        position = position + step_size * unit_vector_random_direction()
        path.append(position)

    return np.array(path)