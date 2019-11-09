from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import ( bytes, dict, int, list, object, range, str, ascii, chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)

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

def readMassFlowRate(timeIn,fileDirLocationIn,fileNameIn):
    ''' Read the results of flowRatePatch of flowRateFaceZone postprocess function of openFoam. 
        The inputs are:
            timeInput
            directory location from the execution directoy
            file name 
        The outputs are:
            time
            flowrates'''
#    latestTime = np.loadtxt(open("latestTime.txt"))
    latestTime = timeIn
#    fileName = str(fileNameIn)
    fileName = fileNameIn
    fileDirLocation = fileDirLocationIn
    print ("latestTime", latestTime)
#    filePathSim = os.path.abspath("postProcessing/singleGraph/" + str(latestTime))
    filePathSim = os.path.abspath(fileDirLocation + str(latestTime))
    print ("filePathSim", filePathSim)
#    alphaSimData = np.loadtxt(open(filePathSim+"/line_UMean.xy"), delimiter=" ", skiprow
    simData = np.loadtxt(open(filePathSim + "/" + fileName), skiprows=0, comments='#')
    time =  simData[:,0]
    print("size", simData.shape[1])
    flowRates = simData[:,1:simData.shape[1]]

    print("time", time[0,])  
    print("flowRates", flowRates[0,:])
    
    print("flowRates.size", flowRates.shape[0])
#    print("magField.size", magField.shape[0])

    return time, flowRates
