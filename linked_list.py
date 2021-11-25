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
            return

        current_node = self.head_node
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        return

    ##############################
    def insert_at_head(self, value):
        new_node = Node(value)
        if self.head_node == None:
            self.head_node = new_node
        else:
            self.head_node.next = self.head_node
            self.head_node = new_node
        # self.printList()

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

    ##############################
    # insert a node at a given index
    def insert_at_idx(self, idx, value):
        pass
    
    ##############################
    # delete a node by value in the list
    def delete_by_value(self, value): # O(n)
        deleted = False
        if self.head_node is None:
            print("List is empty")
            return deleted

        current_node = self.head_node
        previous_node = None

        if current_node.data == value:
            lst.delete_at_head()
            deleted = True
            return deleted

        # Traversing and Searching for the Node to Delete
        while current_node is not None:
            # Node to delete is found
            if current_node.data == value:
                # previous node now points to next node
                previous_node.next = current_node.next
                current_node.next = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next
        
        if deleted is False:
            print(str(value) + " is not in list!")
        else:
            print(str(value) + " deleted!")

        # self.printList()
        return deleted
            
        

    def delete_at_head(self):
        first_node = self.head_node
        if first_node == None:
            print("List is empty!")
        else:
            self.head_node = first_node.next
            first_node.next = None
        return


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
    lst.insert_at_tail(4)
    lst.insert_at_tail(41)
    lst.insert_at_tail(10)
    lst.delete_by_value(4)