from __future__ import division, unicode_literals, print_function  # for compatibility with Python 2 and 3

import matplotlib as mpl
import matplotlib.pyplot as plt

# Optionally, tweak styles.
mpl.rc('figure',  figsize=(10, 6))
mpl.rc('image', cmap='gray')

import numpy as np
import pandas as pd
from pandas import DataFrame, Series  # for convenience

import pims
import trackpy as tp


frames = pims.ImageSequence('3.6e-5driven/*.png', as_grey=True)

f = tp.locate(frames[0], diameter=5, minmass=0.000001, invert=True, topn=1)
f.head()

plt.figure()  # make a new figure
tp.annotate(f, frames[0])
plt.show()

# locate in all frames
f = tp.batch(frames[:], diameter=5, minmass=0.000001, invert=True, topn=1)

# create trajectory
t = tp.link_df(f, 200, memory=3)
t.head()

# plot trajectories
plt.figure()
tp.plot_traj(t)

t.to_csv("trajectory.csv")

