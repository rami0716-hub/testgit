def sum_print(func):
    def wrapper(*args, **kwargs):
        print("using decorator value")
        return(func(*args, **kwargs))
    return wrapper
    
@sum_print
def sum(a: int, b: int) -> int:
    return a+b


@sum_print
def mul(a: int, b: int) -> int:
    return a*b


sum_value = sum(10,30)
print(sum_value)

mul_value = mul(10,30)
print(mul_value)

