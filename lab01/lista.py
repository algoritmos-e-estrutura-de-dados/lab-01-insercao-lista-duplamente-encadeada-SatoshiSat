def main():
    lista = Lista()
    lista.append(Node(150))
    lista.add(Node(40))
    print(lista)



class Node:

    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None


class Lista:

    def __init__(self):
        self.init = None
        self.tail = None

    def append(self, node):
        """
        Método para inserir um elemento no final

        :param node:
        :return:
        """
        if self.init is None:
            new_node = Node(node)
            new_node.prev = None;
            self.init = new_node
        else: 
            new_node = Node(node)
            last = self.init
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last
            new_node.next = None

    def add(self, node):
        """
        Inserir um elemento sempre no inicio da lista

        :param node:
        :return:
        """
        if self.init is None:
            new_node = Node(node)
            new_node.prev = None
            self.init = new_node
        else: 
            new_node = Node(node)
            self.init.prev = new_node
            new_node.next = self.init
            self.init = new_node
            new_node.prev = None

    def __str__(self):
        str_aux = '['
        node_aux = self.init
        while(node_aux is not None):
            str_aux += str(node_aux.x) + ','
            node_aux = node_aux.next
        str_aux += ']'
        return str_aux


if __name__ == '__main__':
    lista = Lista()
    lista.add(Node(x=27))
    lista.add(Node(x=1))
    print(lista)
    lista.append(Node(x=5))
    lista.append(Node(x=19))
    print(lista)
