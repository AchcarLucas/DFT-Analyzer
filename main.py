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
import numpy as np

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
    # Signal Data
    elif(c_index == 3):
        try:
            file_name = sys.argv[2]
            
            try:
                arg_color = sys.argv[3]
            except:
                arg_color = 'red'
                
            # Le o arquivo indicado, faz a unserialized para ter acesso aos dados
            signal = gen.data.loadData(file_name)

            # Cria o Axies (gráfico)
            axies_1 = graphic.getAxiesData('Wave Signal', 'Time (s)', 'Amplitude', [10, 6])

            # Plota os textos referentes ao sample_rate, duration e total_data
            graphic.drawText(0.8, 0.9, f'SAMPLE RATE {signal.sample_rate}', axies_1, 'blue', 0.4);
            graphic.drawText(0.8, 0.83, f'DURATION {signal.duration} (s)', axies_1, 'red', 0.4);
            graphic.drawText(0.8, 0.76, f'TOTAL DATA(S) {len(signal.data)}', axies_1, 'green', 0.4);

            # Limita o gráfico entre 0 até duration (segundos)
            axies_1.set_xlim(0, signal.duration)

            # Manda para o plot exibir a wave no intervalo dado (normalizado)
            axies_1.plot(np.arange(0, signal.duration, 1 / (signal.sample_rate))[:len(signal.data)], signal.data, label='normalized', color=arg_color)

            # Exibe todos os gráficos
            graphic.showGraphic()
            
            del signal
        except:
            print(f'----------------------------------------------------------------')
            print(f'Não foi possível executar o comando {cmd.shellCommands[c_index]}')
            print(f'Verifique os parametros e se o nome do arquivo foi digitado corretamente')
            print(f'Para mais informações use o argumento help')
            print(f'----------------------------------------------------------------')
            return
    else:
        help.inv_args(sys.argv[1])

'''
    Inicializa o Programa
'''

_main()

'''
    Test
'''

'''
test = gen.SignalGenerator([1], [5, 5, 5], [0, 0, 0], 100, 3)
gen.signalGenerator('test/test.data', test)
del test
signal = gen.data.loadData('test/test.data')
print(signal.data)
axies_1 = graphic.getAxiesData('Wave Signal', 'Samples', 'Magnetude', [10, 6])

graphic.drawText(0.8, 0.9, f'SAMPLE RATE {signal.sample_rate}', axies_1, 'blue', 0.4);
graphic.drawText(0.8, 0.83, f'DURATION {signal.duration} (s)', axies_1, 'red', 0.4);
graphic.drawText(0.8, 0.76, f'TOTAL SAMPLE(S) {len(signal.data)}', axies_1, 'green', 0.4);


axies_1.set_xlim(0, signal.duration)
axies_1.plot(np.arange(0, signal.duration, 1 / (signal.sample_rate))[:len(signal.data)], signal.data, label='normalized')

graphic.showGraphic()
'''
