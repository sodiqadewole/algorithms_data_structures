class Node:
    def __init__(self, data):
        self.head = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    #############################    
    def get_head(self):
        return self.head_node

    #############################
    def check_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    ##############################
    def insert_at_tail(self, value):
        # create a node
        new_node = Node(value)
        # check if there's no node in the list
        if self.check_empty():
            self.head_node = new_node
            # return
        else:
            self.currentNode == self.head_node
            while self.currentNode.next is not None:
                self.currentNode = self.currentNode.next
        self.currentNode.next = newNode


    def insert_at_idx(self, idx, value):
        pass

    def insert_at_start(self, value):
        pass

    def delete_at_start(self, value):
        pass

    def delete_idx(self, idx, value):
        pass

    def delete_at_tail(self):
        pass

    def get_length(self):
        pass

    def merge_linked_list(self, linked_lst1, linked_lst2):
        pass

    def node_swap(self, node):
        pass

    def remove_duplicates(self, value):
        pass

    def get_nth_to_last_node(self, n):
        pass

    def count_occurences(self, value):
        pass

    def rotate(self):
        pass

    def is_palindrome(self):
        pass

    def move_tail_to_head(self):
        pass

    def sum_two_linked_lst(self, linked_lst1, linked_lst2):
        pass

    def reverse(self):
        pass
    
    def printList(self):
        # check if list is empty
        if self.head_node is None:
            print("List is empty")
            return False
        currentNode = self.head_node
        else:
            while currentNode.next is not None:
                print(currentNode.data, end=" -> ")
                currentNode = currentNode.next
        print(currentNode, end=" -> ")
        return True

