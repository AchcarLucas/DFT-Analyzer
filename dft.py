'''
    Module: DFT
    Author: Lucas Campos Achcar
'''

import cmath

'''
    Versão do Arquivo dft.py
    Function: _version
    Args:
        None
    Return:
        None
'''
def _version():
    return '0.0.1'

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
    Return:
        Class DFTClass
'''
def DFT(in_sample, sample_rate):
    out_sample = []
    for i in range(0, len(in_sample)):
        out_sample.append(DFTClass(complex(0, 0), 0, 0))
        
    for k in range(0, len(in_sample)):
        t_complex = complex(0, 0)
        for n in range(0, SAMPLE_RATE):
            t_complex.real += in_sample[n]*cos((2*PI*k*n) / N_SAMPLE);
            t_complex.imag += (-1)*in_sample[n]*sin((2*PI*k*n) / N_SAMPLE);
            
        out_sample[k]._complex = t_complex
        out_sample[k]._mag = sqrt(pow(t_complex.real, 2) + pow(t_complex.imag, 2));
        out_sample[k]._phase = cmath.phase(t_complex)
            
    return out_sample

print(f'DFT Module Version: {_version()}')
