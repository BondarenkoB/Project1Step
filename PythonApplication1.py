# -*- coding: cp1251 -*- 
import random
import string
    #gen
def generate_password():
    try:
    #print input value
        length = int(input("Введіть довжину пароля: "))
        special_characters = input("Включити спеціальні символи? (y/n): ")
        numbers = input("Включити цифри? (y/n): ")
        upper_case = input("Включити літери верхнього регістру? (y/n): ")
        lower_case = input("Включити літери нижнього регістру? (y/n): ")
     #func
        if special_characters == "y":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            characters = string.ascii_letters + string.digits

        if numbers == "n":
            characters = characters.translate(str.maketrans("", "", string.digits))

        if upper_case == "n":
            characters = characters.translate(str.maketrans("", "", string.ascii_uppercase))

        if lower_case == "n":
            characters = characters.translate(str.maketrans("", "", string.ascii_lowercase))

        password = "".join(random.choice(characters) for i in range(length))
    #error
    except ValueError:
        print("Помилка: Введено некоректне значення.")
    except IndexError:
        print("Помилка: Введено некоректне значення.")
    else:
        return password
    #succes
print(generate_password())