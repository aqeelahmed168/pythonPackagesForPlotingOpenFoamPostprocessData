from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import ( bytes, dict, int, list, object, range, str, ascii, chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy
from scipy.interpolate import griddata
# from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.interpolate import SmoothBivariateSpline
from scipy.integrate import simps
import os

def readFunctionObjects(timeIn,fileDirLocationIn,fileNameIn,delimiter=None):
    ''' Read the results of  generic function object postprocess of openFoam. 
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
    # put delimiter in the input
    foData = np.loadtxt(open(filePathSim + "/" + fileName), delimiter=delimiter, skiprows=0, comments='#')
    xData =  foData[:,0]
    
    # Print headers
    print("File headers")  
    with open(filePathSim + "/" + fileName, newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        row1 = next(reader)
        row2 = next(reader)
        print(row1,"\n",row2)
    f.close()
    
    print("data columns", foData.shape[1])
    objects = foData[:,1:foData.shape[1]]

    print("xData[0]", xData[0,])  
    print("objects[0,:]", objects[0,:])
    
#    magField = np.sqrt(field[:,0]**2 + field[:,1]**2 + field[:,2]**2)
#    magField = np.absolute(field)
#    magField = np.linalg.norm(field,axis=1)
#    magField = np.sqrt(field**2 )
    
    print("objects.size", objects.shape)

    return xData, objects
