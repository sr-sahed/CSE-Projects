from multiprocessing import Process

def print_hello():
    print("Hello from a separate process!")

p = Process(target=print_hello)
p.start()
p.join()
