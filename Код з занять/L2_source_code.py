
# Online Python - IDE, Editor, Compiler, Interpreter

sum_of_ages = 0
sum_of_apples = 0

def greet():
    # print - виводить інформацію у консоль
    print("Hello")
    
def kvadrat4():
    # print - виводить інформацію у консоль
    print("kvadrat chisla 4 = 16")
    
def cube_of_4():
    # print - виводить інформацію у консоль
    result = 4 ** 3
    print(f'Cube of {4} = {result}')  
    
def add_apples():
    a = 2
    b = 9
    c = a + b
    # global sum_of_apples = c
    print(f'Sum of {a} and {b} is {c}')
    
def add_my_age_with_artems_age() -> None:
    my_age = 33
    artems_age = 46
    result = my_age + artems_age
    # global sum_of_ages = result
    return None
    print(f'Sum of {my_age} and {artems_age} is {result}')
    return None
    
    
def add_numbers() -> int:
    a = 4
    b = 5
    c = a + b
    print(f'Sum of {a} and {b} is {c}')
    return c

def cube_of(number: int) -> int:
    # print - виводить інформацію у консоль
    result = number ** 3
    print(f'Cube of {number} = {result}')
    return result


    # a = "print - виводить інформацію у консоль"
    # print(a)
# # print("Vsim dobroho ranku")
# greet() # виклик функції
# kvadrat4()
# add_apples()
# add_my_age_with_artems_age()
# # print(f'Sum of ages {sum_of_ages} and apples {sum_of_apples} is {sum_of_ages + sum_of_apples}')
# # print(add_apples() + add_apples())
# cube_of_4()
# cube_of(5)
# cube_of(6)

sum_of_cubes = 0
loop_count = 0
for i in range(0, 11):
    c = cube_of(number=i) 
    if c > 500:
        break # пририває цикл і переходить на наступну інструкцію після циклу while/for
    sum_of_cubes = sum_of_cubes + c
    loop_count = i

print(f'Sum of cubes from 0 to {loop_count} = {sum_of_cubes}')

add_my_age_with_artems_age()