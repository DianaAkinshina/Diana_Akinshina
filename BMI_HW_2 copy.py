
user_weight = float(input("Введите ваш вес в кг --> "))
user_hight = float(input("Введите ваш рост в см --> "))
user_BMI = round(user_weight/(user_hight/100)**2,2)

print(f'''
      Индекс массы вашего тела составляет: {user_BMI}
                     
            {'10'+'='*int(user_BMI)+'|'+'='*(45-int(user_BMI))+"45"}'''
     )

