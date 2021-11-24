class Node:
    def __init__(self, data):
        self.head = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head_node = None
    
    def get_head(self):
        return self.head_node

    def check_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    
