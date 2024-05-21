'''
def is_even(num):
    return num%2 == 0
#print(is_even(10))

list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_2 = filter(is_even, list_1)

print(list(list_2))
'''
def is_odd(num):
    return num%2 != 0
#print(is_even(10))

list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_2 = filter(is_odd, list_1)

print(list(list_2))