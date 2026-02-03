class node:
    def __init__(self, val):
        self.__data =val
        self.__left = None
        self.__right = None


    def compare(self,val):
        if self.__data > val:
            self.__left = insert(self.__left,val)
        else:
            self.__right = insert(self.__right,val)

    def traversal(self):
        if self.__left != None:
            self.__left.traversal()
        if self.__right != None:
            self.__right.traversal()
        print(self.__data)

def insert(a, val):
    if a is None:
        a = node(val)
        print("created node with value "+str(val))
    else:
        a.compare(val)
    return a

root = None
a = [7, 8, 9, 6, 3, 4, 1, 5]
for x in a:
    root = insert(root, x)
root.traversal()


