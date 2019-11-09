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

def readSingleGraph(timeIn,fileDirLocationIn,fileNameIn):
    ''' Read the results of singleGraph postprocess function of openFoam. 
        The inputs are:
            timeInput
            directory location from the execution directoy
            file name '''
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
    simData = np.loadtxt(open(filePathSim + "/" + fileName), delimiter=" ", skiprows=0, comments='#')
    ySim =  simData[:,0]
    print("size", simData.shape[1])
    field = simData[:,1:simData.shape[1]]

    print("ySim", ySim[0,])  
    print("field", field[0,:])
    
#    magField = np.sqrt(field[:,0]**2 + field[:,1]**2 + field[:,2]**2)
#    magField = np.absolute(field)
    magField = np.linalg.norm(field,axis=1)
#    magField = np.sqrt(field**2 )
    
    print("field.size", field.shape[0])
    print("magField.size", magField.shape[0])

    return ySim, magField, field
