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
    help._init()
    try:
        index = cmd.checkCommand(sys.argv[1])
        if(index == -1):
            print(f'O comando {sys.argv[1]} é inválido, se você estiver com dificuldade, digite o nome do programa')
            print(f'digite o nome do programa e logo em seguida o comando help para saber mais sobre.')
            return
    #for arg in sys.argv[1:]:
        #print(cmd.checkCommand(arg))

_main()
