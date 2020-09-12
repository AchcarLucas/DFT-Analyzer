'''
    Module: Graphic
    Author: Lucas Campos Achcar
'''

import numpy as np
import matplotlib.pyplot as plot
import matplotlib as mpl

'''
    Adiciona um estilo de apresentação dos gráficos
    O arquivo se localiza em ./mplstyle/presentation.mplstyle
'''

'''
    Versão do Arquivo graphic.py
    Function: _version
    Args:
        None
    Return:
        None
'''
def _version():
    return '0.0.1'

'''
    Função para desenhar os dados de uma onda complexa
    Function: drawGraphicData
    Args:
        title: Titulo do gráfico
        x_label: Significado do dado no eixo x
        y_label: Significado do dado no eixo y
        size_x_y: List [largura, altura] do gráfico
        data: Contém os pontos da onda
    Return:
        None
'''
def drawGraphicData(title, x_label, y_label, size_x_y, data):
    plot.style.use('./mplstyle/presentation.mplstyle')
    figure, (axies) = plot.subplots(1, 1, figsize=(size_x_y[0],size_x_y[1]))

    axies.set_xlabel(x_label)
    axies.set_ylabel(y_label)
    axies.set_title(title)
    
    axies.plot(data, 'r-o')

'''
    Função que exibe todos os gráficos adicionados
    Function: showGraphic
    Args:
        None
    Return:
        None
'''
def showGraphic():
    plot.show()

print(f'Graphic Module Version: {_version()}')



