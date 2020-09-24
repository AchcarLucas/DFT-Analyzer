'''
    Module: DFT
    Author: Lucas Campos Achcar
'''

import math

'''
    Versão do Arquivo dft.py
    Function: _version
    Args:
        None
    Return:
        None
'''
def _version():
    return '0.0.3'

'''
    Classe Complexa
    Class: ComplexClass
    Data:
        _real: Parte real
        _imag: Parte Imaginária
    Functions:
        None
'''
class ComplexClass(object):
    def __init__(self, _real, _imag):
        self._real = _real
        self._imag = _imag
'''
    Classe DFT pós analise dos dados
    Class: DFTClass
    Data:
        sample_rate: Quantos bytes por amostragem (amostras de 1 segundo)
        duration: Tempo de duração dos dados (em segundos)
        data_len: Tamanho total dos dados
        data: Dados da onda
    Functions:
        None
'''
class DFTClass(object):
    def __init__(self, _complex, _mag, _phase):
        self._complex = _complex
        self._mag = _mag
        self._phase = _phase

'''
    Função Analisador DFT (Discrete Fourier Transform)
    Function: DFT
    Args:
        data: lista dos dados a ser analisado
        sample_rate: taxa de amostragem em cada ciclo
        interval_analyzer: intervalo da amostragem
    Return:
        Class DFTClass
'''
def DFT(in_sample, sample_rate, interval_analyzer):
    out_sample = []

    # Quantidade de pontos na amostra
    N = sample_rate
    
    for k in range(interval_analyzer[0], interval_analyzer[1]):
        out_sample.append(DFTClass(ComplexClass(0, 0), 0, 0))
        t_complex = ComplexClass(0, 0)
        
        for n in range(0, N - 1):
            t_complex._real += in_sample[n]*math.cos((2*math.pi*k*n) / N);
            t_complex._imag += (-1)*in_sample[n]*math.sin((2*math.pi*k*n) / N);
            
        out_sample[k - interval_analyzer[0]]._complex = t_complex
        out_sample[k - interval_analyzer[0]]._mag = math.sqrt(pow(t_complex._real, 2) + pow(t_complex._imag, 2)) / N;
        out_sample[k - interval_analyzer[0]]._phase = math.atan2(t_complex._imag, t_complex._real);
            
    return out_sample

print(f'DFT Module Version: {_version()}')
