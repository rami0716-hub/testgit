def capitalize_and_ascii_sum(word: str):
    return sum(ord(x) for x in word.capitalize())

animals = ["ant","elephant","dog"]
animal_output = list(map(capitalize_and_ascii_sum,animals))
print(animal_output)