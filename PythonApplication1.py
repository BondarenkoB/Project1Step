# -*- coding: cp1251 -*- 
import random
import string
    #gen
def generate_password():
    try:
    #print input value
        length = int(input("������ ������� ������: "))
        special_characters = input("�������� ��������� �������? (y/n): ")
        numbers = input("�������� �����? (y/n): ")
        upper_case = input("�������� ����� ��������� �������? (y/n): ")
        lower_case = input("�������� ����� �������� �������? (y/n): ")
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
        print("�������: ������� ���������� ��������.")
    except IndexError:
        print("�������: ������� ���������� ��������.")
    else:
        return password
    #succes
print(generate_password())