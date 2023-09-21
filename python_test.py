import timeit

class Benchmark:
    def __init__(self):
        pass
    
    def run(self, fn, number=1):
        timer = timeit.Timer(lambda: fn())
        return timer.timeit(number=number)

def multiplication_table():
    x = 0
    for i in range(300000):
        x += i
        x ^= i
    return x

if __name__ == "__main__":
    benchmark = Benchmark()
    elapsed_time = benchmark.run(multiplication_table)
    print(elapsed_time)
    print(multiplication_table())
