'''
    Module: Gerador de Sinal
    Author: Lucas Campos Achcar
'''
import wave
import math
import data
import numpy
import struct

'''
    Versão do Arquivo generador.py
    Function: _version
    Args:
        None
    Return:
        None
'''
def _version():
    return '0.0.1'

'''
    Classe de dados para salvar a amostra do sinal
    Class: DataSignal
    Data:
        sample_rate: Quantos bytes por amostragem (amostras de 1 segundo)
        duration: Tempo de duração dos dados (em segundos)
        data_len: Tamanho total dos dados
        data: Dados da onda
    Functions:
        None
'''
class DataSignal(object):
    def __init__(self, sample_rate, duration, data_len, data):
        self.sample_rate = sample_rate
        self.duration = duration
        self.data_len = data_len
        self.data = data
'''
    Classe auxiliar para gerar os sinais
    Class: SignalGenerator
    Data:
        frequencies: As frequências (Hz) bases para gerar o pacote de dados (list)
        magnetude: Magnetude correspondente a cada frequência (list)
        phases: Fases (Graus) correspondente a cada frequência
        sample_rate: Quantos bytes por amostragem (amostras de 1 segundo)
        duration: Duração (segundos) que o sinal deve ter
    Functions:
        None
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
    Return:
        True -> Sucess
        False -> Error
'''
def signalGenerator(file_name, signalGen):
    try:
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

                # Magnetude é opcional, portanto, se não encontrar dados, adiciona 1 como padrão
                if(i >= len(signalGen.magnetude)):
                    signalGen.magnetude.append(1)

                # Phase é opcional, portanto, se não encontrar dados, adiciona 0º como padrão 
                if(i >= len(signalGen.phases)):
                    signalGen.phases.append(0)
                    
                DataGenerator[g] += signalGen.magnetude[i]*math.sin(signalGen.frequencies[i]*2*math.pi*g*FS + (signalGen.phases[i]*math.pi / 180));

        # Gera a classe e sinal e salva o objeto no arquivo de dados
        dataSignal = DataSignal(signalGen.sample_rate, signalGen.duration, len(DataGenerator), DataGenerator)
        data.saveData(file_name, dataSignal)
        
        return True
    except:
        return False

'''
    Gerador de Sinais a partir de um arquivo wav
    Function: createSignalFromWav
    Arg:
        file_wav_name: nome do arquivo wave
        file_data_name: nome do arquivo onde será salvo
        s_time_analysis: tempo inicial do áudio
        e_time_analysis: tempo final do áudio
    Return:
        True -> Sucess
        False -> Error
'''
def createSignalFromWav(file_wav_name, file_data_name):
    #try:
        with wave.open(file_wav_name, mode='rb') as wav:
            sample_rate = wav.getframerate()
            n_frame = wav.getnframes()

            # Duração do áudio
            duration = n_frame / sample_rate

            # Buffer de Dados
            dataBuffer = wav.readframes(n_frame)

            # Descompacta os bytes em pacotes de 2 bytes (short)   
            DataGenerator = struct.unpack("%ih" % (n_frame * wav.getnchannels()), dataBuffer)
            
            # Converte 16bits wav para float, entre -1.0 e 1.0
            DataGenerator = [float(value) / pow(2, 15) for value in DataGenerator]
        
        # Cria nosso sinal e salva em um file
        dataSignal = DataSignal(sample_rate, duration, len(DataGenerator), DataGenerator)
        data.saveData(file_data_name, dataSignal)
        
        return True
    #except:
        return False

print(f'Generator Module Version: {_version()}')
