for j in range(rowsSubplots):
    
            
    if j==0:
        type = 'avePiezo'
        valueZ = 'avePSDZ.npy'
        labelsd = 'Ave. Piezo (Hz)'
        trial = 'trial_1_Jan_2014'
        extraDir = 'avePiezo'
    elif j==1:
        type = 'avePiezo'
        valueZ = 'avePSDZ.npy'
        labelsd = 'Ave. Piezo (Hz)'
        trial = 'trial_2_June_2014'
        extraDir = 'avePiezo'
    else:
        type = 'avePiezo'
        valueZ = 'avePSDZ.npy'
        labelsd = 'Ave. Piezo (Hz)'
        trial = 'trial_3_Sept_2014'
        extraDir = '10_14_2014/avePiezo'
        
    long = False

        
    for i in range(columnsSubplots):
        
        tic = time.clock() 
        ax = plt.subplot2grid((rowsSubplots,columnsSubplots), (j,i))
        
        if i%2 ==0: 
            if i==0: 
                ax.set_ylabel(labelsd, fontsize=16)
                trial = trial
                flow = '20'
                o2 = 'high'
                temp = '95'
                
                title = '0.77 l/min'
                
                if type == 'FAC':
                    ax.set_ylabel('FAC Rate (mm/year)',fontsize=16)
                    plotDir1 = '/Users/cathymartin/Desktop/DickBiscuit'
                    FAC = np.load(os.path.join(plotDir1, '30_2.npy'))
                    dateB1 = FAC[0]
                    diameterB1 = FAC[1]
                    fitB1 = FAC[2]
                    FACB1 = FAC[3]
                else:
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+extraDir
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = False
                
            elif i==2:
                trial = trial
                flow = '50'
                o2 = 'high'
                temp = '95'
                
                title = '1.93 l/min'
                
                if type == 'FAC':
                    plotDir1 = '/Users/cathymartin/Desktop/DickBiscuit'
                    FAC = np.load(os.path.join(plotDir1, '30_2.npy'))
                    dateB1 = FAC[0]
                    diameterB1 = FAC[1]
                    fitB1 = FAC[2]
                    FACB1 = FAC[3]
                else:
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+extraDir
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = False
                
            else:
                trial = trial
                flow = '80'
                o2 = 'high'
                temp = '95'
                
                title = '3.09 l/min'
                
                if type == 'FAC':
                    plotDir1 = '/Users/cathymartin/Desktop/DickBiscuit'
                    FAC = np.load(os.path.join(plotDir1, '30_2.npy'))
                    dateB1 = FAC[0]
                    diameterB1 = FAC[1]
                    fitB1 = FAC[2]
                    FACB1 = FAC[3]
                else:
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+extraDir
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = False
             
        else:
            if i==1:   
                trial = trial
                flow = '35'
                o2 = 'high'
                temp = '95'
                
                title = '1.35 l/min'
                
                if type == 'FAC':
                    plotDir1 = '/Users/cathymartin/Desktop/DickBiscuit'
                    FAC = np.load(os.path.join(plotDir1, '30_2.npy'))
                    dateB1 = FAC[0]
                    diameterB1 = FAC[1]
                    fitB1 = FAC[2]
                    FACB1 = FAC[3]
                else:
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+extraDir
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = False
                
            elif i==3:
                trial = trial
                flow = '65'
                o2 = 'high'
                temp = '95'
                
                title = '2.59 l/min'
                
                if type == 'FAC':
                    plotDir1 = '/Users/cathymartin/Desktop/DickBiscuit'
                    FAC = np.load(os.path.join(plotDir1, '30_2.npy'))
                    dateB1 = FAC[0]
                    diameterB1 = FAC[1]
                    fitB1 = FAC[2]
                    FACB1 = FAC[3]
                else:
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+extraDir
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = False
                
            else:
                trial = trial
                flow = '20'
                o2 = 'high'
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
                    plotDir1 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+type
                    plotDir2 = getDirectory(mainDir,flow,o2,temp,trial,flow_ramping=True)+extraDir
                    print plotDir1
                    X = np.load(os.path.join(plotDir2, 'avePSDX.npy'))
                    Y = np.load(os.path.join(plotDir2, 'avePSDY.npy'))
                    Z = np.load(os.path.join(plotDir1, valueZ))
                   
                    long = False