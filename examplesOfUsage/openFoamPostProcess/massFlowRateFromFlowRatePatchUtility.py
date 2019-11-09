# # Mass flow rate form OpenFOAM postProcessing utility

# Load modules
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv
import scipy
from scipy.interpolate import griddata
# from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.interpolate import SmoothBivariateSpline
import prettyplotlib as ppl
from prettyplotlib import brewer2mpl
from scipy.integrate import simps
import os


#- load the functions from openFoamPostProcess package
from openFoamPostProcess import readSingleGraph
from openFoamPostProcess import readMassFlowRate

[time1, flowRates1] = \
readMassFlowRate(0, "cavitatingFoamInjOnly/postProcessing/flowRatePatch/", "surfaceFieldValue.dat")

#[ySim2, magField2, field2] = \
#readSingleGraph(0.015,"3dCavInjLimosWALE/postProcessing/singleGraph/", "line_UMean.xy")

#convert 5 deg to 360 deg
flowRates1 *=(360.0/5.0)

# reference data from ECN
mflExp = np.ones_like(time1)
mflExp *= 10.07e-3 # data in Kg/s
mflExpErr = 0.11e-3


#    plot data
plt.figure(figsize=(8,6))
plt.plot(time1, flowRates1[:,0], '-b',linewidth=2, label="Numerical")
plt.plot(time1, mflExp, '-r',linewidth=2, label="Experimental")
plt.fill_between(time1, mflExp-mflExpErr,  mflExp+mflExpErr, facecolor='r', alpha=0.5, edgecolor='none')
#plt.plot(ySim, field[:,0], '--b',linewidth=2, label="Ux - WALE")

#    plt.xlim(0,0.2)
#    plt.ylim(0,)
#plt.legend(loc=4)
plt.legend(loc ='best',fancybox=True, framealpha=0.1)
plt.grid()
#plt.xlabel('Distance [mm]' , {'fontsize': 12})
plt.gca().yaxis.tick_left()
plt.gca().yaxis.set_label_position("left")
plt.ylabel('MassflowRate [kg/s]' , {'fontsize': 12})
#plt.ylabel('Mean Velocity  [m/s]' , {'fontsize': 12})
plt.xlabel('Time  [s]' , {'fontsize': 12})
plt.xticks(size=12)
plt.yticks(size=12)
plt.savefig('massFlowRatePloti.pdf')
plt.show()
