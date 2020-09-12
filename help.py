'''
    Module: Ajuda
    Author: Lucas Campos Achcar
'''

def _version():
    return '0.0.1'

def _init():
    print('digite help para mais informações')
    
def c_help():
    print('help                              -> abre a tela de ajuda')
    print('gen [nome-arquivos] [frequências] -> gerar sinais com as frequências definidas, ex: ./gen 5 12')
    print('          irá gerar um arquivo com as frequências 5 hz e 12 hz')
