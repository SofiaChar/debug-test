import numpy as np
import time

for x in range(10):
    print(f'Doing computation {x}')
    data = np.random.random((50,50))
    suma = np.sum(data)
    time.sleep(2)