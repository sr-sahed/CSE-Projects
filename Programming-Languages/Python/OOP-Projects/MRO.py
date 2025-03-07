class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

print(D.mro())  # Output: [D, B, C, A, object]
