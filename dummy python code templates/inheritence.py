class A:
    def displayA(self):
        print("I am in A")
        
class B(A):
    def displayB(self):
        print("I am in B")
        
class C(A):
    def displayC(self):
        print("I am in C")
        
class D(B,C):
    def displayD(self):
        print("I am in D")