import time

start = time.time()
lista = [x*2 for x in range(1000000)]
stop = time.time()

print(stop-start)


def baz():
    pass

def foo(bar):
    print(bar.__name__)

foo(print)

def log(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = funkcja(*args, **kwargs)
        stop = time.time()
        duration = stop - start
        print(f"Długość wywołania {funkcja.__name__} to {duration}s")
        return result
    return wrapper


@log
def foo(arg):
    return f'To jest {arg}'

@log
def dodaj(a, b):
    return a + b


print("-"*20)
wynik = foo("1")
print(wynik)
wynik = dodaj(20, 40)



# def test_decorated_foo():
#     assert "Długość wywołania foo" in foo(1)