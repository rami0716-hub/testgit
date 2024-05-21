

#def capitalize_and_ascii_sum(word: str):
 #   return sum(ord(x) for x in word.capitalize())

#animals = ["ant","elephant","dog"]
#animal_output = list(map(capitalize_and_ascii_sum,animals))
#print(animal_output)

def square(x):
    return x**2
    #lambda x: x**2
numbers = [1,2,3,4]

squares = map(lambda x: x**2, numbers)
print(list(squares))