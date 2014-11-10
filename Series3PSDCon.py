import matplotlib as mpl
mpl.use('AGG')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
import os
import time
import gc
import datetime


# Main Directory Selector
mainDir = '/Volumes/The Pit/FAC PiezoSensor/Data/' #External Harddrive selection

# # of plots to be made subliminal
rowsSubplots = 3
columnsSubplots = 2

#Sub-directory finder
def getDirectory(mainDir, flow, o2, temp, trial, flow_ramping = None):
    subDir = mainDir+'flow_'+flow+'%/'+o2+'O2/'+'temp_'+temp+'/'+trial+'/processedData/'
    if flow_ramping != None:
        subDir =  subDir.replace('temp_'+temp,'temp_'+temp+'/flow_ramping')
    else:
        pass
    
    return subDir

def getRunsAverage(Z,n):
    shap =  Z.shape
    print 'Averaging over %s Runs' %n
    length = shap[1]
    sizeCorrection = length-length%n
    interval = sizeCorrection/n
      
    if length%n != 0:
        del_list = range(sizeCorrection,length)
        Z = np.delete(Z,del_list, axis = 1)
       
    Zsplit = np.split(Z, interval,axis = 1)
    Zsplit = np.asarray(Zsplit)
    splitShape = Zsplit.shape
    bins = splitShape[0]
    newArr = list()
    newAppend = newArr.append
    
    for i in range(bins):
        tempZ = Zsplit[i]
        meanTemp = np.mean(tempZ,axis=1)
        newAppend(meanTemp)
        
    newArr = np.asarray(newArr)
    Znew = np.transpose(newArr)
    
    return Znew, bins

fig = plt.figure(0, figsize = (12,18))
# fig.suptitle(title, fontweight = 'bold',fontsize = '20')

for j in range(rowsSubplots):
    
            
    if j==0:
        type = 'avePiezo'
        valueZ = 'avePSDZ.npy'
        labelsd = 'Ave. Piezo (Hz)'
    elif j==1:
        type = 'accelerometer'
        valueZ = 'accelZ.npy'
        labelsd = 'Ave. Accel (Hz)'
    else:
        type = 'FAC'
        
    long = False

        
    for i in range(columnsSubplots):
        
        tic = time.clock() 
        ax = plt.subplot2grid((rowsSubplots,columnsSubplots), (j,i))
        
        if i%2 ==0: 
            if i==0: 
                ax.set_ylabel(labelsd, fontsize=16)
                trial = 'trial_1_June_2014'
                flow = '80'
                o2 = 'no'
                temp = '95'
                
                title = 'T=95Deg C, No O2'
                
                if type == 'FAC':
                    ax.set_ylabel('Inner Diameter (m)',fontsize=16)
                    plotDir1 = '/Users/cathymartin/Desktop/DickBiscuit'
                    FAC = np.load(os.path.join(plotDir1, '80_1.npy'))
                    dateB1 = FAC[0]
                    diameterB1 = FAC[1]
                    fitB1 = FAC[2]
                    FACB1 = FAC[3]
                else:
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial)+'avePiezo'
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = True
                
            elif i==2:
                trial = 'trial_1_Mar3_2014'
                flow = '30'
                o2 = 'high'
                temp = '95'
                
                title = 'T.1. 1.16l/min  w/O2'
                
                if type == 'FAC':
                    plotDir1 = '/Users/cathymartin/Desktop/DickBiscuit'
                    FAC = np.load(os.path.join(plotDir1, '30_o_1.npy'))
                    dateB1 = FAC[0]
                    diameterB1 = FAC[1]
                    fitB1 = FAC[2]
                    FACB1 = FAC[3]
                else:
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial)+'avePiezo'
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = True
                
            else:
                trial = 'skip'
                flow = '30'
                o2 = 'no'
                temp = '95'
                
                title = '20% Flow ' +'No O2'
                
                if type == 'FAC':
                    plotDir1 = '/Users/cathymartin/Desktop/DickBiscuit'
                    FAC = np.load(os.path.join(plotDir1, '30_2.npy'))
                    dateB1 = FAC[0]
                    diameterB1 = FAC[1]
                    fitB1 = FAC[2]
                    FACB1 = FAC[3]
                else:
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial)+'avePiezo'
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = True
             
        else:
            if i==1:   
                trial = 'trial_1_June_2014'
                flow = '80'
                o2 = 'no'
                temp = '140'
                
                title = 'T=140Deg C, No O2'
                
                if type == 'FAC':
                    plotDir1 = '/Users/cathymartin/Desktop/DickBiscuit'
                    FAC = np.load(os.path.join(plotDir1, '80_2.npy'))
                    dateB1 = FAC[0]
                    diameterB1 = FAC[1]
                    fitB1 = FAC[2]
                    FACB1 = FAC[3]
                else:
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial)+'avePiezo'
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = True
                
            elif i==3:
                trial = 'trial_2_Mar13_2014'
                flow = '30'
                o2 = 'high'
                temp = '95'
                
                title = '20% Flow ' +'No O2'
                
                if type == 'FAC':
                    plotDir1 = '/Users/cathymartin/Desktop/DickBiscuit'
                    FAC = np.load(os.path.join(plotDir1, '30_o_2.npy'))
                    dateB1 = FAC[0]
                    diameterB1 = FAC[1]
                    fitB1 = FAC[2]
                    FACB1 = FAC[3]
                else:
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial)+'avePiezo'
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = True
                
            else:
                trial = 'skip'
                flow = '20'
                o2 = 'no'
                temp = '95'
                
                title = '20% Flow ' +'No O2'
                
                if type == 'FAC':
                    plotDir1 = '/Users/cathymartin/Desktop/DickBiscuit'
                    FAC = np.load(os.path.join(plotDir1, '30_2.npy'))
                    dateB1 = FAC[0]
                    diameterB1 = FAC[1]
                    fitB1 = FAC[2]
                    FACB1 = FAC[3]
                else:
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial)+'avePiezo'
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = True


        print 'Subplot(' +str(j)+','+str(i)+')'
        
        if long == True:
            Zave = getRunsAverage(Z,6)
            zNew = Zave[0]
            bins = Zave[1]
            bins = range(bins)
            ax.set_xlabel('Hours (hr)')
        else:
            zNew = Z
            bins = X
            ax.set_xlabel('Hours (hr)')
            print X
            
        if j==0:
            ax.set_title(title, fontsize=20)
        print 'Plotting'
