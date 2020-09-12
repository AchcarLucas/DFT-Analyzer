'''
    Module: Ajuda
    Author: Lucas Campos Achcar
'''

'''
    Versão do Arquivo help.py
    Function: _version
    Args:
        None
    Return:
        None
'''
def _version():
    return '0.0.1'

'''
    Exibe uma mensagem padrão caso ocorra um erro de except
    Function: _except
    Args:
        None
    Return:
        None
'''
def _except():
    print(f'-----------------------------------------------------------------')
    print(f'Está com problemas? Digite o argumento help para mais informações')
    print(f'-----------------------------------------------------------------')

'''
    Mensagem de ajuda para o usuário
    Function: c_help
    Args:
        None
    Return:
        None
'''
def c_help():
    print(f'-----------------------------------------------------------------')
    print(f'------------------------  Command Args --------------------------')     
    print(f'-----------------------------------------------------------------')
    print(f'arg help')
    print(f'  Abre a tela de ajuda')  
    print(f'-----------------------------------------------------------------')
    print(f'arg gen [nome-arquivo] [frequências] [magnetudes] [fases]')
    print(f'  O comando acima gera sinais com as frequências definidas, ex: gen 5 12')          
    print(f'  irá gerar um arquivo com as frequências 5 hz e 12 hz')
    print(f'  * Magnetudes e Fases são opcionais')
    print(f'  Ex: gen test.data 1 5 3 ; 5 2 6 ; 30 45 60')
    print(f'   O Comando de exemplo acima gera um sinal complexo cuja as componentes são: ')
    print(f'     1 hz com 5 de magnetude e 30º de fase')
    print(f'     5 hz com 2 de magnetude e 45º de fase')
    print(f'     3 hz com 6 de magnetude e 60º de fase')
    print(f'   A Sample da onde será gerado e salvo no arquivo test.data')
    print(f'-----------------------------------------------------------------')
    print(f'arg analyzer [nome-arquivo]')
    print(f'  Faz a análise do sinal do arquivo de dados')
    print(f'-----------------------------------------------------------------')

'''
    Caso ocorra um erro de argumento inválido (comando inválido)
    Function: inv_args
    Args:
        None
    Return:
        None
'''
def inv_args(arg):
    print(f'-----------------------------------------------------------------')
    print(f'O comando {arg} é inválido, se você estiver com dificuldade,')
    print(f'digite o nome do programa e logo em seguida o comando help para.')
    print(f'mais informações')
    print(f'-----------------------------------------------------------------')

print(f'Help Module Version: {_version()}')

