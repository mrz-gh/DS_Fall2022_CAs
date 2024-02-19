import unittest
import sys
import functools

def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if attr == 'Node':
                setattr(cls, attr, getattr(cls, attr))
            elif callable(getattr(cls, attr)) :
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

@for_all_methods(staticmethod)
class Utils():
    def parse_line(line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def delete_end_char(line):
        return line.rstrip(line[-1])

    def get_attribute_pointer(object, attribute):
        return getattr(object, attribute)

    def get_args(argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def run_function(attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)
      
    def covert_args_to_int(args):
        newArgsList = list(args[1:])
        for i in range(1, len(args)):
            if isinstance(args[i], str) and (args[i].isnumeric() or args[i][0] == '-'):
                newArgsList[i - 1] = int(args[i])
        return tuple([args[0]] + newArgsList)
    
    def delete_quotation(args):
        newArgsList = list(args)
        for i in range(1,len(args)):
            if isinstance(newArgsList[i], str):
                newArgsList[i] = newArgsList[i].replace('\'', '')
        return tuple(newArgsList)

def fix_str_arg(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if(len(args) > 1):
            args = Utils.delete_quotation(args)
            args = Utils.covert_args_to_int(args)
        return func(*args, **kwargs)
    return wrapper

def print_raised_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
            if val != None:
                return val
        except Exception as e:
            print(str(e))
    return wrapper

class MainEmu():
    def __init__(self):
        self.items = dict()

    def start_program(self):
        for line in sys.stdin:
            line = Utils.delete_end_char(line)
            action, line = Utils.parse_line(line)
            actionPointer = Utils.get_attribute_pointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = Utils.parse_line(line)
        itemName, line = Utils.parse_line(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = Utils.parse_line(line, '.')
        funcName, line = Utils.parse_line(line, '(')
        argsLine, line = Utils.parse_line(line, ')')
        args = Utils.get_args(argsLine)
        attribute = Utils.get_attribute_pointer(self.items[itemName],
                                                   funcName)

        Utils.run_function(attribute, args)

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class MinHeap:
    def __init__(self):
        self.heap : list = []
    
        
    def bubble_up(self, index):
        if isinstance(index, int) is False : 
            raise Exception ('invalid index')
        elif index >= len(self.heap) or index < 0:
            raise Exception ('out of range index')
        else :
            while (index-1)//2 >= 0 and self.heap[(index - 1)//2] > self.heap[index]:
                temp = self.heap[(index - 1)//2]
                self.heap[(index - 1)//2] = self.heap[index]
                self.heap[index] = temp
                index = (index-1)//2


            
    def bubble_down(self, index):
        if isinstance(index, int) is False : 
            raise Exception ('invalid index')
        elif index >= len(self.heap) or index < 0:
            raise Exception ('out of range index')
        else :
            smallest : int = -1
            while 2*index + 1 < len(self.heap):
                smallest = index

                if self.heap[smallest] > self.heap[2*index + 1]:
                    smallest = 2*index + 1

                if 2*index + 2 < len(self.heap) and self.heap[smallest] > self.heap[2*index + 2]:
                    smallest = 2*index + 2


                if smallest == index :
                    break
                else:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[smallest]
                    self.heap[smallest] = temp
                    index = smallest


    
    def heap_push(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)

        
    def heap_pop(self):
        if len(self.heap) == 0 :
            raise Exception ("empty")
        else:
            if len(self.heap) == 1 :
                print(self.heap.pop())
            else:
                ans = self.heap[0]
                self.heap[0] = self.heap.pop()
                self.bubble_down(0)
                print(ans)


    def find_min_child(self, index):
        if isinstance(index, int) is False : 
            raise Exception ('invalid index')
        elif (2*index + 1) >= len(self.heap) or index < 0:
            raise Exception ('out of range index')
        else :
            if 2*index + 2 == len(self.heap):
                return 2*index + 1

            if self.heap[2*index + 2] < self.heap[2*index + 1]:
                return 2*index + 2

            else : 
                return 2*index + 1

        

    def heapify(self, *args):
        
        self.heap.extend(args)
        i = len(self.heap)//2
        while i >= 0 : 
            self.bubble_down(i)
            i -= 1
        
        #self.heap = sorted(args)

        pass


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


class HuffmanTree:
    def __init__(self):
        self.freq = {}
        pass

    @fix_str_arg    
    def set_letters(self,*args):
        for c in args:
            self.freq[c] = -1


    @fix_str_arg    
    def set_repetitions(self,*args):
        for i, c in enumerate(self.freq.keys()):
            self.freq[c] = args[i]


    
    def build_huffman_tree(self):
        freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

        nodes = freq

        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = Node(key1, key2)
            nodes.append((node, c1 + c2))

            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)



        def huffman_code_tree(node, left=True, binString=''):
            if type(node) is str:
                return {node: binString}
            (l, r) = node.children()
            d = dict()
            d.update(huffman_code_tree(l, True, binString + '0'))
            d.update(huffman_code_tree(r, False, binString + '1'))
            return d



        self.huffmanCode = huffman_code_tree(nodes[0][0])
    

    def get_huffman_code_cost(self):
        cost = 0
        for char in self.freq:
            #print(' %-4r |%12s' % (char, self.huffmanCode[char]))
            #print(self.freq[char])
            cost += self.freq[char] * len(self.huffmanCode[char])

        print(cost)


    @fix_str_arg
    def text_encoding(self, text):
        for c in text:
            if c in self.freq:
                self.freq[c] += 1
            else:
                self.freq[c] = 1

        self.build_huffman_tree()

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class RBNode:
        def __init__(self,val):
            self.val = val                                   
            self.parent : RBNode= None                               
            self.left : RBNode= None                                 
            self.right : RBNode = None                                
            self.color = 1                                   # Red Node because new node is always inserted as Red Node

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class RedBlackTree():
    

    def __init__(self):
        self.NULL = RBNode ( 0 )
        self.NULL.color = 0


        self.root = self.NULL
        pass
        

    def fix_insert(self, node : RBNode):
        while node.parent.color == 1:                        # While parent is red
            if node.parent == node.parent.parent.right:         # if parent is right child of its parent
                u : RBNode = node.parent.parent.left                  # Left child of grandparent
                if u.color == 1:                          # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set both children of grandparent node as black
                    node.parent.color = 0
                    node.parent.parent.color = 1             # Set grandparent node as Red
                    node = node.parent.parent                   # Repeat the algo with Parent node to check conflicts
                else:
                    if node == node.parent.left:                # If k is left child of it's parent
                        node = node.parent
                        self.right_rotate(node)                        # Call for right rotation
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            else:                                         # if parent is left child of its parent
                u = node.parent.parent.right                 # Right child of grandparent
                if u.color == 1:                          # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set color of childs as black
                    node.parent.color = 0
                    node.parent.parent.color = 1             # set color of grandparent as Red
                    node = node.parent.parent                   # Repeat algo on grandparent to remove conflicts
                else:
                    if node == node.parent.right:               # if k is right child of its parent
                        node = node.parent
                        self.left_rotate(node)                        # Call left rotate on parent of k
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)              # Call right rotate on grandparent
            if node == self.root:                            # If k reaches root then break
                break


        self.root.color = 0                               # Set color of root as black


        
    def find_node_color(self, value):
        x : RBNode = self.root
        
        while x != self.NULL :
            if x.val == value : 
                if x.color == 1 :
                    return "RED"
                else : 
                    return "BLACK"
            
            elif value < x.val :
                x = x.left 
            else:
                x = x.right



    def left_rotate(self, node : RBNode):
        y : RBNode = node.right                                      # Y = Right child of x
        node.right = y.left                                 # Change right child of x to left child of y
        if y.left != self.NULL :
            y.left.parent = node

        y.parent = node.parent                              # Change parent of y as parent of x
        if node.parent == None :                            # If parent of x == None ie. root node
            self.root = y                                # Set y as root
        elif node == node.parent.left :
            node.parent.left = y
        else :
            node.parent.right = y
        y.left = node
        node.parent = y
        

    def right_rotate(self, node : RBNode):
        y = node.left                                       # Y = Left child of x
        node.left = y.right                                 # Change left child of x to right child of y
        if y.right != self.NULL :
            y.right.parent = node

        y.parent = node.parent                              # Change parent of y as parent of x
        if node.parent == None :                            # If x is root node
            self.root = y                                # Set y as root
        elif node == node.parent.right :
            node.parent.right = y
        else :
            node.parent.left = y
        y.right = node
        node.parent = y

        
    def insert(self, value):
        node : RBNode = RBNode(value)
        node.parent = None
        node.val = value
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Set root colour as Red

        y = None
        x = self.root

        while x != self.NULL :                           # Find position for new node
            y = x
            if node.val < x.val :
                x = x.left
            else :
                x = x.right

        node.parent = y                                  # Set parent of Node as y
        if y == None :                                   # If parent i.e, is none then it is root node
            self.root = node
        elif node.val < y.val :                          # Check if it is right Node or Left Node by checking the value
            y.left = node
        else :
            y.right = node

        if node.parent == None :                         # Root node is always Black
            node.color = 0
            return

        if node.parent.parent == None :                  # If parent of node is Root Node
            return

        self.fix_insert ( node )                          # Else call for Fix Up


classDict = { "min_heap": MinHeap, "red_black_tree": RedBlackTree, "huffman_tree": HuffmanTree}
    
if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.start_program()
