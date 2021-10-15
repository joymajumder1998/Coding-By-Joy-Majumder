class node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x
        
class binarytree:
    def __init__(self):
        self.root=None
        
    def insert(self):
        data=input("Enter the value : ")
        x=node(data)
        if(data!="NULL"):
            print("Left child of ",data)
            x.left=self.insert()
            print("Right child of ",data)
            x.right=self.insert()
        return x
        
    def visit(self,r):
        if(r.data=="NULL"):
            print("NULL",end=" ")
            return
        print(r.data,end=" ")
        self.visit(r.left)
        self.visit(r.right)
        
    def display(self):
        self.visit(self.root)
        
    def create(self):
        self.root=self.insert()