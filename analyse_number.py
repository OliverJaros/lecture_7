
def is_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False


my_numbers = [-5, 4.5, 2, 3, 4]
for my_number in my_numbers:
    print(is_even_number(my_number))
##