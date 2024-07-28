import time

def measure(unit):
    def wrapper(func):
        def inner():
            start = time.time()
            func()
            end = time.time()
            duration = end-start
            if unit == 'seconds':
                print(f"duration: {duration:.6f} seconds")
            if unit == 'microseconds':
                print(f"duration: {duration * 1e6:.2f} microseconds")
        return inner
    return wrapper

@measure(unit='seconds')
def example():
    i = 0
    while i<=100000000:
        i+=1
example()
