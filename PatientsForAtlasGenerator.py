#Thomas Created: 19/11/2018
#Finished: 23/11/2018

#Notes:

#Please change directory for .cvs file. I am unsure whether to sort the subsets before randomly selecting
#And I am still unsure about this mehod being a good method
#Change the 3rd input on the random patient gerator to select more then 1 patient

#import librarys
import random
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

#Define Random Sample function
def some(x, n):
    return x.iloc[random.sample(x.index, n)]

# Load Prostate Volume data
AdmirePatientAtlas = pd.read_csv(r"C:\Users\Alexander\Documents\4th_year\Lab\Lab work\19.11.2018\PatientVolumeDataForATLAS.csv")

#Access Colums: patientNumber, patientID, prostteVolume, rectumVolume, bodyVolume
bodyVolume = AdmirePatientAtlas["bodyVolume"]
prostateVolume = AdmirePatientAtlas["prostateVolume"]
patientNumber = AdmirePatientAtlas["patientNumber"]

#size of table
totalPatient = len(patientNumber)

#Sorted tables
sortByBodyVolume = AdmirePatientAtlas.sort_values(by=['bodyVolume'])
sortByProstateVolume = AdmirePatientAtlas.sort_values(by=['prostateVolume'])
#print(sortByBodyVolume.head(n=3))
#print(sortByProstateVolume.head(n=3))

# Create a list for subsets around the percentiles
subsetList = []

# Add subsets to subset list (just makes it easier to iterate over and cuts down a bit of code)
    # add bodyVolumes subset
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 17)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 23))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 32)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 38))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 43)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 47))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 48)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 52))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 53)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 57))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 62)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 68))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= np.percentile(bodyVolume, 77)) & (AdmirePatientAtlas.bodyVolume <= np.percentile(bodyVolume, 83))])
    # add prostateVolumes subset
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 17)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 23))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 32)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 38))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 43)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 47))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 48)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 52))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 53)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 57))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 62)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 68))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.prostateVolume >= np.percentile(prostateVolume, 77)) & (AdmirePatientAtlas.prostateVolume <= np.percentile(prostateVolume, 83))])
    # add rectumVolumes subset
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 17)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 23))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 32)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 38))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 43)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 47))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 48)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 52))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 53)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 57))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 62)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 68))])
subsetList.append(AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.rectumVolume >= np.percentile(rectumVolume, 77)) & (AdmirePatientAtlas.rectumVolume <= np.percentile(rectumVolume, 83))])

# create a list to hold the patient ID's of those chosen to be in the ATLAS
atlasPatients = [] 

# Select a random Patient from each subset in subsetList, add the ID of that patient to the list of atlasPatients
for i in range(0, 21):
    RandomPatient = subsetList[i].iloc[np.random.randint(0, len(subsetList[i]), 1)]
    atlasPatients.append(RandomPatient)
    
# print a list of atlas patients
for i in range(0, len(atlasPatients)):
    print(atlasPatients[i].patientList)

