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
                return current
            current = current.next
        return None

    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.val))
        return " -> ".join(nodes)

    def remove(self, val):
        current = self.head
        previous = None

        while current is not None:
            if current.val == val:
                if previous is None:
                    self.head = current.next
                    if self.head is None:
                        self.tail = None
                else:
                    previous.set_next(current.next)
                    if current.next is None:
                        self.tail = previous
                return True
            previous = current
            current = current.next

        return False


if __name__ == "__main__":
    lt = LinkedList()

    lt.add_to_tail(Node("A"))
    lt.add_to_tail(Node("B"))
    lt.add_to_tail(Node("H"))
    lt.add_to_tail(Node("Z"))

    print(lt.find("H"))
    print(lt)
    lt.remove("Z")
    print(lt)
    lt.remove("B")

    print(lt)
    lt.remove("J")
