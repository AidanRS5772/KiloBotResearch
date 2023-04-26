import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import pims
import trackpy as tp

frames = pims.as_gray(pims.open('IMG_0253/*.tiff'))

"""
fs = 150
f = tp.locate(frames[fs], 5, invert=True, minmass=150)
tp.annotate(f, frames[fs])
#plt.imshow(frames[fs])

"""

xpos = []
ypos = []
for i in range(0,len(frames)):
    f = tp.locate(frames[i],5,invert = True , minmass=100)
    data = np.array(f.iloc[:,:2])
    mask = np.logical_and(data[:,0] <= 600, data[:,1] >= 50)
    data = data[mask]
    xavg = np.mean(data[:,0])
    yavg = np.mean(data[:,1])
    xpos.append(xavg)
    ypos.append(yavg)

plt.figure()
xpos = np.divide(np.array(xpos),634)
ypos = np.divide(np.array(ypos),636)
plt.scatter(xpos,ypos, s = 2)
plt.title("Position of KiloBot")
plt.xlabel("Position Y (m)")
plt.ylabel("Position X (m)")

print("Got data")

msd = []
length = len(xpos)


interval = 5
for n in range(0,length,interval):
    msd.append(np.mean((xpos[n:]-xpos[:length-n])**2+(ypos[n:]-ypos[:length-n])**2))

plt.figure()
plt.scatter(np.multiply(range(0,length,interval),1/60),msd , s = 2)
plt.title("MSD")
plt.xlabel("Time Interval (s)")
plt.ylabel("Mean Squared Displacement (m^2)")

plt.show()