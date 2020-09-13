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
    print(f'arg generator [nome-arquivo] [taxa-de-amostragem] [duração] [frequências] [magnetudes] [fases]')
    print(f'  O comando acima gera sinais com as frequências definidas, ex: gen 5 12')          
    print(f'  irá gerar um arquivo de dados de onda complexa de frequências 5 hz e 12 hz')
    print(f'  * [magnetudes] e [fases] são opcionais')
    print(f'  * [magnetudes] por default é 1')
    print(f'  * [fases] por default é 0º')
    print(f'  Ex: generator ./data/test.data 300 3 1 5 3 ; 5 2 6 ; 30 45 60')
    print(f'   O Comando de exemplo acima gera um sinal complexo cuja as componentes são: ')
    print(f'     1 hz com 5 de magnetude e 30º de fase')
    print(f'     5 hz com 2 de magnetude e 45º de fase')
    print(f'     3 hz com 6 de magnetude e 60º de fase')
    print(f'   Possui 3 segundos de duração com uma amostragem de 300 por segundos,')
    print(f'   totalizando 900 amostras')
    print(f'   No exemplo, os dados da onde serão gerados e salvo na pasta data no arquivo test.data')
    print(f'-----------------------------------------------------------------')
    print(f'arg signal-analyzer [nome-arquivo-data] [cor]')
    print(f'  Faz a análise do sinal do arquivo de dados, o argumento [cor] é opcional')
    print(f'  Ex: analyzer ./data/test.data blue')
    print(f'-----------------------------------------------------------------')
    print(f'arg signal-data [nome-arquivo-data] [cor]')
    print(f'  Exibe a forma de onda do arquivo de dados, o argumento [cor] é opcional')
    print(f'  Ex: signal-data ./data/test.data blue')
    print(f'-----------------------------------------------------------------')
    print(f'arg wav-data [nome-wav] [nome-arquivo-data] [start_time] [end_time]')
    print(f'  Essa opção converte um arquivo wav em um arquivo-data para posterior análise')
    print(f'  [start_time] e [end_time] são opcionais, padrão start_time = 0 e end_time = 1')
    print(f'  Ex: wav-data ./wav/440.wav ./data/test.data 0.0 5.0')
    print(f'   O comando acima converte o arquivo wav em um arquivo de dados com duração')
    print(f'   de 0.0 segundo até 5.0 segundos')
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

