'''
    Module: Data (Save and Load)
    Author: Lucas Campos Achcar
'''

import pickle

def _version():
    return '0.0.1'

def saveData(file_name, data):
    with open(file_name, 'wb') as output:
            pickle.dump(data, output, pickle.HIGHEST_PROTOCOL)

def loadData(file_name):
    with open(file_name, 'rb') as input:
        return pickle.load(input)
    
