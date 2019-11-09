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
import sys
import shutil
import glob
from itertools import islice

def sortKeyFunc(s):
    #'''function to generate sort key'''
    #print(os.path.basename(s))
    return float(os.path.basename(s)[:])

def combineFilesAndApplyUnique(timeIn,fileDirLocationIn,fileNameIn,delimiter=None,skipLinesForAppendFiles=1):
    ''' Read the results of  generic function object postprocess of openFoam. 
        The inputs are:
            timeInput
            directory location from the execution directoy
            file name '''
#    latestTime = np.loadtxt(open("latestTime.txt"))
    latestTime = timeIn
    fileName = fileNameIn
    fileDirLocation = fileDirLocationIn
    print ("latestTime", latestTime)
    filePathSim = os.path.abspath(fileDirLocation + str(latestTime))
    print ("filePathSim", filePathSim)
    
    mainFolderPath = filePathSim + "/*"
    print("mainFolderPath", mainFolderPath)
    
    list_of_folders = glob.glob(mainFolderPath)
    print("list", list_of_folders)
    sortedList = sorted(list_of_folders, key=sortKeyFunc)
    print("sorted list", sortedList)
    newFileName = fileNameIn + "_Combined.dat"
    f2 = open(newFileName, 'w')
    index = 0
    for i in sortedList:
        print("i",i)
        fileName = i + "/" + fileNameIn
        print("fileName", fileName)
        f = open(fileName, 'r')
        if index == 0:
            for line in f:
                f2.write(line)
        else:
            for line in islice(f, skipLinesForAppendFiles, None):
                f2.write(line)
        f.close()
    f2.close()

    # Print headers
    print("File headers")  
    with open(newFileName, 'r',  newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        row1 = next(reader)
        row2 = next(reader)
        row3 = next(reader)
        row4 = next(reader)
        print(row1,"\n",row2, "\n", row3, "\n", row4)
    f.close()

    foData = np.loadtxt(newFileName, delimiter=delimiter, skiprows=0, comments='#')
    xData =  foData[:,0]
    objects = foData[:,1:foData.shape[1]]
    print("xData[0]", xData[0,])  
    print("objects[0,:]", objects[0,:])
    print("objects.size", objects.shape)
    print("data columns", foData.shape[1])
    objects = foData[:,1:foData.shape[1]]
    
    # apply unique filter
    uniqueX, uniqueIndex = np.unique(xData, return_index=True)
    xData = xData[uniqueIndex]
    objects = objects[uniqueIndex,:]

    return xData, objects
