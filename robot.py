from math import sqrt

finish_possition_X = 0
finish_possition_Y = 0

def distance(X,Y):
    return round(sqrt((X**2 + Y**2)), 3)

while True:
    choose_direction = input("Введите направление движения и количество шагов: R, L, U, D   ")
    if choose_direction == '':
        break
    for item in choose_direction:
        if item[0] == 'R':
            finish_possition_X += int(choose_direction[2:])
        elif item[0] == 'L':
            finish_possition_X -= int(choose_direction[2:])
        elif item[0] == 'U':
            finish_possition_Y += int(choose_direction[2:])
        elif item[0] == 'D':
            finish_possition_Y -= int(choose_direction[2:])
print(f'Расстояние от точки старта до конечно составляет {distance(finish_possition_X,finish_possition_Y)} единиц')