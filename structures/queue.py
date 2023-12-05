from .linked_list import LinkedList

class Queue(LinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        if self.head is None:
            return None
        pop = self.head.data
        self.delete_node(self.head.data)
        return pop

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.head is None

    def print_queue(self):
        self.print_list()
