import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import pims
import trackpy as tp

frames = pims.as_gray(pims.open('IMG_0253/*.tiff'))

print(len(frames))
fs = 150
f = tp.locate(frames[fs], 5, invert=True, minmass=150)
tp.annotate(f, frames[fs])
plt.imshow(frames[fs])

"""
xpos = []
ypos = []
for i in range(0,len(frames)):
    f = tp.locate(frames[i],5,invert = True , minmass=140)
    data = np.array(f.iloc[:,:2])
    mask = np.logical_and(data[:,0] <= 600, data[:,1] >= 50)
    data = data[mask]
    xavg = np.mean(data[:,0])
    yavg = np.mean(data[:,1])
    xpos.append(xavg)
    ypos.append(yavg)

plt.scatter(xpos,ypos, s = 5)
plt.show()

"""
