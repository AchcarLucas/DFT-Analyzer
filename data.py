'''
    Module: Data (Save and Load)
    Author: Lucas Campos Achcar
'''

import pickle

def _version():
    return '0.0.1'

'''
    Serialização dos dados de um objeto ou classe para um arquivo de dados
    Function: saveData
    Arg:
        file_name: Nome do arquivo para onde será salvo
        data: Objeto a ser serializado
'''
def saveData(file_name, data):
    with open(file_name, 'wb') as output:
            pickle.dump(data, output, pickle.HIGHEST_PROTOCOL)

'''
    Reserialização de um objeto ou classe a partir de um arquivo de dados
    Function: loadData
    Arg:
        file_name: Nome do arquivo onde os dados estão
'''
def loadData(file_name):
    with open(file_name, 'rb') as input:
        return pickle.load(input)
    
