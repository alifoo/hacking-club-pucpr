# Merge sort (funcao recursiva)

def merge_sort(nums):

1. Definir base case com um if, retornar se a lista ja estiver ordenada
2. definir variavel que marca o meio da lista recebida (nums)
    len() para pegar o tamanho da lista
3. chamar a funcao merge sort na esquerda da lista (definida usando :)
4. chamar a funcao merge sort na direita da lista (definida usando :)
5. retornar chamada da funcao merge, passando esquerda e direita

def merge(left, right):

1. definir variaveis i e j como 0
2. criar uma lista vazia para popular
3. enquanto i e j forem menores que o comprimento das listas da esquerda e direita
    4. comparar se posicao i na lista esquerda é menor ou igual posicao j da lista direita
        se for, adiciona item da posicao i na lista esquerda na lista final
        incrementa i
    se não:
        adiciona item da posicao j na lista direita na lista final
        incrementa j

5. verificar se sobrou algum item na lista esquerda ou direita e adicionar na lista final se tiver
6. retornar lista final
