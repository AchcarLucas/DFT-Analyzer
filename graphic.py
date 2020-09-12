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
plot.style.use('./mplstyle/presentation.mplstyle')

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
    Essa função cria um axies para ser plotado um gráfico
    Function: getAxiesData
    Args:
        title: Titulo do gráfico
        x_label: Significado do dado no eixo x
        y_label: Significado do dado no eixo y
        size_x_y: List [largura, altura] do gráfico
    Return:
        Axies (Janela do Gráfico)
'''
def getAxiesData(title, x_label, y_label, size_x_y):
    figure, (axies) = plot.subplots(1, 1, figsize=(size_x_y[0],size_x_y[1]))

    axies.set_xlabel(x_label)
    axies.set_ylabel(y_label)
    axies.set_title(title)
    
    return axies

'''
    Função para desenhar os dados de uma onda complexa
    Function: drawGraphicData
    Args:
        x: Posição x na tela, (0 até 1)
        y: Posição y na tela, (0 até 1)
        color: A cor da caixa do texto
        alpha: Transparência da caixa de texto
        horizontal_align: Alinhamento horizontal do texto
        vertical_align: Alinhamento vertical do texto
        axies: Axies do matplot
    Return:
        None 
'''
def drawText(x, y, text, axies, color='black', alpha=0.0, horizontal_align='center', vertical_align='center'):
    axies.text(x,  y, text, bbox=dict(facecolor=color, alpha=alpha),
                 horizontalalignment=horizontal_align, verticalalignment=vertical_align,
                 transform=axies.transAxes)

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



