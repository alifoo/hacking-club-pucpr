Um push em uma fila é 0(n) ao invés de 0(1), porque inserimos no começo e todos os elementos tem que ser movidos para a direita.

Pra fazer uma fila rápida, a melhor opção é usar uma linkedlist. Os elementos não estão perto um dos outros na memória, mas cada item referencia o outro.

Os nodes são definidos como uma classe simples de dois campos:
- val: o valor string raw que o node segura
- next: referencia pro proximo node na lista

Inserir no meio de uma lista encadeada é O(1) porque nós simplesmente mudamos duas referencias: de um valor para o novo, e do novo para o que o valor antigo referenciava.

