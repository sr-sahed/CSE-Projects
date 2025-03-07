import gc

class Test:
    def __del__(self):
        print("Object destroyed")

obj = Test()
del obj
gc.collect()  # Manually trigger garbage collection
