import numpy as np
cnt = 0
for i in range(1000000):
    x = np.random.rand()
    y = np.random.rand()
    if (x-0.5)**2+(y-0.5)**2 < 0.25:
        cnt+=1

print("simulation result is: ",4*cnt/1000000)
print("Ground Truth for pi is:",np.pi)
