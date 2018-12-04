# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:53:36 2018

@author: Alexander
"""

#Created: 27/11/2018

#import librarys
import numpy as np
import pandas as pd
import seaborn as sns; sns.set()
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

#import seaborn as sns

# Load patients list data
AdmirePatientList = pd.read_csv(r"C:/Users/Alexander/Documents/4th_year/Lab\Lab work/29.11.2018 NewAutoContours/GlobalDifference/AllData19Frac.csv")

# Access patient ID numbers and recurrence
PatientID = AdmirePatientList["patientList"]
Recurrence = AdmirePatientList["reccurrence"]

# Create containers to store patients prostate maps
patientMapRecurrenceContainer = []
patientMapNonRecurrenceContainer = []

# Get total number of patients
totalPatients = PatientID.size

atlas = {'200806930','201010804', '201304169', '201100014', '201205737','201106120', '201204091', '200803943', '200901231', '200805565', '201101453', '200910818', '200811563','201014420'}
corrupt = {'196708754','200801658'}

# Read in the patients map and store in correct container
for x in range(0, totalPatients):
    name = str(PatientID.iloc[x])
    patientMap = pd.read_csv(r"C:/Users/Alexander/Documents/4th_year/Lab/Lab work/29.11.2018 NewAutoContours/RadialDifference/"+name+".csv",header=None)
    
    if name in atlas or name in corrupt:
        print("Not including patient: " + name)
    # Reacurrence
    elif Recurrence.loc[x] == '1':
        patientMapRecurrenceContainer.append(patientMap)
    #    plt.imshow(patientMap, cmap='hot', interpolation='nearest')
    #    plt.show()
    
        # Non Recurrence
    else:
        patientMapNonRecurrenceContainer.append(patientMap)
  
        
        
# Calculate Mean and Variance Heat map for patient recurrence
totalRecurrencePatients = pd.concat(patientMapRecurrenceContainer)
by_row_indexRec = totalRecurrencePatients.groupby(totalRecurrencePatients.index)
meanRecurrence = by_row_indexRec.mean()
varRecurrence = by_row_indexRec.var()

# Calculate Mean and Variance Heat map for patient non-recurrence
totalNonRecurrencePatients = pd.concat(patientMapNonRecurrenceContainer)
by_row_indexNonRec = totalNonRecurrencePatients.groupby(totalNonRecurrencePatients.index)
meanNonRecurrence = by_row_indexNonRec.mean()
varNonRecurrence = by_row_indexNonRec.var()

# Display 2D Heat maps
#f, (recurrenceMean, recurrenceVar) = plt.subplots(1, 2)
recurrenceMean = sns.heatmap(meanRecurrence, center=0)
recurrenceMean.set(ylabel='Theta $/dot{\Theta}$', xlabel='Azimutal $\phi$')
fig = recurrenceMean.get_figure()
fig.savefig('C:/Users/Alexander/Documents/4th_year/Lab/Lab work/3.12.2018 Analysis/Local Analysis/meanRecurrenceMap.png')
fig.clear()

recurrenceVar = sns.heatmap(varRecurrence, center=0)
recurrenceVar.set(ylabel='Theta $\dot{\Theta}$', xlabel='Azimutal $\phi$')
fig2 = recurrenceVar.get_figure()
fig2.savefig('C:/Users/Alexander/Documents/4th_year/Lab/Lab work/3.12.2018 Analysis/Local Analysis/varRecurrenceMap.png')
fig2.clear()

nonRecurrenceMean = sns.heatmap(meanNonRecurrence, center=0)
nonRecurrenceMean.set(ylabel='Theta $\dot{\Theta}$', xlabel='Azimutal $\phi$')
fig3 = nonRecurrenceMean.get_figure()
fig3.savefig('C:/Users/Alexander/Documents/4th_year/Lab/Lab work/3.12.2018 Analysis/Local Analysis/meanNonRecurrenceMap.png')
fig3.clear()

nonRecurrenceVar = sns.heatmap(varNonRecurrence, center=0)
nonRecurrenceVar.set(ylabel='Theta $\dot{\Theta}$', xlabel='Azimutal $\phi$')
fig4 = nonRecurrenceVar.get_figure()
fig4.savefig('C:/Users/Alexander/Documents/4th_year/Lab/Lab work/3.12.2018 Analysis/Local Analysis/varNonRecurrenceMap.png')
fig4.clear()

DifferenceInMean = meanRecurrence - meanNonRecurrence
DifferenceInMeanGraph = sns.heatmap(DifferenceInMean, center=0)
DifferenceInMeanGraph.set(ylabel='Theta $\dot{\Theta}$', xlabel='Azimutal $\phi$')
fig5 = DifferenceInMeanGraph.get_figure()
fig5.savefig('C:/Users/Alexander/Documents/4th_year/Lab/Lab work/3.12.2018 Analysis/Local Analysis/differenceMeanMap.png')
fig5.clear()

DifferenceInvar = varRecurrence + varNonRecurrence
DifferenceInvarGraph = sns.heatmap(DifferenceInvar, center=0)
DifferenceInvarGraph.set(ylabel='Theta $dot{Theta}$', xlabel='Azimutal $phi$')
fig6 = DifferenceInvarGraph.get_figure()
fig6.savefig('C:/Users/Alexander/Documents/4th_year/Lab/Lab work/3.12.2018 Analysis/Local Analysis/differencevarMap.png')
fig6.clear()

DifferenceInSignfi = DifferenceInMean / np.sqrt(DifferenceInvar)
DifferenceInSignfiGraph = sns.heatmap(DifferenceInSignfi, center=0)
DifferenceInSignfiGraph.set(ylabel='Theta $dot{Theta}$', xlabel='Azimutal $phi$')
fig7 = DifferenceInSignfiGraph.get_figure()
fig7.savefig('C:/Users/Alexander/Documents/4th_year/Lab/Lab work/3.12.2018 Analysis/Local Analysis/differenceSignfiMap.png')
fig7.clear()



# =============================================================================
# # 3D figures
# phi = np.arange(0, 360, 7.2)
# theta = np.arange(-90,90,3.6)
# 
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = phi
# Y = theta
# X, Y = np.meshgrid(X, Y)
# Z = DifferenceInMean
# 
# # Plot the 3D surface
# ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
# 
# # Plot projections of the contours for each dimension.  By choosing offsets
# # that match the appropriate axes limits, the projected contours will sit on
# # the 'walls' of the graph
# cset = ax.contourf(X, Y, Z, zdir='z', offset=-0.5, cmap=cm.coolwarm)
# cset = ax.contourf(X, Y, Z, zdir='x', offset=0, cmap=cm.coolwarm)
# cset = ax.contourf(X, Y, Z, zdir='y', offset=90, cmap=cm.coolwarm)
# 
# ax.set_xlim(0, 360)
# ax.set_ylim(-90, 90)
# ax.set_zlim(-0.5, 0.5)
# 
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# 
# plt.show()
# =============================================================================
