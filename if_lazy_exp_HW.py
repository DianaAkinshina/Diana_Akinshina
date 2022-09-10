num_1 = int(input('Ведите 1-ое число -->  '))
num_2 = int(input('Ведите 2-ое число -->  '))
num_3 = int(input('Ведите 3-ое число -->  '))

num_1 != 0 and num_2 != 0 and num_3 != 0 and print("Нет нулевых значений!!!")

num_1 != 0 or num_2 != 0 or num_3 != 0
first_not_nul = num_1 or num_2 or num_3 or ''
print(f"Первое ненулевое значение равно  {first_not_nul}")

num_1 == 0 and num_2 == 0 and num_3 == 0 and print("Введены все нули!")

if num_1 > (num_2+num_3):
    print(f"{num_1} больше суммы {num_2} и {num_3}, выводим  {num_1-num_2-num_3}")

else:
    print(f"{num_1} меньше суммы {num_2} и {num_3}, выводим  {num_2+num_3-num_1}")

if num_1 > 50 and num_2 > num_1 or num_3 > num_1:
    print("Вася")
elif num_1 > 5 or num_2 == 7 and num_3 == 7:
    print("Петя")
