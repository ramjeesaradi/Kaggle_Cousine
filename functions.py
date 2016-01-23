'''
Created on 01-Jan-2016

@author: ramjeesaradi

'''
# from multiprocessing import Pool

def getRow(inglst,x):
    return [x["id"]] + boolvec(x["ingredients"],inglst) + [x["cuisine"]]

def json2mat(jsonobj):
    #here goes code for getting all the json into single records.
    inglst = ingrset(jsonobj)
#     p = Pool(processes = 8)
    return map(lambda x: [x["id"]] + boolvec(x["ingredients"],inglst) + [x["cuisine"]], jsonobj)

def boolvec(ingr,inglst):
#     p = Pool(processes = 8)
    return map(lambda x:x in ingr ,inglst)

def ingrset(jsonobj):
#     p = Pool(processes = 8)
    return reduce(lambda c,x: list(set(c+ x["ingredients"])) , jsonobj, [])
    
    