
user_weight = float(input("Введите ваш вес в кг --> "))
user_hight = float(input("Введите ваш рост в см --> "))
user_BMI = round(user_weight/(user_hight/100)**2,2)

value_start = '10'
value_end = '45'
value_symbol = '|'
scale_symbol = '='
step_symbol = 2
amount_symbol = 17
BMI_on_scale = (int(user_BMI) - int(value_start))//step_symbol
scale_ = [value_start, scale_symbol*BMI_on_scale, value_symbol, scale_symbol*(amount_symbol-BMI_on_scale), value_end]
print(f'''
      Индекс массы вашего тела составляет: {user_BMI}
                     
            {''.join(scale_)}'''
    )

