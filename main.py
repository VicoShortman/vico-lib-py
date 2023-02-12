# Testing File
from vicolib.converter.time import Time
from vicolib.decorators.benchmark import bench_time
from vicolib.decorators.debug import debug, debug_important


@bench_time
def bench_test(n=None):
    if not n:
        n = 1000000
    if type(n) is not int:
        raise ValueError("Bench Test needs int!")
    for r in range(n):
        r += r * 2

important = debug_important("=")

@important
def debug_important_test():
    return "Long Return Debug Text"


@debug
def debug_test():
    return "Long Return Debug Text"


if __name__ == "__main__":
    debug_important_test()
    bench_test(9000000)
    debug_test()
