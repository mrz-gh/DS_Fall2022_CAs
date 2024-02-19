import sys

class Queue:
    def __init__(self):
        self.arr : list = []
        pass

    def getSize(self):
        return len(self.arr)
        pass

    def enqueue(self, value):
        self.arr.append(value)
        pass

    def dequeue(self):
        return self.arr.pop(0)
        pass

    def isEmpty(self):
        if len(self.arr) == 0 :
            return True
            pass
        else :
            return False
            pass
        pass

    def getInOneLine(self):
        return ' '.join(self.arr)
        pass

class Stack:
    def __init__(self, size=10):
        self.arr : list = []
        self.size = size
        self.top = -1
        pass

    def isEmpty(self):
        if self.top == -1 :
            return True
            pass
        else:
            return False
            pass
        pass

    def push(self, value):
        if self.top < self.size - 1 :
            self.top = self.top + 1
            self.arr.append(value)
            pass
        else: 
            raise Exception("Overflow")
            pass
        pass

    def pop(self):
        if self.top == -1 :
            raise Exception("Underflow")
            pass
        else:
            self.top = self.top - 1
            return self.arr.pop()
        pass

    def put(self,value_):
        self.arr[self.top] = value_
        pass

    def peek(self):
        if self.top == -1 :
            raise Exception("Underflow")

        return self.arr[self.top]
        pass

    def expand(self):
        self.size = self.size * 2
        pass

    def getInOneLine(self):
        return ' '.join(self.arr)
        pass

    def getSize(self):
        return self.top + 1
        pass
    
    def getCapacity(self):
        return self.size
        pass

class Node():
    def __init__(self, val):
        self.val = val
        self.next : int = -1
        self.prev : int = -1
        pass

class LinkedList():
    def __init__(self):
        self.arr : list[Node] = []
        self.head : int = -1
        pass
    
    def getList(self):
        if self.head == -1:
            raise Exception ("LL is Empty")
            pass
        else :
            str = ""
            currNode : Node = self.arr[self.head]
            while currNode.next != -1 :
                str = str + currNode.val + ' '
                currNode = self.arr[currNode.next]
                pass
            str = str + currNode.val
            return str
            pass
        pass
    
    def insertFront(self, new_data):
        if self.head == -1 :
            self.head = 0
            n = Node(new_data)
            n.prev = -1
            n.next = -1
            self.arr.append(n)
            pass
        else:
            n = Node(new_data)
            n.next = self.head
            n.prev = -1
            self.arr[self.head].prev = len(self.arr)
            self.head = len(self.arr)
            self.arr.append(n)
            pass
    pass
    
    def insertEnd(self, new_data):
        if self.head == -1 :
            self.head = 0
            n = Node(new_data)
            n.prev = -1
            n.next = -1
            self.arr.append(n)
            pass
        else :
            currNode : Node = self.arr[self.head]
            while self.arr[currNode.next].next != -1 :
                currNode = self.arr[currNode.next]
                pass
            n = Node(new_data)
            n.prev = currNode.next
            n.next = -1
            self.arr[currNode.next].next = len(self.arr)
            self.arr.append(n)
            pass
        pass
    
    def reverse(self):
        currNode : Node = self.arr[self.head]
        temp : int = -1
        while currNode.next != -1 :
                temp = currNode.next
                currNode.next = currNode.prev
                currNode.prev = temp
                currNode = self.arr[temp]
                pass
        temp = currNode.next
        currNode.next = currNode.prev
        currNode.prev = -1
        self.head = self.arr[currNode.next].prev
        pass

classDict = { "stack": Stack, "queue": Queue, "linked_list": LinkedList}

class Utils():
    def __init__(self):
        pass

    def parseLine(self, line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def deleteEndChar(self, line):
        return line.rstrip(line[-1])

    def getAttributePointer(self, object, attribute):
        return getattr(object, attribute)

    def getArgs(self, argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def runFunction(self, attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)

class MainEmu():
    def __init__(self):
        self.utils = Utils()
        self.items = dict()

    def startProgram(self):
        for line in sys.stdin:
            line = self.utils.deleteEndChar(line)
            action, line = self.utils.parseLine(line)
            actionPointer = self.utils.getAttributePointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = self.utils.parseLine(line)
        itemName, line = self.utils.parseLine(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = self.utils.parseLine(line, '.')
        funcName, line = self.utils.parseLine(line, '(')
        argsLine, line = self.utils.parseLine(line, ')')
        args = self.utils.getArgs(argsLine)
        attribute = self.utils.getAttributePointer(self.items[itemName],
                                                   funcName)

        self.utils.runFunction(attribute, args)

if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.startProgram()