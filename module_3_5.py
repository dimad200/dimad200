# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.

def get_multiplied_digits(number=0):
  str_number = str(number)
  first=int(str_number[0])
  if len(str_number)<2:
    return first
  else:
   return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)

print(result)

# Вывод на консоль:
# 24
