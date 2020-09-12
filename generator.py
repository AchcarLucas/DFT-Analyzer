'''
    Module: Gerador de Sinal
    Author: Lucas Campos Achcar
'''
import math
import data

'''
    Versão do Arquivo generador.py
    Function: _version
    Args:
        None
'''
def _version():
    return '0.0.1'

'''
    Classe de dados para salvar a amostra do sinal
    Class: DataSignal
    Data:
        sample_rate: Quantos bytes por amostragem (amostras de 1 segundo)
        time_duration: Tempo de duração dos dados (em segundos)
        data_len: Tamanho total dos dados
        data: Dados da onda
'''
class DataSignal(object):
    def __init__(self, sample_rate, time_duration, data_len, data):
        self.sample_rate = sample_rate
        self.time_duration = time_duration
        self.data_len = data_len
        self.data = data
'''
    Classe auxiliar para gerar os sinais
    Class: SignalGenerator
    Data:
        frequencies: As frequências (Hz) bases para gerar o pacote de dados (list)
        magnetude: Magnetude correspondente a cada frequência (list)
        phases: Fases (Rad) correspondente a cada frequência
        sample_rate: Quantos bytes por amostragem (amostras de 1 segundo)
        duration: Duração (segundos) que o sinal deve ter
'''
class SignalGenerator(object):
    def __init__(self, frequencies, magnetude, phases, sample_rate, duration):
        self.frequencies = frequencies
        self.magnetude = magnetude
        self.phases = phases
        self.sample_rate = sample_rate
        self.duration = duration

'''
    Gerador de Sinais
    Function: signalGenerator
    Arg:
        file_name: Nome do arquivo para onde será salvo os dados
        signalGen: Classe SignalGenerator
'''
def signalGenerator(file_name, signalGen):

    # List com os dados para serem salvos
    DataGenerator = []

    '''
        FS -> SAMPLE FRAME
        É necessário para gerar a amostragem do sinal
        A cada sample_rate, teremos um ciclo do sinal gerado
    '''
    
    FS = 1.0 / signalGen.sample_rate

    '''
        A fórmula utilizada para gerar o sinal foi
        Magnetude*sin(Frequence*2*PI*FS*x + Phase)
        O X representa a posição da amostra, e como dito,
        a cada sample_rate*FS teremos o sinal de repetindo
    '''
    for g in range(0, signalGen.sample_rate*signalGen.duration):
        DataGenerator.append(0)
        for i in range(0, len(signalGen.frequencies)):
            DataGenerator[g] += signalGen.magnetude[i]*math.sin(signalGen.frequencies[i]*2*math.pi*g*FS + signalGen.phases[i]);

    dataSignal = DataSignal(signalGen.sample_rate, signalGen.duration, len(DataGenerator), DataGenerator)
    data.saveData(file_name, dataSignal)


test = SignalGenerator([1, 5, 10], [5, 5, 5], [0, 0, 0], 1000, 2)
signalGenerator('test_5.txt', test)

'''       
signal = DataSignal(44100, 1, 1000, [1, 2, 3, 4, 5, 6, 7])
data.saveData('test.data', signal)
del signal
signal = data.loadData('test.data')
print(test.sample_rate)
'''
    
