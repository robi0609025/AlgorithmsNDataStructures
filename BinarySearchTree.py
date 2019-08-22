from random import randint

class Node():
    def __init__(self, value = None):
        self.value = value
        self.rightChild = None
        self.leftChild = None


class BinarySearchTree(object):
    """description of class"""
    def __init__(self):
        self.root = None

    def Insert(self, value):
        if (self.root == None):  
            self.root = Node(value)
        else:
            self._Insert(value, self.root)

    def _Insert(self, value, cur_node):
        if (value < cur_node.value):
            if (cur_node.leftChild == None):
                cur_node.leftChild = Node(value)
            else:
                self._Insert(value, cur_node.leftChild)
        elif (value > cur_node.value):
            if (cur_node.rightChild == None):
                cur_node.rightChild = Node(value)
            else:
                self._Insert(value, cur_node.rightChild);
        else:
            print ("Already exist")

    def PrintTree(self):
        if self.root == None:
            print ("The tree is empty")
        else:
            self._PrintTree(self.root)

    def _PrintTree(self, cur_node):
        if cur_node != None:
            self._PrintTree(cur_node.leftChild)
            print (cur_node.value)
            self._PrintTree(cur_node.rightChild)


def FillTree(tree, numOfNodes = 100, MaxRange = 1000):
    for _ in range (numOfNodes):
        tree.Insert(randint(0,MaxRange))
    return tree


tree = BinarySearchTree()

tree = FillTree(tree)

tree.PrintTree()