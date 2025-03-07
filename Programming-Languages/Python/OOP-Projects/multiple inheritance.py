class A:
    def method_a(self):
        return "Method from A"

class B:
    def method_b(self):
        return "Method from B"

class C(A, B):  # Multiple Inheritance
    pass

obj = C()
print(obj.method_a(), obj.method_b())  # Output: Method from A Method from B
