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

#Find percentile 20,35,45,50,55,65,80
print(bodyVolume.quantile([.2, .35, .45, .5, .55, .65, .80]))

#define quantiles
twentyPC = np.percentile(bodyVolume, 20) # return 50th percentile, e.g median.
thirtyFivePC = np.percentile(bodyVolume, 35) # return 50th percentile, e.g median.
fourtyFivePC = np.percentile(bodyVolume, 45) # return 50th percentile, e.g median.
fiftyPC = np.percentile(bodyVolume, 50) # return 50th percentile, e.g median.
fiftyFivePC = np.percentile(bodyVolume, 55) # return 50th percentile, e.g median.
sixtyFivePC = np.percentile(bodyVolume, 65) # return 50th percentile, e.g median.
eightyPC = np.percentile(bodyVolume, 80) # return 50th percentile, e.g median.

#Create subsets
patientSubset1 = AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= twentyPC) & (AdmirePatientAtlas.bodyVolume < thirtyFivePC)]
patientSubset2 = AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= thirtyFivePC) & (AdmirePatientAtlas.bodyVolume < fourtyFivePC)]
patientSubset3 = AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= fourtyFivePC) & (AdmirePatientAtlas.bodyVolume < fiftyPC)]
patientSubset4 = AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= fiftyPC) & (AdmirePatientAtlas.bodyVolume < fiftyFivePC)]
patientSubset5 = AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= fiftyFivePC) & (AdmirePatientAtlas.bodyVolume < sixtyFivePC)]
patientSubset6 = AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= sixtyFivePC) & (AdmirePatientAtlas.bodyVolume < eightyPC)]
ExtremePatient = AdmirePatientAtlas[lambda AdmirePatientAtlas:(AdmirePatientAtlas.bodyVolume >= eightyPC) & (AdmirePatientAtlas.bodyVolume < twentyPC)]

# sort subsets - I don't know whether this is necessary?
patientSubset1 = patientSubset1.sort_values(by=['bodyVolume'])
patientSubset2 = patientSubset2.sort_values(by=['bodyVolume'])
patientSubset3 = patientSubset3.sort_values(by=['bodyVolume'])
patientSubset4 = patientSubset4.sort_values(by=['bodyVolume'])
patientSubset5 = patientSubset5.sort_values(by=['bodyVolume'])
patientSubset6 = patientSubset6.sort_values(by=['bodyVolume'])
ExtremePatient = ExtremePatient.sort_values(by=['bodyVolume'])
# print(patientSubset1)
# print(patientSubset2)


#Select a random Patient from subsets ...
x = patientSubset1.iloc[np.random.random_integers(0, len(patientSubset1), 1)]	
print(x)

# print (x.bodyVolume)
# df_filteredA = AdmirePatientAtlas.query('9000<bodyVolume<12000') #makes a cut to dataset
# print(df_filteredA.head(n = 3))

