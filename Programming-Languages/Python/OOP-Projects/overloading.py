class Math:
    def add(self, a, b, c=0):  # c is optional
        return a + b + c

m = Math()
print(m.add(5, 10))    # Output: 15
print(m.add(5, 10, 20))  # Output: 35
