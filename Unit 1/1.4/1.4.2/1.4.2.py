# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os.path
import numpy as np

directory = os.path.dirname(os.path.abspath(__file__)) 

filename = os.path.join(directory, 'cat1-a.gif')

img = plt.imread(filename)

fig, ax = plt.subplots(1,3)

ax[0].set_xlim(35,45)
ax[1].set_xlim(45,55)
ax[2].set_xlim(55,65)

for pic in ax:
    pic.set_ylim(70,80)
    pic.imshow(img, interpolation='none')
    
fig.show()