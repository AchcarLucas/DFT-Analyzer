Dependências: 

```diff
+ import pickle
+ import math
+ import wave
+ import data
+ import numpy
+ import struct
+ import numpy
+ import matplotlib
+ import sys
```

# DFT-Analyzer
Analisador de sinal com algoritmo DFT (Discrete Fourier Transform)

Referência: https://en.m.wikipedia.org/wiki/Discrete_Fourier_transform

A fórmula abaixo foi utilizado para o desenvolvimento do algoritmo

![Fórmula DFT](https://github.com/AchcarLucas/DFT-Analyzer/blob/master/img/formula.png?raw=true)

Para a criação de uma onda complexa foi utilizado a seguinte fórmula.

![Fórmula Sum Sin](https://github.com/AchcarLucas/DFT-Analyzer/blob/master/img/sum_sin.png?raw=true)

- `A1, A2 ... ,An` representando os elementos da amplitude
- `F1, F2 ... ,Fn` representando as frequências
- `P1, P2 ... ,Pn` representando as fases
- FS representa `1 / (taxa_de_amostragem)` 2*(PI)*f*FS faz com que a taxa de amostragem seja equivalente a 1 ciclo. ou seja, a cada ciclo o sinal se repete a uma taxa de amostragem fixa.

Somando todas as componentes teremos uma onda complexa.

O Software possui 4 comandos de argumentos de fácil utilização, são eles:

```
help
generator
signal-analyzer
signal-data
wav-data
```

O Comando help, como o próprio nome diz, é uma ajuda para auxiliar nos comandos básicos. Para utilizar, digite o seguinte comando:

```
python main.py help
```

Exibição:

![Help](https://github.com/AchcarLucas/DFT-Analyzer/blob/master/img/help.png?raw=true)

```diff
- (OBS: O comando python main.py tem que ser digitado dentro da pasta que o programa está contido)
```

Já, se deseja gerar uma onda especifica, utilize o seguinte comando:

```
python main.py generator ./data/file-name.data 1000 5 1 5 8 10 - 5 6 7 8 - 30 45 60
```

Seu comando genérico:

```
python main.py generator [nome-arquivo] [taxa-de-amostragem] [duração] [frequências] - [magnetudes] - [fases]
```

Sendo ```[magnetudes]``` e  ```[fase]``` opcionais.

```diff
- (OBS: O `-` é obrigatório após a digitação das frequências e magnetudes)
```

- O primeiro argumento após o comando `generator`, `./data/file-name.data` é o local onde será salvo e o nome do arquivo de dados (Nesse caso, será salvo na pasta `data` com o nome `file-name.data`). 
- O segundo argumento `1000` é a quantidade de amostras a cada ciclo.
- O terceiro argumento `5` é a quantidade de ciclos, se considerarmos uma amostra de 1000 e 5 ciclos, teremos um total de 5000 amostras, o cálculo da quantidade
de amostras é dado por `amostras = segundos*(amostras/ciclo).`

```diff
- OBS: O programa considera cada ciclo como 1 segundo.
```

- O quarto argumento, podemos considerar como um único pacote (`1 5 8 10`), esses dados representam as frequências em Hz
- O quinto pacote de argumentos após o `-` (`5 6 7 8`) são as amplitudes e corresponde a cada frequência (magnetude 5 corresponte a frequência 1 Hz, a magnetude 6 representa a frequência 5 Hz etc).
- O sexto argumento após o `-` (`30 45 60`) são as fases em graus (`º`) respectivamente de cada frequência (30º da frequência 1 Hz, 45º da frequência 5 Hz etc). Observe que a frequência 10Hz não possui uma fase correspondente, com isso, podemos considera-la 0º.

```diff
- (OBS: a quantidade de amplitude e fases podem ser menor que a de frequência porém, as frequências que não possuir uma amplitude ou fase especifica terão como padrão: 1 de amplitude e 0º de fase. O argumento de amplitude e as fase são opcionais.)
```

Com os dados acima, teremos uma saída como mostrado na figura abaixo:

![WaveSignal](https://github.com/AchcarLucas/DFT-Analyzer/blob/master/img/WaveSignal.png?raw=true)

Observe que gerar uma onda com `generator` não irá exibir detalhe algum de como a onda é, para isso o comando `signal-data` foi criado.

Exemplo de utilização:

```
python main.py signal-data .\data\file-name.data blue 0 2
```

Seu comando genérico:

```
python main.py signal-data [nome-arquivo-data] [cor] [tempo-inicial] [tempo-final]
```

```diff
- (OBS: O argumento `cor`, `tempo-inicial` e `tempo-final` são opcionais.)
```

- O primeiro argumento `cor` será a cor de exibição do gráfico. 

Segue a tabela de cores para utilizar no argumento:

```diff
- blue
red
+ green
white
black
cyan
magenta
! yellow
```

A cor, se desejar, pode ser adicionado como Hex Decimal.

Exemplo:

```
python main.py signal-analyzer ./data/test1.data '#ff0000' 0 101
```

Sendo, o primero `FF` Vermelho o `00` Verde e `00` Azul formando o hex `#ff0000`.

- O segundo e o terceiro argumento `[tempo-inicial]` e  `[tempo-final]` representam o tempo inicial e final de análise.

```diff
- (OBS: O tempo inicial, se não for especificado, por padrão é 0.0, já o tempo final, por padrão é a duração que a onda possui)
```

- Exemplo 1

Se um sinal, por exemplo, 10Khz for difícil visualização, reduzindo o tempo inicial e fínal o efeito será como um Zoom na onda.
Esses argumetos podem ser pontos decimais, por exemplo, `0.1 0.5`, o argumento anterior, exibiria uma onda no intervalo de tempo de 0.1 segundo até 0.5 segundos.

Veja a imagem a seguir para exemplo:

![WaveSignal](https://github.com/AchcarLucas/DFT-Analyzer/blob/master/img/0.1-0.5.png?raw=true)

```diff
- (OBS: Os dois argumentos são opcionais como citado anteriormente)
```

- Exemplo 2

A saída para o comando de exemplo abaixo será:

```
python main.py signal-data .\data\test1.data blue 0.0 2.0
```

![WaveSignal](https://github.com/AchcarLucas/DFT-Analyzer/blob/master/img/WaveSignal.png?raw=true)

- Exemplo 3

Já se não for informado os tempos inicias e finais como no exemplo abaixo, a saída será:

```
python main.py signal-data .\data\test1.data red
```

![WaveSignal](https://github.com/AchcarLucas/DFT-Analyzer/blob/master/img/saida-no-time.png?raw=true)

O comando `wav-data` gera um arquivo de dados a partir de um arquivo wav. Utilize o comando como a seguir:

```
main.py wav-data .\tone\10kHz_44100Hz_16bit_05sec.wav ./data/10kHz_44100Hz_16bit_05sec.data
```

- O primeiro argumento `.\tone\100Hz_44100Hz_16bit_05sec.wav.wav` informa qual arquivo wav os dados serão extraidos.
- O segundo argumento `./data/100Hz_44100Hz_16bit_05sec.wav.data` será o nome do arquivo que os dados serão salvos.

```diff
- (OBS: Os dois argumentos são necessários e devem ser preenchidos corretamente)
```

`.\tone\` é o nome da pasta onde se localiza o wav.
`./data/`é o nome da pasta onde deverá ser salvo o arquivo data.

Seu comando genérico é representado a seguir:

```
wav-data [nome-wav] [nome-arquivo-data]
```

O comando `signal-analyzer` é o que faz a análise do sinal, segue o exemplo abaixo para a sua utilização:

```
python main.py signal-analyzer .\data\test.data green 0 50
```

- O primeiro argumento `.\data\test.data` é a localização do arquivo de dados, seja ele gerado pelo comando `generator` ou pelo comando `wav-data`.
- O segundo argumento é a cor exibida pelo gráfico.
- O terceiro e o quarto argumento são as frequências de análise inicial e final, no exemplo, será análisado as frequências de 0 Hz até 50 Hz.

Veja a figura a seguir gerado pelo comando citado:

![Wave-Analyzer](https://github.com/AchcarLucas/DFT-Analyzer/blob/master/img/0-50.png?raw=true)

Seu comando genêrico pode ser descrito abaixo:

```
signal-analyzer [nome-arquivo-data] [cor] [faixa-frequência-inferior] [faixa-frequência-superior]
```

```diff
- (OBS: Os argumentos `[cor]`, `[faixa-frequência-inferior]` e `[faixa-frequência-superior]`são opcionais, por padrão, a cor inicial é vermelha, a frequência de análise inicial e 0 Hz e a frequência de análise final é 100 Hz)
```

Além da frequência por magnetude, a análise do sinal também exibe a frequência por fase (º), veja as imagens a seguir:

Análise do Sinal pela Magnetude (Hz/Mag)
![DFT-Signal](https://github.com/AchcarLucas/DFT-Analyzer/blob/master/img/DFT_Signal.png?raw=true)

Análise do Sinal pela Fase (Hz/º)
![DFT-Signal](https://github.com/AchcarLucas/DFT-Analyzer/blob/master/img/PhaseSignal.png?raw=true)
