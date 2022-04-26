import subprocess
import datetime
from pprint import pprint

class SRIQ_settings:
    def __init__(self):
        self.settings = {
                "studyName":"LU_LUAD_SRIQ",
                "studyPath":"/home/Researcher/SRIQ/software/data/",
                "inFileName":"GeneData_AC_fpkm_mc_log2_nz",
                "outPath":"/home/Researcher/SRIQ/software/output/",
                "distCutOff":[0.8, 0.79, 0.78, 0.77, 0.76, 0.75, 0.74, 0.73, 0.72, 0.71, 0.7, 0.69, 0.68, 0.67, 0.66, 0.65, 0.64, 0.63, 0.62, 0.61, 0.6, 0.59, 0.58, 0.57, 0.56, 0.55, 0.54, 0.53, 0.52],
                "permutations":10000,
                "iterations":10,
                "spiral":"TRUE",
                "minClusterSize":0,
                "minBagSize":1200,
                "method":"PEARSON",
            }

    def get_settings(self):
        return self.settings

    def change_property(self, property, value):
        self.settings[property] = value



def runSRIQ(studyName, studyPath, inFileName, outPath, **args):
    properties = SRIQ_settings()
    
    args = [(str(x),args[x]) for x in args]
    arguments = [("studyName",studyName), 
                ("studyPath",studyPath), 
                ("inFileName",inFileName), 
                ("outPath",outPath), 
                *args]
    for argument in arguments:
        properties.change_property(argument[0], argument[1])


    pprint (properties.get_settings())

if __name__ == "__main__":
    try: 
        runSRIQ()
    except TypeError as e:
        print(e)
        print("Make sure to include all the required arguments")
    except Exception as e:
        print(e)
        print("Unknown Error")