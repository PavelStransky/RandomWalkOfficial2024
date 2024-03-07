import numpy as np

def unit_vector_random_direction(dimension):
    " Jednotkový vektor mířící do náhodného směru v obecné dimenzi "
    x = np.random.normal(size=dimension)
    return x / np.linalg.norm(x)

def random_walk(num_steps=100, step_size=1, initial=np.array([0, 0])):
    " Generuje náhodnou procházku"
    position = initial
    dimension = len(initial)
    path = [position]

    for _ in range(num_steps):
        position = position + step_size * unit_vector_random_direction(dimension)
        path.append(position)

    return np.array(path)