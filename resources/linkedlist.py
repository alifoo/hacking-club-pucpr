class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def find(self, val):
        current = self.head
        while current is not None:
            if current.val == val:
                return current  # found!
            current = current.next
        return None  # not found

    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        # O novo node deve apontar para o antigo head (começo da lista)
        node.set_next(self.head)
        # O head passa a apontar para o node atual já que ele foi inserido
        self.head = node

    def add_to_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        # Faz o tail atual apontar pro novo node
        self.tail.set_next(node)
        # Transforma o novo item adicionado no novo tail
        self.tail = node

    # método especial que define como um método será iterado
    def __iter__(self):
        # Inicia iteração pelo primeiro item
        node = self.head
        while node is not None:
            # yield retorna o node atual para o caller sem parar a iteracao
            yield node
            # passa para o proximo
            node = node.next

    # define a representacao string do objeto linked list
    # retorna os valores da linked list separados por uma seta
    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.val))
        return " -> ".join(nodes)

    def remove(self, val):
        # seta a atual
        current = self.head
        # variavel para manter registrado a anterior a atual
        previous = None

        while current is not None:
            # achar a node pra remover
            if current.val == val:
                # verificar se a node achada ta no head
                if previous is None:
                    # aponta o head pro proximo
                    self.head = current.next
                    # se isso abaixo acontece, a lista ficou vazia entao atualizamos tail
                    if self.head is None:
                        self.tail = None
                # se chegou aqui, o node achado nao ta no head, ta no meio ou fim
                else:
                    # pula o node atual
                    previous.set_next(current.next)
                    # node removida era o tail
                    if current.next is None:
                        # update no tail
                        self.tail = previous
                return True  # node removed
            # movemos o pointer do previous para frente e o current pointer para frente
            previous = current
            current = current.next
        return False  # node not found


if __name__ == "__main__":
    lst = LinkedList()
    lst.add_to_tail(Node("A"))
    lst.add_to_tail(Node("B"))
    lst.add_to_tail(Node("C"))

    print(lst.is_empty())  # False
    print(lst.find("B"))  # Node object with val "B"
    lst.remove("B")
    print(lst)  # A -> C
    lst.remove("A")
    lst.remove("C")
    print(lst.is_empty())  # True
