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
from openFoamPostProcess import readFunctionObjects

[time1, objects] = \
readFunctionObjects(0, "times/p16/time/", "time.dat")

[time1s, objects1s] = \
readFunctionObjects(0, "times/p16scotch/time/", "time.dat")

[time2, objects2] = \
readFunctionObjects(0, "times/p8/time/", "time.dat")

[time2s, objects2s] = \
readFunctionObjects(0, "times/p8scotch/time/", "time.dat")

[time3, objects3] = \
readFunctionObjects(0, "times/p4/time/", "time.dat")

[time3s, objects3s] = \
readFunctionObjects(0, "times/p4scotch/time/", "time.dat")

[time0, objects0] = \
readFunctionObjects(0, "times/p1serial/time/", "time.dat")

print(objects.size)


# Plot data
plotTitle = "CPU times for serial and parallel run (About 350 time steps)"
xLable =  "Physical simulation time [ms]"
yLable = 'CPU Time/Maximum Time [-]'
#fileNameForPlot = 'cpuTimesNormalizedNoTitle.pdf'
fileNameForPlot = 'cpuTimesNormalizedNoSerialNoTitle.pdf'
xLimitMax = 0.5e-5*1000.0
yLimitMax = None
yLimitMax = 1
#maxCPUTime = 1842 #serial
maxCPUTime = 544 #parallel 4scoth

plt.figure(figsize=(8,6))
#plt.plot(time0*1000, objects0[:,1]/maxCPUTime, '-k',linewidth=2, label="1-serial")
plt.plot(time3*1000, objects3[:,1]/maxCPUTime, '-r',linewidth=2, label="4-simple")
plt.plot(time3s*1000, objects3s[:,1]/maxCPUTime, '--r',linewidth=2, label="4-scotch")
#plt.plot(time3*1000, objects3[:,-1]*100, '-r',linewidth=2, label="4/timeStepX100")
plt.plot(time2*1000, objects2[:,1]/maxCPUTime, '-g',linewidth=2, label="8-simple")
plt.plot(time2s*1000, objects2s[:,1]/maxCPUTime, '--g',linewidth=2, label="8-scotch")
plt.plot(time1*1000, objects[:,1]/maxCPUTime, '-b',linewidth=2, label="16-simple")
plt.plot(time1s*1000, objects1s[:,1]/maxCPUTime, '--b',linewidth=2, label="16-scotch")

#plt.plot(time1, mflExp, '-r',linewidth=2, label="Experimental")
#plt.fill_between(time1, mflExp-mflExpErr,  mflExp+mflExpErr, facecolor='r', alpha=0.5, edgecolor='none')

#plt.title(plotTitle)
plt.xlim(0,xLimitMax)
plt.ylim(0,yLimitMax)
#plt.legend(loc=4)
plt.legend(loc ='best',fancybox=True, framealpha=0.1, prop={'size':14}, ncol=2)
plt.grid()
plt.grid(color='tab:gray', linestyle='-', linewidth=0.5, alpha=0.5)
#plt.grid(color='0.5', linestyle='-', linewidth=0.5, alpha=1)
#plt.xlabel('Distance [mm]' , {'fontsize': 12})
plt.gca().yaxis.tick_left()
plt.gca().yaxis.set_label_position("left")
plt.ylabel(yLable , {'fontsize': 12})
#plt.ylabel('Mean Velocity  [m/s]' , {'fontsize': 12})
plt.xlabel(xLable , {'fontsize': 12})
plt.xticks(size=12)
plt.yticks(size=12)
plt.savefig(fileNameForPlot)
plt.show()

