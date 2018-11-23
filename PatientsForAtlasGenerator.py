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
totalPatient = len(patientNumber)

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
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 17)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 23))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 32)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 38))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 43)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 47))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 48)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 52))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 53)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 57))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 62)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 68))])
subsetBodyList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 77)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 83))])
    # add prostateVolumes subset
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 17)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 23))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 32)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 38))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 43)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 47))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 48)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 52))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 53)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 57))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 62)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 68))])
subsetProstateList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 77)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 83))])
    # add rectumVolumes subset
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 17)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 23))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 32)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 38))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 43)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 47))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 48)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 52))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 53)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 57))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 62)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 68))])
subsetRectumList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 77)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 83))])

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
 
