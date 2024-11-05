# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.



# Пункты задачи:

# Напишите функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number=0):
  str_number = str(number)
  first=int(str_number[0])
  if len(str_number)<2:
    return first
  else:
    print("first=",first)
    print("str_number[1:]=", str_number[1:])
    print("int(str_number[1:])=", int(str_number[1:]))
    print ("first * str_number[1:]",first ,str_number[1:])
  return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)

print(result)

# Вывод на консоль:

# 24



# Примечания:

# При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
# Если возникает ошибка, рекомендуется пошагово отладить программу "жучком". Чаще всего ошибка заключается в бесконечной рекурсии или же в неверном обращении по индексу.
