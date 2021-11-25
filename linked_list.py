class Node:
    def __init__(self, data):
        self.data = data
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
    def insert_at_tail(self, value): # O(n)
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
        self.currentNode.next = new_node
    
    ##############################
    def insert_at_head(self, value):
        new_node = Node(value)
        if self.head_node == None:
            self.head_node = new_node
        else:
            self.head_node.next = self.head_node
            self.head_node = new_node
        self.printList()

    ##############################
    # search the list for a value
    def search(self, value): # O(n)
        if self.head_node == None:
            print("List is empty")    
            return False
        elif self.head_node == value:
            print("Found!")
            return True
        else: 
            currentNode = self.head_node
            while currentNode.next is not None:
                currentNode = currentNode.next
                if currentNode == value:
                    print("Found!")
                    return True

    def insert_at_idx(self, idx, value):
        pass

    def delete_by_value(self, value): # O(n)
        if self.head_node == None:
            print("List is empty")
            return False
        elif self.head_node == value:
            self.head_node = None #self.head_node.next
            self.head_node = self.head_node.next
        else:
            current_node = self.head_node
            while current_node.next is not None:
                if current_node == value:
                    current_node = None #current_node.next
                    current_node = current_node.next
                    return True
            # else:
            #     print('value not found!')
            #     return False
        self.printList()

    def delete_at_start(self, value):
        pass

    def delete_by_idx(self, idx, value):
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
        currentNode = self.head_node
        # check if list is empty
        if self.head_node == None:
            print("List is empty")
            return False
        else:
            while currentNode.next is not None:
                print(currentNode.data, end=" -> ")
                currentNode = currentNode.next
        print(currentNode.data, end=" -> ")
        return True

if __name__ == "__main__":
    lst = LinkedList()
    lst.insert_at_head(4)
    lst.insert_at_head(41)
    lst.insert_at_head(10)
    lst.delete_by_value(4)