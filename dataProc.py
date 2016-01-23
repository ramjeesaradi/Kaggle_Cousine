'''
Created on 30-Nov-2015

@author: ramjeesaradi
'''
import json
import numpy as np
from macpath import split
from functions import json2mat
from os import chdir
# import yaml

chdir('/Users/ramjeesaradi/Desktop/Kaggle/Cousine')

print "this is test message."
with open("train.json") as trainDta:
    d = json.load(trainDta)
    trainDta.close()
dta = json2mat(d)
darray = np.array(dta)
# length of array 6716
darray[1:10,0:5]

