# Decorator way — exactly same outcome
import builtins

original_len = builtins.len
original_print = builtins.print   # save before ANY override
oritinal_range = builtins.range

def len_decorator(func):
    def wrapper(obj):
        builtins.print(f"[LOG]: {type(obj).__name__} {original_len(obj)}")
        return func(obj)
    return wrapper

builtins.len = len_decorator(builtins.len)   # decorator applied manually

len([1,2,3])



# ─── RANGE DECORATOR ─────────────────────────────────
def range_decorator(func):
    def return_modified_range(start: int = 0, stop: int = 10, step: int = 1):
        original_print(f"[LOG]: range called with args {start} {stop} {step}")
        result =  func(start, stop+1, step)
        return result
    return return_modified_range

builtins.range = range_decorator(builtins.range)

lst = list(range(1, 5))
print(lst)

lst = list(oritinal_range(1, 5))
print(lst)



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

@log
def subtract(a, b):
    return a - b

@log
def multiply(a, b):
    return a * b

print( add(3, 5) )       # [LOG] add called
print( subtract(10, 4) )  # [LOG] subtract called
print( multiply(3, 5) )  # [LOG] multiply called