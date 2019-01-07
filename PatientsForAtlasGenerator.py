#Thomas Created: 19/11/2018
#Finished: 23/11/2018

#Notes:

#Please change directory for .cvs file. I am unsure whether to sort the subsets before randomly selecting
#And I am still unsure about this mehod being a good method
#Change the 3rd input on the random patient gerator to select more then 1 patient

#import librarys
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Define Random Sample function
def some(x, n):
    return x.iloc[random.sample(x.index, n)]

# Load Prostate Volume data
AdmirePatientAtlas = pd.read_csv(r"C:\Users\Alexander\Documents\4th_year\Lab\Lab work\19.11.2018\PatientVolumeDataForATLAS.csv")

#Access Colums: patientNumber, patientID, prostteVolume, rectumVolume, bodyVolume
bodyVolume = AdmirePatientAtlas["bodyVolume"]
prostateVolume = AdmirePatientAtlas["prostateVolume"]
rectumVolume = AdmirePatientAtlas["rectumVolume"]
patientNumber = AdmirePatientAtlas["patientNumber"]

#size of table
totalPatient = 50

#Sorted tables
sortByBodyVolume = AdmirePatientAtlas.sort_values(by=['bodyVolume'])
sortByProstateVolume = AdmirePatientAtlas.sort_values(by=['prostateVolume'])
#print(sortByBodyVolume.head(n=3))
#print(sortByProstateVolume.head(n=3))

# Create a list for subsets around the percentiles
subsetBodyList = []
subsetProstateList = []
subsetRectumList = []

# Add subsets to subset list (just makes it easier to iterate over and cuts down a bit of code)
    # add bodyVolumes subset
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 12)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 18))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 27)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 33))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 38)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 42))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 44)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 46))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 49)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 51))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 54)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 56))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 58)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 62))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 67)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 73))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 82)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 88))])
    # add prostateVolumes subset
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 12)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 18))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 27)) & (AdmirePatientAtlas.prostateVolume<= np.percentile(prostateVolume, 33))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 38)) & (AdmirePatientAtlas.prostateVolume<= np.percentile(prostateVolume, 42))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 44)) & (AdmirePatientAtlas.prostateVolume<= np.percentile(prostateVolume, 46))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 49)) & (AdmirePatientAtlas.prostateVolume<= np.percentile(prostateVolume, 51))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 54)) & (AdmirePatientAtlas.prostateVolume<= np.percentile(prostateVolume, 56))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 58)) & (AdmirePatientAtlas.prostateVolume<= np.percentile(prostateVolume, 62))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 67)) & (AdmirePatientAtlas.prostateVolume<= np.percentile(prostateVolume, 73))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 82)) & (AdmirePatientAtlas.prostateVolume<= np.percentile(prostateVolume, 88))])
    # add rectumVolumes subset
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume>= np.percentile(rectumVolume, 12)) & (AdmirePatientAtlas.rectumVolume<= np.percentile(rectumVolume, 18))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume>= np.percentile(rectumVolume, 27)) & (AdmirePatientAtlas.rectumVolume<= np.percentile(rectumVolume, 33))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume>= np.percentile(rectumVolume, 38)) & (AdmirePatientAtlas.rectumVolume<= np.percentile(rectumVolume, 42))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume>= np.percentile(rectumVolume, 44)) & (AdmirePatientAtlas.rectumVolume<= np.percentile(rectumVolume, 46))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume>= np.percentile(rectumVolume, 49)) & (AdmirePatientAtlas.rectumVolume<= np.percentile(rectumVolume, 51))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume>= np.percentile(rectumVolume, 54)) & (AdmirePatientAtlas.rectumVolume<= np.percentile(rectumVolume, 56))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume>= np.percentile(rectumVolume, 58)) & (AdmirePatientAtlas.rectumVolume<= np.percentile(rectumVolume, 62))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume>= np.percentile(rectumVolume, 67)) & (AdmirePatientAtlas.rectumVolume<= np.percentile(rectumVolume, 73))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume>= np.percentile(rectumVolume, 82)) & (AdmirePatientAtlas.rectumVolume<= np.percentile(rectumVolume, 88))])

# create a list to hold the patient ID's of those chosen to be in the ATLAS
atlasBodyPatients = [] 
atlasProstatePatients = [] 
atlasRectumPatients = [] 

# Select a random Patient from each subset in subsetList, add the ID of that patient to the list of atlasPatients
for i in range(0, len(subsetBodyList)):
    atlasBodyPatients.append(subsetBodyList[i].iloc[np.random.randint(0, len(subsetBodyList[i]), 1)])
    atlasProstatePatients.append(subsetProstateList[i].iloc[np.random.randint(0, len(subsetProstateList[i]), 1)])
    atlasRectumPatients.append(subsetRectumList[i].iloc[np.random.randint(0, len(subsetRectumList[i]), 1)])

# instead of making these lists, concatonate them for ease
bodyAtlas = pd.concat(atlasBodyPatients)
prostateAtlas = pd.concat(atlasProstatePatients)
rectumAtlas = pd.concat(atlasRectumPatients)
    
# print a list of atlas patients
print(bodyAtlas,'\n',prostateAtlas,'\n',rectumAtlas)

# display histograms, overlapping to show the original data and where the selected data lays upon it
# body volumes
plt.hist(bodyVolume, totalPatient, alpha=0.5, label='All patients')
plt.hist(bodyAtlas["bodyVolume"], totalPatient, alpha=0.5, label='Selected patients')
plt.ylabel('Frequency')
plt.xlabel('Patient body contour volume $\mathregular{cm^3}$')
plt.legend(loc='upper right')
plt.show()
# prostate volumes
plt.hist(prostateVolume, totalPatient, alpha=0.5, label='All patients')
plt.hist(prostateAtlas["prostateVolume"], totalPatient, alpha=0.5, label='Selected patients')
plt.ylabel('Frequency')
plt.xlabel('Patient prostate contour volume $\mathregular{cm^3}$')
plt.legend(loc='upper right')
plt.show()
# rectum volumes
plt.hist(rectumVolume, totalPatient, alpha=0.5, label='All patients')
plt.hist(rectumAtlas["rectumVolume"], totalPatient, alpha=0.5, label='Selected patients')
plt.ylabel('Frequency')
plt.xlabel('Patient rectum contour volume $\mathregular{cm^3}$')
plt.legend(loc='upper right')
plt.show()
 