#         Z = np.transpose(Z)
        if type == 'FAC':
            first = dateB1[0]
            timesince = [(t-first)/3600 for t in dateB1]
            minutesince = [t.total_seconds() for t in timesince]
            labels = ax.get_xticklabels()
            for label in labels:
                label.set_rotation(90) 
                print label

            ax.plot(minutesince,diameterB1,'c')
            ax.plot(minutesince,fitB1,'k')
            font = {'family' : 'serif', 'size' : 12}
            ax.set_xlim(0,max(minutesince))
#             if i==1:
#                 ax.set_ylim(0.0022,0.0024)
            ax.text(minutesince[300],fitB1[300]+0.00005, 'FAC ='+str("{:5.4f}".format(FACB1))+' mm/year', fontdict=font)
        else:
            print'yikes'
            
            labels = ax.get_xticklabels()
            for label in labels:
                label.set_rotation(90) 
#             xticks = ax.xaxis.get_major_ticks()
#             xticks[0].label1.set_visible(False)
#             ax.set_ylim(0,)
            
            ax.set_ylim(100,100000)
            ax.semilogy()
            ax.contourf(bins,Y,zNew,norm=LogNorm())
#         ,norm=LogNorm()
        toc = time.clock()
        

#         yticks = ax.yaxis.get_major_ticks()
#         xticks[0].label1.set_visible(False)
#         yticks[0].label1.set_visible(False)
        print 'Subplot(' +str(j)+','+str(i)+') Plotted in: ' +str(toc-tic)
#         del Z, Y
        print 'Arrays Deleted'
        gc.collect()

# 
# plt.setp([a.get_yticklabels() for a in fig.axes[1:5]], visible=False)
# plt.setp([a.get_yticklabels() for a in fig.axes[5:10]], visible=False)
# plt.setp([a.get_yticklabels() for a in fig.axes], visible=False)
fig.tight_layout(pad = 1, h_pad = 0.75, w_pad = 0.18)
fig.set_facecolor('0.75')
# plt.subplots_adjust(top=0.90)
plt.savefig('Series3PSDCon.png')
print 'saved'
# toc = time.clock()
# print toc-tic
plt.cla()