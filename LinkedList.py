class LinkedList:
    head = None

    class Node:
        data = None
        next_node = None
        def __init__(self, data, next_node=None) -> set:
            self.data = data
            self.next_node = next_node
    
    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
            return
        node = self.head
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(data)

    def print_linked_list(self):
        node = self.head
        print(f"[{node.data}]", end=" ")

        while node.next_node:
            print(f"-> [{node.next_node.data}]", end=" ")
            node = node.next_node


    def return_head(self):
        return self.head
    


linkedlist = LinkedList()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
linkedlist.append(6)

linkedlist.print_linked_list()
