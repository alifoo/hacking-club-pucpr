# Introdução ao Clube

1. O objetivo do clube é fazer com que todos evoluam como desenvolvedores
2. Aprendam a pensar em organização de dados para acesso eficiente e otimização de performance

Estruturas de dados?

Algoritmos?
Finitos/Definidos = sequencia de passos
Implementáveis = podem ser executados
Inambíguos = tem jeito certo e jeito errado

## Pontos importantes
- [x] Não tente memorizar.
- [x] Foque em aprender a quebrar problemas grandes em problemas pequenos
- [x] Entenda como DSA funciona no momento; ou seja, entenda o código, mas não se preocupe em decorar.

## Exemplos de algoritmos

Start with an original string called S and a new empty string called R.
Loop through S from its last character to its first character, and for each one, add it to the end of R.
Once you’ve processed all the characters, return R.

Encontrar o mínimo

# Big O

Análise simplificada da eficiência de algoritmos

1. Complexidade baseada em input size (dados de entrada)
2. Independente de máquina
3. Análise do passo a passo computacional
4. Mapeamento de tempo e espaço

## Tipos de análise
Pior, melhor e médio caso

## Regras
1. Ignoramos constantes
5n -> O(n)

Por que tivemos um estudo da base matemática?
Porque existe a dominância de termos.

O(1) < O(log n) < O(n) < O(n log n) < O(nˆ2) < O(2ˆn) < O(n!)

Termos de ordem menor são ignorados. Mas por que?

Basicamente porque queremos a medida do crescimento de um algoritmo. f(n) = 1000n
não importa ter uma constante grande 1000, o que importa é que o algoritmo em si cresce de forma linear (n).

Exemplo de ordem menor ser ignorada:
```python
y = 5 + (15 * 20) # O(1)
for x in range(0, n): # O(n)
    print(x)
```
Quando N for grande, o tempo que leva para computar y é insignificante.

## Constant time (O(1))
```python
x = 5 + (15 * 20)
y = 15 - 2
x+y
```

O(1) + O(1) + O(1)
Não dependem do input! 3 * O(1) = O(1)

Imaginem uma lista de 1.000.000 itens
1 milisegundo pra cada item
16 minutos, 40 segundos em O(n)

31,7 anos em O(nˆ2)

E o log(n)?
20 milisegundos!

## Quadratic time
```python
for x in range(0, n): # 0(n)
    for y in range(0, n): # O(n)
        print(x * y)
```
## Logarithmic time

O(log n) - Logaritmico. O tempo de execução cresce muito devagas. Comum em algoritmos que dividem o problema pela metade a cada passo
O(n log n) - Linear algoritmico, passa por todos os elementos mas também faz alguma divisão logarítmica, como recursão.

