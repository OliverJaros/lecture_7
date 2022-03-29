
def is_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False



my_numbers = [-5, 5, 1.2, 5]
for my_number in my_numbers:
    print(is_even_number(my_number))
##