# # Alpha experimenta vs numerical 2D test case - ECN Spray A

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
#print matplotlib.get_backend()

from openFoamPostProcess import readSingleGraph

#print(readSingleGraph.__doc__)

[ySim1, magField1, field1] = \
readSingleGraph(0.015, "3dCavInjLimosDynKEqn/postProcessing/singleGraph/", "line_UMean.xy")

[ySim2, magField2, field2] = \
readSingleGraph(0.015,"3dCavInjLimosWALE/postProcessing/singleGraph/", "line_UMean.xy")

ySim1 *=1000
ySim2 *=1000
#    plot data
plt.figure(figsize=(8,6))
#plt.plot(ySim1, magField1, '-',linewidth=2, label="dynKEqn")
#plt.plot(ySim2, magField2, '-',linewidth=2, label="WALE")
#plt.plot(ySim1, field1[:,0], '-b',linewidth=2, label="Ux - dynKEqn")
#plt.plot(ySim2, field2[:,0], '--b',linewidth=2, label="Ux - WALE")
#plt.plot(ySim1, field1[:,1], '-g',linewidth=2, label="Uy - dynKEqn")
#plt.plot(ySim2, field2[:,1], '--g',linewidth=2, label="Uy - WALE")
#plt.plot(ySim1, field1[:,2], '-r',linewidth=2, label="Uz - dynKEqn")
#plt.plot(ySim2, field2[:,2], '--r',linewidth=2, label="Uz - WALE")

plt.plot(field1[:,0], ySim1,'-b',linewidth=2, label="Ux - dynKEqn")
plt.plot(field2[:,0], ySim1, '--b',linewidth=2, label="Ux - WALE")
plt.plot(field1[:,1], ySim1, '-g',linewidth=2, label="Uy - dynKEqn")
plt.plot(field2[:,1], ySim1, '--g',linewidth=2, label="Uy - WALE")
plt.plot(field1[:,2], ySim1,'-r',linewidth=2, label="Uz - dynKEqn")
plt.plot(field2[:,2], ySim1, '--r',linewidth=2, label="Uz - WALE")
#    plt.xlim(0,0.2)
#    plt.ylim(0,)
#plt.legend(loc=4)
plt.legend(loc ='best',fancybox=True, framealpha=0.1)
plt.grid()
#plt.xlabel('Distance [mm]' , {'fontsize': 12})
plt.gca().yaxis.tick_right()
plt.gca().yaxis.set_label_position("right")
plt.ylabel('Distance [mm]' , {'fontsize': 12})
#plt.ylabel('Mean Velocity  [m/s]' , {'fontsize': 12})
plt.xlabel('Mean Velocity  [m/s]' , {'fontsize': 12})
plt.xticks(size=12)
plt.yticks(size=12)
plt.savefig('velocity3plot.pdf')
plt.show()
