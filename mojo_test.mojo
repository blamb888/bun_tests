from benchmark import Benchmark

fn main():
    var x = 0
    @parameter
    fn multiplication_table():
        for i in range(300000):
            x += i
            x ^= i

    print(Benchmark().run[multiplication_table]())
    print(x)