'''
    Module: Verificador de comandos
    Author: Lucas Campos Achcar
'''

shellCommands = {0:'help', 1:'generator', 2:'analyzer'}

'''
    Versão do Arquivo command.py
    Function: _version
    Args:
        None
    Return:
        None
'''
def _version():
    return '0.0.1'

'''
    Verifica os comandos dos argumentos e retorna o index
    Function: checkCommand
    Args:
        commandLine: Comando na qual deseja ser verificado
    Return:
        Command Index
'''
def checkCommand(commandLine):
    for v in shellCommands:
        if commandLine == shellCommands[v]:
            return v
    return -1
            
print(f'Command Module Version: {_version()}')
