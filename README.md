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

Somando todas as componentes teremos uma onda complexa.

O Software possui 4 comandos de argumentos de fácil utilização, são eles:

```
help
signal-analyzer
signal-data
wav-data
```

O Comando help, como o próprio nome diz, é um ajuda para auxiliar nos comandos básicos. Para utilizar, digite o seguinte comando:

```
python main.py help
```

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

Sendo ```diff - [magnetudes]` ``` e  ```diff - [fase]``` opcionais.

```diff
- (OBS: O `-` é obrigatório após a frequência e magnetudes)
```

O primeiro argumento após o comando generator `./data/file-name.data` é o local onde será salvo o arquivo de dados. 
O segundo argumento `1000` é a quantidade de amostras a cada ciclo.
O terceiro argumento `5` é a quantidade de ciclos, se considerarmos uma amostra de 1000 e 5 ciclos, teremos um total de 5000 amostras, o cálculo da quantidade
de amostras é dado por `amostras = segundos*(amostras/ciclo).`

```diff
- OBS: O programa considera cada ciclo como 1 segundo.
```

O quarto argumento, podemos considerar como um único pacote (`1 5 8 10`), esses dados representam as frequências em Hz
O quinto pacote de argumentos após o `-` (`5 6 7 8`) são as amplitudes e corresponde a cada frequência (magnetude 5 corresponte a frequência 1Hz, a magnetude 6 representa a frequência 5Hz).
O sexto argumento após o `-` (`30 45 60`) são as fases em graus (`º`) respectivamente de cada frequência (30º da frequência 1Hz, 45º da frequência 5Hz). Observe que a frequência 10Hz não possui uma fase correspondente, com isso, podemos considera-la 0º.

```diff
- (OBS: a quantidade de amplitude e fases podem ser menor que a de frequência porém, as frequências que não possuir uma amplitude ou fase especifica terão como padrão: 1 de amplitude e 0º de fase. O argumetno de amplitude e as fase são opcionais.)
```

Com os dados acima, teremos uma saída igual a essa:

![WaveSignal](https://github.com/AchcarLucas/DFT-Analyzer/blob/master/img/WaveSignal.png?raw=true)

Observe que gerar uma onda com `generator` não irá exibir detalhe algum de como a onda é, para isso o comando `signal-data` foi criado.

Exemplo de utilização:

```
python main.py signal-data .\data\test1.data blue 0 2
```
