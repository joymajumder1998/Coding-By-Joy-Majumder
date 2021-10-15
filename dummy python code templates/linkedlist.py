class Node:
    def __init__(self,value):
        self.value=value
        self.link=None
        
class List:
    def __init__(self):
        self.header=None
        
    def insert(self,value):
        new=Node(value)
        if(self.header==None):
            self.header=new
            return
        ptr=self.header
        while(ptr.link!=None):
            ptr=ptr.link
        ptr.link=new
        
    def display(self):
        ptr=self.header
        while(ptr):
            print(ptr.value,end=" ")
            ptr=ptr.link
            
    def Reverse(self,ptr):
        if(ptr.link==None):
            return ptr[]
        if(ptr.link.link==None):
            ptr.link.link=ptr
        self.Reverse(ptr.link)
        
    def reverse(self):
        self.Reverse(self.header)
        
        
        
        
        
        
        
        
        