#Task 1:

#python code
def find_numbers(start=None, finish=None, divisible_by=None, not_divisible_by=None):
    numbers = []
    for num in range(start, finish+1):
        if num % divisible_by == 0 and num % not_divisible_by != 0:
            numbers.append(num)
    print(numbers)


# Example usage:


find_numbers(start=2000, finish=3200, divisible_by=7, not_divisible_by=5)


# Task 2:


def count_pistas(names):
    count = names.count('Pista')
    return count

names = ['Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']
pistas_count = count_pistas(names)
print(pistas_count)


#Task 3:


def print_hello(count):
    for i in range(count):
        print("Hello!")

def convert_to_number(text):
    try:
        number = int(text)
        return number
    except ValueError:
        return None

user_input = input("Enter a number: ")
number = convert_to_number(user_input)
if number is not None:
    print_hello(number)


#Task 4:


def calculate_area(radius):
    area = 3.14 * (radius ** 2)
    return area

def calculate_circumference(radius):
    circumference = 2 * 3.14 * radius
    return circumference

user_input = input("Enter the radius of a circle: ")
radius = convert_to_number(user_input)
if radius is not None:
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    print("Area:", area)
    print("Circumference:", circumference)


# Task 5:


def sort_and_split_names(names):
    sorted_names = sorted(names)
    midpoint = len(sorted_names) // 2
    group1 = sorted_names[:midpoint]
    group2 = sorted_names[midpoint:]

    for name in group1:
        print(name)
    print("group")
    for name in group2:
        print(name)

names = ['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs', 'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']
sort_and_split_names(names)


#Note: In Task 5, if the number of names is odd, one group will have one more name than the other.
# Backend 1 -homework