class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

class LinkedList:
    def __init__(self) -> None:
        self.head_node = None
    
    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        if(self.is_empty()):
            self.head_node = temp_node
            return self.head_node
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

class Graph():
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # Define a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []
        # Creating a new Linkedlist for each vertex/index of the list
        for i in range(vertices):
            self.array.append(LinkedList())

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_head(destination) # Directed graph
            # self.array[destination].insert_at_head(source) # Undirected graphs

            # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
            # We would create an edge from destination towards source as well
            # i.e self.list[destination].insertAtHead(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")

if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(1, 3)
    g.add_edge(2, 3)

    g.print_graph()

    print(g.array[1].get_head().data)
