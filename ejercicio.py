import numpy as np
import matplotlib.pylab as plt
a=np.linspace(-2*np.pi,2*np.pi,100)
b=[]
for i in range(len(a)):
    b.append(np.cos(a[i]))
plt.plot(a,b)
plt.savefig('seno.png')