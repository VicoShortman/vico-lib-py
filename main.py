from vicolib.converter.time import Time
from vicolib.decorators.debug import debug, important, create_important_decorator
from vicolib.decorators.benchmark import bench_time

# get timestamp
print(f"Timestamp Now: {Time.stamp_now()}")
# get timestamp with DMY
print(f"Timestamp Now Formattet: {Time.stamp_now('dmy')}")
# get timestamp custom formattet
print(f"Timestamp Now Formattet: {Time.stamp_now('%Y,%d Month: %M')}")


# measure the time a function takes to execute and prints it to console
@bench_time
def bench_test(n=None):
    if not n:
        n = 1000000
    if type(n) is not int:
        raise ValueError("Bench Test needs int!")
    for r in range(n):
        r += r * 2

# print the return of a function with timestamp and function name
@debug
def debug_test():
    return "Long Return Debug Text"


# print the return like debug but with a line full of '!' 
@important
def debug_important_test():
    return "Long Return Debug Text"

# you could also write it like this:
#
# @create_important_decorator("!")
# def debug_important_test():
#     return "Long Return Debug Text"
#
# but if you use it more then once, its inefficient

# If you want a custom char to be printend, create your own decorator
my_decorator = create_important_decorator("=")

@my_decorator
def debug_my_decorator():
    return "My Test Text"




bench_test(9000000)
debug_test()
debug_important_test()
debug_my_decorator()