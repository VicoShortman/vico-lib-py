# vicolib
Vico's personal python library with useful decorators and functions.
Use at your own risk!

# Installation
`pip install vicolib`

# Functionality / Modules
*vicolib* is split in different modules with. These are:
## 1. Decorators:
<details><summary>vicolib.decorators.benchmark</summary>

- `@bench_time`   -> prints the time a function needs to execute
</details>

<details><summary>vicolib.decorators.debug</summary>

- `@debug`   -> prints the return value of a function
- `@important`   -> prints the return like debug with extra chars so it stands out
</details>

## 2. Converter:
`vicolib.converter.Time`
<details><summary>Time.stamp_now( format: string )</summary>

- **description:** Converts the current time to a formattable timestamp string
- **params:** *format: string* -> e.g. "%Y/%m/%d" or from formats dict:

#### Predefined Formats:
| Key          |    Format        | Example Output         | Description |
| -----------  | ---------------- | ---------------------- | ------------ 
| "def"        | %Y/%m/%d - %X  | 2023/2/4 - 18:30:26      | Default 
| "dmy"        | %d.%m.%Y"      | 4.2.2023                 | Day.Month.Year
| "dmy-time"   | %d.%m.%Y - %X  | 4.2.2023 - 18:30:26      | Day.Month.Year with time
| "ymd"        | %Y/%m%d        | 2023/2/4                 | Year/Month/Day
| "ymd-time"   | %Y/%m/%d - %X  | 2023/2/4 - 18:30:26      | Year/Month/Day with time
| "time"       | %X             | 18:30:26                 | Time with seconds
| "time-short" | %H:%M          | 18:30                    | Time without seconds
| "time-apm"   | %I:%M %p       | 6:30 PM                  | Time with AM / PM
| "written"    | %A %d. %B %Y   | Sunday 12. February 2023 | Written Date



- **return:** *str* (like "2023/2/4 - 18:30:26")
</details>
<details><summary>Time.us_to_ms(us)</summary>

- **description:** Converts microseconds (us) to milliseconds (ms). (us = ms / 1000)
- **params:** microsecond as string, int or float
- **return:** int
</details>

<details><summary>Time.ms_to_us(ms)</summary>

- **description:** Converts milliseconds (ms) to microseconds (us). (us = ms * 1000)
- **params:** microsecond as string, int or float
- **return:** int
</details>

# TODO:
- [x] Nothing to do here :eyes:
- [x] Open for requests :smile:

# Example Code:
### main.py

```python
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


```
### Output
```
Timestamp Now: 2023/02/13 - 10:01:07
Timestamp Now Formattet: 13.02.2023
Timestamp Now Formattet: 2023,13 Month: 01
BENCH_TIME: bench_test took 0.585132360458374 seconds to execute
[2023/02/13 - 10:01:07]: debug_test -> Long Return Debug Text
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[2023/02/13 - 10:01:07]: debug_important_test -> Long Return Debug Text
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
===========================================================
[2023/02/13 - 10:01:07]: debug_my_decorator -> My Test Text
===========================================================
```
# Licence (MIT):
### **[LICENCE.txt](LICENCE.txt)**