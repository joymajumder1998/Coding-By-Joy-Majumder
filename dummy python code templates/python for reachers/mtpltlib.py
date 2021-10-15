import matplotlib.pyplot as plt
import numpy as np

a=[(2,3),(4,1),(5,2),(2,8),(1,8)]
b=[(3,6),(9,2),(4,2),(2,6)]

aa=np.array(a)
bb=np.array(b)
plt.plot(aa[:,0], aa[:,1], "bo", label="1st")
plt.plot(bb[:,0], bb[:,1], "ro", label="2nd")
plt.legend()
plt.axis([0,10,0,10])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
plt.savefig("test.png")
