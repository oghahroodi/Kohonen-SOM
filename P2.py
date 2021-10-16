from som import *
import matplotlib.pyplot as plt
import numpy as np


color_data = np.random.rand(40*40, 3)


som_color = SOM(40, 40, 3)
frames_color = []
som_color.train(color_data, L0=0.8, lam=1e2, sigma0=20, frames=frames_color)


# print(list(frames_color[-1]))
plt.imshow(frames_color[0])
plt.show()
plt.imshow(frames_color[-1])
plt.show()
