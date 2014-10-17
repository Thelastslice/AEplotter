import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import piezoBackup as pF
import numpy as np
import os
import time
import gc

# plotDir1 = '/Volumes/The Pit/FAC PiezoSensor/Data/flow_80%/noO2/temp_95/trial_1_June_2014/processedData/Test/avePiezo'
# plotDir1 = '/Volumes/The Pit/FAC PiezoSensor/Data/flow_80%/noO2/temp_95/trial_1_June_2014/processedData/Test/avePiezo'
plotDir1 = '/Volumes/The Pit/FAC PiezoSensor/Data/flow_30%/noO2/temp_95/trial_1_Feb_2014/processedData/piezos'
plotDir2 = '/Volumes/The Pit/FAC PiezoSensor/Data/flow_30%/noO2/temp_95/trial_2_Mar_2014/processedData/piezos'
plotDir3 = '/Volumes/The Pit/FAC PiezoSensor/Data/flow_30%/noO2/temp_95/trial_1_Feb_2014/processedData/accelerometer'
plotDir4 = '/Volumes/The Pit/FAC PiezoSensor/Data/flow_30%/noO2/temp_95/trial_2_Mar_2014/processedData/accelerometer'


# xNew = np.load(os.path.join(plotDir1, 'avePSDX.npy'))
# yNew = np.load(os.path.join(plotDir1, 'avePSDY.npy'))
# zNew = np.load(os.path.join(plotDir1, 'avePSDZ.npy'))

# 
# xAccel = np.load(os.path.join(plotDir1, 'avePSDXAccel.npy'))
# yAccel = np.load(os.path.join(plotDir1, 'avePSDYAccel.npy'))
# zAccel = np.load(os.path.join(plotDir1, 'avePSDZAccel.npy'))


# np.savetxt(os.path.join(plotDir2, '80zReadout'), zNew)

# xNew = np.asarray(xNew)
# print xNew.shape
# yNew = np.asarray(yNew)
# print yNew.shape
# zNew = np.asarray(zNew)
# print zNew.shape

# xAccel = np.asarray(xAccel)
# print xAccel.shape
# yAccel = np.asarray(yAccel)
# print yAccel.shape
# zAccel = np.asarray(zAccel)
# print zAccel.shape

# zNew = np.transpose(zNew)
#  
# ySplit = np.split(yNew,[1])
# ySplit = np.asarray(ySplit)
# ysplitShape = ySplit.shape
# yCut = ySplit[1]
# print yCut.shape
#   
# zSplit = np.split(zNew,[1])
# zSplit = np.asarray(zSplit)
# splitShape = zSplit.shape
# zCut = zSplit[1]
# print zCut.shape

# xSplit = np.split(yNew,[1])
# xSplit = np.asarray(xSplit)
# xSplitShape = xSplit.shape
# xCut = xSplit[1]
# print xCut.shape
# np.savetxt(os.path.join(plotDir1, 'zDelReadout'), zDel)
# xOld = np.load(os.path.join(plotDir1, 'avePSDX_old.npy'))
# yOld = np.load(os.path.join(plotDir1, 'avePSDY_old.npy'))
# zOld = np.load(os.path.join(plotDir1, 'avePSDZ_old.npy'))
# xOld = np.asarray(xOld)
# print xOld.shape
# yOld = np.asarray(yOld)
# print yOld.shape
# zOld = np.asarray(zOld)
# print zOld.shape
# print' '
# 
# zCut = np.transpose(zCut)


# zOld = [i*6 for i in zOld]
# plt.plot(freq,PSD,'', label='Theirs')
# plt.plot(yNew,zNew[0],'', label='Ours')
# minValZ = np.min(zNew[np.nonzero(zNew)])
# maxValZ = np.max(zNew[np.nonzero(zNew)])
# minValY = np.min(yCut[np.nonzero(yCut)])
# maxValY = np.max(yCut[np.nonzero(yCut)])
# print minValY 
# print maxValY
 
# print minValZ 
# print maxValZ 
# print np.log10(minValZ)
# print np.log10(maxValZ)
# zsubbed = zCut - yCut
# lvls = np.logspace(np.log10(minValZ),np.log10(maxValZ),20)
# plt.subplot(311)
# CF = plt.contourf(xNew,yNew,zNew,norm=LogNorm(),labels='...')
# plt.subplot(312)
# CF = plt.contourf(xNew,xCut,yCut,norm=LogNorm(),labels='...')
# plt.subplot(313)
# CF = plt.contourf(xNew,xCut,zsubbed,norm=LogNorm(),labels='...')

plt.plot(y1s,z1s,'',label='Time = 0min')
plt.plot(y1s,z1s,'',label='Time = 0min')
plt.plot(y1s,z1s,'',label='Time = 0min')

plt.plot(y1s,z1s,'',label='Time = 0min')
plt.plot(y1s,z1s,'',label='Time = 0min')
plt.plot(y1s,z1s,'',label='Time = 0min')
plt.plot(y1s,z1s,'',label='Time = 0min')
plt.plot(y1s,z1s,'',label='Time = 0min')
plt.plot(y1s,z1s,'',label='Time = 0min')

# from matplotlib.ticker import LogFormatter
# l_f = LogFormatter(10, labelOnlyBase=False)
plt.semilogy()
plt.ylim(100,100000)
# plt.xlim(100,500000)
# plt.loglog()
plt.title('Example of PSD Applied to AE System')
plt.legend(loc='best')
plt.xlabel('Hz (cyc/s)')
plt.ylabel('Volt^2/Hz')
# cbar = plt.colorbar(CF, ticks=lvls, format=l_f)
plt.show()
