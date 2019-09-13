#Search function

class Tree:
    def __init__(self, value):
        self.value = value
        self.child = []
    
    def addEmptyChild(self):
        self.child.append(None)

    def addChild(self,childTree):
        self.child.append(childTree)
    
    def changeValue(self,newValue):
        self.value = newValue

    def showChildLength(self):
        return len(self.child)

# Below is a unit testing for class Tree

# def main():
#     tree1 = Tree(20)
#     tree2 = Tree(15)
#     print(tree1.showChildLength())
#     print(tree2.showChildLength())
#     tree1.addEmptyChild()
#     print(tree1.showChildLength())
#     tree1.addChild(tree2)
#     print(tree1.showChildLength())
#     print(tree1.value)
#     tree1.changeValue(25)
#     print(tree1.value)
    

# if __name__ == "__main__":
#     main()