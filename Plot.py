from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
# defining surface and axes
x = np.outer(np.linspace(-10, 10, 20), np.ones(20))
y = x.copy().T

#z = np.power(np.cos(x),2) + np.power(np.sin(y),2)
z = np.power(x,2) + np.power(y,2)

fig = plt.figure()
 
# syntax for 3-D plotting
ax = plt.axes(projection='3d')
 
# syntax for plotting
ax.plot_surface(x, y, z, cmap='plasma',\
                edgecolor='black')
ax.set_title('For testing the optimization')
print(np.shape(z))
print(np.linspace(-10, 10, 20))
print(np.outer(np.linspace(-10, 10, 20), np.ones(20)))
plt.show()

