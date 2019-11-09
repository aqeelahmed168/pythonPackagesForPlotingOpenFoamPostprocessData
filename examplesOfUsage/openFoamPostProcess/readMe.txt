The data is in the location 
"cavitatingFoamInjOnly/postProcessing/flowRatePatch/"
time directory is 0, and the file name is "surfaceFieldValue.dat"
readMassFlowRate function is used to get the time vs flow rate data.

Next this is called in the pyhton script (which also plots data as save it as .pdf)
massFlowRateFromFlowRatePatchUtility.py as
> python massFlowRateFromFlowRatePatchUtility.py

---------------------------------------------------

In the second example data is read from two different directories
    1. 3dCavInjLimosDynKEqn
    2. 3dCavInjLimosWALE
to call the readSingleGraph utility from the package 'openFoamPostProcess'
The script used is
velocityOnSampledLines.py, run it as 
> pyhton velocityOnSampledLines.py

---------------------------------------------------

In the third example data is read from "times" directory
to call the readFunctionObjects utility from the package 'openFoamPostProcess'
The script used is
plotFromFoamData.py, run it as 
> pyhton plotFromFoamData.py
