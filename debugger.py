import numpy as np
import time
import debugpy

debugpy.listen(5678)

debugpy.wait_for_client()
for x in range(10):
    print(f'Doing computation {x}')
    data = np.random.random((50,50))
    suma = np.sum(data)
    time.sleep(2)