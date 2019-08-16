from functools import lru_cache
@lru_cache(maxsize=2)
def add(a:int, b:int):
    print("function in {} + {}.".format(a, b))
    return (a+b)

print(add(10,10))
print(add(10,12))
print(add(10,10))
print(add(10,10))
print(add(10,10))
