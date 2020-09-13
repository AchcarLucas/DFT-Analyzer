'''
    Programa: Analisador de Sinal
    Author: Lucas Campos Achcar
'''

import sys

import license
import generator as gen
import command as cmd
import help
import dft
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
        # Verifica se foi digitado o nome do arquivo no argumento
        try:
            file_name = sys.argv[2]
        except:
            print(f'[nome-arquivo] é obrigatório')
            return

        # Verifica se a taxa de amostragem foi digitado no argumento
        try:
            sample_rate = int(sys.argv[3])
        except:
            print(f'[taxa-de-amostragem] é obrigatório')
            return

        # Verifica se o tempo de exibição da onda foi digitada no argumento
        try:
            duration = int(sys.argv[4])
        except:
            print(f'[duração] é obrigatório')
            return

        frequencies = []
        magnetudes = []
        phases = []

        # Já foram 4 argumentos, falta o resto
        c_count = 5
        # Procura todos os argumentos da frequência
        for arg in sys.argv[c_count:]:
            c_count += 1
            if(arg != '-'):
                frequencies.append(float(arg))
                continue
            break

        # Procura todos os argumentos da magnetudes
        for arg in sys.argv[c_count:]:
            c_count += 1
            if(arg != '-'):
                magnetudes.append(float(arg))
                continue
            break

        # Procura todos os argumentos da fase
        for arg in sys.argv[c_count:]:
            c_count += 1
            if(arg != '-'):
                phases.append(float(arg))
                continue
            break

        print('------------------------------------')
        print(f'Frequências: {frequencies}')
        print(f'Magnetudes {magnetudes}')
        print(f'Fases {phases}')
        
        signal = gen.SignalGenerator(frequencies, magnetudes, phases, sample_rate, duration)
            
        if(gen.signalGenerator(file_name, signal)):
            print(f'Sinal gerado com sucesso, o arquivo foi gerado em {file_name}')
        else:
            print(f'Desculpe, não foi possível gerar o sinal, verifique o comando novamente')
            
        del signal
        print('------------------------------------')
    # Analyzer
    elif(c_index == 2):
        # Verifica se foi digitado o nome do arquivo de dados no argumento
        try:
            file_name = sys.argv[2]
        except:
            print(f'[nome-arquivo] é obrigatório')
            return

        # Verifica se foi digitado a cor de exibição, se não, adiciona o padrão
        try:
            color = sys.argv[3]
        except:
            color = 'red'

        interval_analyzer = [0, 0]

        # Verifica se foi digitado o limite inicial da frequência, coloca padrão 0
        try:
            interval_analyzer[0] = int(sys.argv[4])
        except:
            interval_analyzer[0] = 0

        #  Verifica se foi digitado o limite final da frequência, coloca padrão 100
        try:
            interval_analyzer[1] = int(sys.argv[5])
        except:
            interval_analyzer[1] = 100

        # Pega as informações carregando o arquivo de dados
        signal = gen.data.loadData(file_name)

        out_data = dft.DFT(signal.data, signal.sample_rate, interval_analyzer)

        '''
            ------------------------------- Análise de Frequência -------------------------------------
        '''

        # Normaliza a magnetude
        mag = [v._mag for v in out_data]

        # Adiciona o gráfico com suas legendas
        axies_1 = graphic.getAxiesData('DFT Analyzer', 'Frequência (Hz)', 'Magnetude', [10, 6])

        max_value_mag = max(mag) + 1;

        # Configuração dos eixos (exibição)
        x_major_ticks = np.arange(0, interval_analyzer[1], np.ceil(interval_analyzer[1]*(1 / interval_analyzer[1])))
        y_major_ticks = np.arange(0, max_value_mag, np.ceil(max_value_mag*(1 / max_value_mag)))

        # Exibe os valores limites superiores e inferiores
        axies_1.set_xticks(x_major_ticks, minor=True)
        axies_1.set_yticks(y_major_ticks, minor=True)

        # Limita os eixos para exibir até a última frequência
        axies_1.set_xlim(interval_analyzer[0], interval_analyzer[1])
        axies_1.set_ylim(0, max_value_mag)

        # Configura o Grid
        axies_1.grid(which='both')
        
        axies_1.grid(which='minor', alpha=1.0)
        axies_1.grid(which='major', alpha=1.0)

        # Exibe as linhas verticais das frequências
        for i in range(0, int(len(mag))):
            axies_1.vlines(i + interval_analyzer[0], 0, mag[i], lw=2, color=color)

        '''
            --------------------------------------------------------------------------------
        '''

        '''
            ------------------------------- Análise de Fase -------------------------------------
        '''

        # Gera a list de fases
        phases = [v._phase for v in out_data]
        
        # Normaliza a fase
        for i in range(0, len(phases)):
            if(phases[i] > 0.1):
                phases[i] = 180 - (phases[i] * (180 / np.pi))

        # Adiciona o gráfico com suas legendas
        axies_2 = graphic.getAxiesData('Phase Analyzer', 'Frequências (Hz)', 'Fases (º)', [10, 6])

        max_value_phase = max(phases) + 5

        # Configuração dos eixos (exibição)
        x_major_ticks = np.arange(0, interval_analyzer[1], np.ceil(interval_analyzer[1]*(1 / interval_analyzer[1])))
        y_major_ticks = np.arange(0, max_value_phase, np.ceil(max_value_phase*(1 / max_value_phase)))

        # Exibe os valores limites superiores e inferiores
        axies_2.set_xticks(x_major_ticks, minor=True)
        axies_2.set_yticks(y_major_ticks, minor=True)

        # Limita os eixos para exibir até a última frequência
        axies_2.set_xlim(interval_analyzer[0], interval_analyzer[1])
        axies_2.set_ylim(0, max_value_phase)

        # Configura o Grid
        axies_2.grid(which='both')
        
        axies_2.grid(which='minor', alpha=1.0)
        axies_2.grid(which='major', alpha=1.0)

        # Exibe as linhas verticais das fases
        for i in range(0, int(len(phases))):
            axies_2.vlines(i + interval_analyzer[0], 0, phases[i], lw=2, color=color)

        '''
            --------------------------------------------------------------------------------
        '''
            
        graphic.showGraphic()

    # Signal Data
    elif(c_index == 3):
        try:
            file_name = sys.argv[2]

            # Verifica se o argumento da cor existe, se não, mantém padrão
            try:
                arg_color = sys.argv[3]
            except:
                arg_color = 'red'

            time_limit_display = [0, 0]

            # Verifica se o argumento do limite de tempo inferior existe, se não, mantém padrão
            try:
                time_limit_display[0] = float(sys.argv[4])
            except:
                time_limit_display[0] = 0.0
                
            # Le o arquivo indicado, faz a unserialized para ter acesso aos dados
            signal = gen.data.loadData(file_name)

            # Verifica se o argumento do limite de tempo superior existe, se não, mantém padrão
            try:
                time_limit_display[1] = float(sys.argv[5])
            except:
                time_limit_display[1] = signal.duration

            # Cria o Axies (gráfico)
            axies_1 = graphic.getAxiesData('Wave Signal', 'Time (s)', 'Amplitude', [10, 6])

            # Plota os textos referentes ao sample_rate, duration e total_data
            graphic.drawText(0.8, 0.9, f'SAMPLE RATE {signal.sample_rate}', axies_1, 'blue', 0.4);
            graphic.drawText(0.8, 0.83, f'DURATION {signal.duration} (s)', axies_1, 'red', 0.4);
            graphic.drawText(0.8, 0.76, f'TOTAL DATA(S) {len(signal.data)}', axies_1, 'green', 0.4);

            # Limita o gráfico entre 0 até duration (segundos)
            axies_1.set_xlim(time_limit_display[0], time_limit_display[1])

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
        
    # Wav Data
    elif(c_index == 4):
        # Verifica se foi digitado o nome do arquivo wav no argumento
        try:
            wav_file_name = sys.argv[2]
        except:
            print(f'[nome-wav] é obrigatório')
            return

        # Verifica se foi digitado o nome do arquivo data no argumento
        try:
            file_name = sys.argv[3]
        except:
            print(f'[nome-arquivo-data] é obrigatório')
            return

        # Gera o arquivo de dados da onda
        if(gen.createSignalFromWav(wav_file_name, file_name)):
            print(f'Sinal gerado com sucesso, o arquivo foi gerado em {file_name}')
        else:
            print(f'Desculpe, não foi possível gerar o sinal, verifique o comando novamente')
            
    # Nenhum comando encontrado
    else:
        help.inv_args(sys.argv[1])

'''
    Inicializa o Programa
'''
_main()
