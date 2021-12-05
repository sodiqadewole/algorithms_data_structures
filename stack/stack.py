
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.item = self.items[-1]
        self.items = self.items[:-1]
        return self.item

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

def is_match(p1, p2):
    '''
    Check if parenthesis match
    '''
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "{[(":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


def reverse_string(string):
    stack = Stack()
    for s in list(string):
        stack.push(s)
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    return str(reversed_string)

def dec_to_bin(dec_num):
    stack = Stack()
    if dec_num == 0:
        return 0
    while dec_num // 2 > 0:
        stack.push(str(dec_num % 2))
        dec_num = dec_num // 2
    stack.push(str(dec_num))
    binary_ = ''
    while not stack.is_empty():
        binary_ += stack.pop()
    return binary_

def main_test1():
    print("String : (((({})))) Balanced or not?")
    print(is_paren_balanced("(((({}))))"))

    print("String : [][]]] Balanced or not?")
    print(is_paren_balanced("[][]]]"))

    print("String : [][] Balanced or not?")
    print(is_paren_balanced("[][]"))

def main_test2():
    my_stack = Stack()
    print(my_stack.is_empty())
    my_stack.push("A")
    my_stack.push("B")
    print(my_stack.get_stack())
    my_stack.push("C")
    print(my_stack.get_stack())
    my_stack.pop()
    print(my_stack.get_stack())
    print(my_stack.is_empty())

def main_test3(my_string):
    print(reverse_string(my_string))

def main_test4(my_num):
    print(dec_to_bin(my_num))

if __name__ == '__main__':
    main_test4(242)
    main_test4(56)
    main_test4(32)
    main_test4(2)
    main_test4(0)
    main_test4(1)