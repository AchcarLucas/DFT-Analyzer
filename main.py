'''
    Programa: Analisador de Sinal
    Author: Lucas Campos Achcar
'''

import sys

import license
import generator as gen
import command as cmd
import help
import graphic

'''
    Loop Principal
    Function: _main
    Args:
        None
    Return:
        None
'''
def _main():
    # Verifica se o comando é válido
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

'''
    Inicializa o Programa
'''

#_main()

'''
    Test
'''

test = gen.SignalGenerator([1], [5, 5, 5], [0, 90, 0], 100, 2)
gen.signalGenerator('test/test.data', test)
del test
signal = gen.data.loadData('test/test.data')
print(signal.data)
graphic.drawGraphicData('Wave Signal', 'Time (10^-2 s)', 'Magnetude', [10, 5], signal.data)
graphic.drawGraphicData('Wave Signal', 'Time (10^-2 s)', 'Magnetude', [5, 5], signal.data)
graphic.showGraphic()
