# # Mass fow rate form OpenFOAM postProcessing utility

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
from openFoamPostProcess import combineFilesAndApplyUnique

[time, objects] = \
combineFilesAndApplyUnique("", "postProcessing/flowRateFaceZone/", "surfaceFieldValue.dat", skipLinesForAppendFiles=4)
#[time1, objects1] = \
#readFunctionObjects("massLoss", "results/", "volFieldValue_nOuter4.dat")

print("time", time)
print("objects", objects)

# Plot data
plotTitle = "Liquid, vapor and total mass"
xLable =  "Physical simulation time [s]"
yLable = '$\dot{m}$ [kg/s]'
#fileNameForPlot = 'cpuTimesNormalizedNoTitle.pdf'
fileNameForPlot = 'massFlowRate.pdf'
#xLimitMax = 0.5e-5*1000.0
xLimitMax = None
xLimitMax = 12e-5
yLimitMax = None
yLimitMin = None

plt.figure(figsize=(12,6))
#plt.plot(time, objects[:,0], '-b', linewidth=2, label="mfl")
plt.plot(time, objects[:,0]*-1, '-r', linewidth=2, label="Flowrate")
#plt.title(plotTitle)
plt.xlim(0,xLimitMax)
plt.ylim(yLimitMin,yLimitMax)
#plt.legend(loc=4)
plt.legend(loc ='best',fancybox=True, framealpha=0.1, prop={'size':14}, ncol=2)
plt.grid()
plt.grid(color='tab:gray', linestyle='-', linewidth=0.5, alpha=0.5)
#plt.grid(color='0.5', linestyle='-', linewidth=0.5, alpha=1)
#plt.xlabel('Distance [mm]' , {'fontsize': 12})
plt.gca().yaxis.tick_left()
plt.gca().yaxis.set_label_position("left")
plt.gca().axes.ticklabel_format(axis='y', style='sci', scilimits=(-1,0), useMathText=True, useOffset=False)
#ax = plt.gca()
#ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.ylabel(yLable , {'fontsize': 12})
#plt.ylabel('Mean Velocity  [m/s]' , {'fontsize': 12})
plt.xlabel(xLable , {'fontsize': 12})
plt.xticks(size=12)
plt.yticks(size=12)
plt.savefig(fileNameForPlot)
plt.show()
