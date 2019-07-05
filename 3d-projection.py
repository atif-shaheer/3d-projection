import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=[1,2,3,4,5]
y=[45,34,45,56,78]
a = plt.figure()
p = a.add_subplot(211,projection= '3d')
p.scatter(x,y)
p2 = a.add_subplot(212,projection='3d')
p2.bar(x,y)

plt.show()
