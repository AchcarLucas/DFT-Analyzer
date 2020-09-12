'''
    Module: Verificador de comandos
    Author: Lucas Campos Achcar
'''

shellCommands = {0:'help', 1:'generator', 2:'analyzer'}

def _version():
    return '0.0.1'

def checkCommand(commandLine):
    for v in shellCommands:
        if commandLine == shellCommands[v]:
            return v
    return -1
            
