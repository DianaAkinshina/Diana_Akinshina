my_string = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!'

print(f'''
       Шаг 1: Количество символов равно  {len(my_string)}
       Шаг 2: Развернуть строку --> {my_string[::-1]}
       Шаг 3: Сделать каждое слово с большой буквы -->  {my_string.title()}
       Шаг 4: Сделать весь текст прописными буквами-->  {my_string.upper()}
       Шаг 5: Найти число вхождений "нд", "ам", "о" в строку. 
              5.1 "нд" повторяется в сторке {my_string.count('нд')} раз
              5.2 "ам" повторяется в сторке {my_string.count('ам')} раза
              5.3 "о" повторяется в сторке {my_string.count('о')} раз
       Шаг 6: Собственные упражнения-->
              6.1 Замена города:  {my_string.replace('Лондоне', 'Монте-Карло')}
              6.2 Работа с регистром: {my_string.swapcase()}
              6.3 Удаление префикса и суффикса: {my_string.removeprefix('Не знаю,').removesuffix('человека!')}
              6.4 Удаление из середины:  {my_string.replace('Может, там собака — друг человека.', '')}
                             
       ''')

my_string_split = my_string.split()
reverse_my_string = ' '.join(my_string_split[::-1])

print(f'''
       Шаг 7: Развернуть предложение:  {reverse_my_string}
       Шаг 8: Вывести в консоль исходную строку  {my_string}''')
