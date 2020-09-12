'''
    Programa: Analisador de Sinal
    Author: Lucas Campos Achcar
'''

import sys

import generator as gen
import command as cmd
import help

def _main():
    print(f'Generator Module Version: {gen._version()}')
    print(f'Command Module Version: {cmd._version()}')
    print(f'Help Module Version: {help._version()}')
    
    try:
        c_index = cmd.checkCommand(sys.argv[1])
    except:
        help._except()
        return

    # Help
    if(c_index == 0):
        help.c_help()
    # Generator
    elif(c_index == 1):
        print('Generator')
        for arg in sys.argv[2:]:
            print(arg)
    # Analyzer
    elif(c_index == 2):
        print('Analyzer')
        for arg in sys.argv[2:]:
            print(arg)
    else:
        help.inv_args(sys.argv[1])

_main()
