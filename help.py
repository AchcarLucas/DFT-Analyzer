'''
    Module: Ajuda
    Author: Lucas Campos Achcar
'''
    
def _version():
    return '0.0.1'

def _except():
    print(f'-----------------------------------------------------------------')
    print(f'Está com problemas? Digite o argumento help para mais informações')
    print(f'-----------------------------------------------------------------')

def c_help():
    print(f'-----------------------------------------------------------------')
    print(f'------------------------  Command Args --------------------------')     
    print(f'-----------------------------------------------------------------')
    print(f'arg help                             -> abre a tela de ajuda')
    print(f'-----------------------------------------------------------------')
    print(f'arg gen [nome-arquivo] [frequências] -> gerar sinais com as frequências definidas, ex: gen 5 12')
    print(f'                                        irá gerar um arquivo com as frequências 5 hz e 12 hz')
    print(f'-----------------------------------------------------------------')
    print(f'arg analyzer [nome-arquivo]          -> faz a análise do sinal escrito arquivo de dados')
    print(f'-----------------------------------------------------------------')

def inv_args(arg):
    print(f'-----------------------------------------------------------------')
    print(f'O comando {arg} é inválido, se você estiver com dificuldade,')
    print(f'digite o nome do programa e logo em seguida o comando help para.')
    print(f'mais informações')
    print(f'-----------------------------------------------------------------')

