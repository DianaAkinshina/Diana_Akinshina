
user_weight = float(input("Введите ваш вес в кг --> "))
user_hight = float(input("Введите ваш рост в см --> "))
user_gender = input("""Ваш пол: введите М - если муж. Ж - если жен.-->  """)
user_age = int(input("Введите ваш возраст-->  "))
user_BMI = round(user_weight/(user_hight/100)**2,2)

print(f'''
      Индекс массы вашего тела составляет: {user_BMI}
                     
      {'10'+'='*int(user_BMI)+'|'+'='*(45-int(user_BMI))+"45"}'''
     )

if user_gender == "М" and user_age <= 45:
      if user_BMI < 16.5:
            print(
               f"""
               1.Вам неободимо набрать вес.
               2.Вам необходимо обратиться к врачу.
               3.Вам необходимо есть пищу, богатую белком.""" 
               )
      elif  16.5 <= user_BMI < 40:
            print(
               f"""
               1.Вам неободимо поддерживать текущий вес.
               2.Вам необходимо есть пищу, богатую белком и клетчаткой
               3.Вам необходимо следить за физической активностью.""" 
               )
      elif  user_BMI >= 40:
            print(
               f"""
               1.Вам неободимо снизить вес.
               2.Вам необходимо есть больше овощей и отказаться от быстрых углеводов.
               3.Вам необходимо заниматься спортом каждый день.""" 
               )
elif user_gender == "М" and user_age > 45:
      if user_BMI < 16.5:
            print(
               f"""
               1.Вам необходимо срочно обратиться к врачу.
               2.Вам необходимо есть больше сладкого.
               3.Вам необходимо меньше двигаться""" 
               )
      elif  16.5 <= user_BMI < 40:
            print(
               f"""
               1.Вам неободимо продолжать вести активный образ жизни.
               2.Вам необходимо употреблять витамины.
               3.Вам необходимо следить за давлением.""" 
               )
      elif  user_BMI >= 40:
            print(
               f"""
               1.Вам неободимо срочно снизить вес.
               2.Вам необходимо сесть на низкоуглеводную диету.
               3.Вам необходимы кардиотренировки каждый день.""" 
               )
elif user_gender == "Ж" and user_age <= 39:
      if user_BMI < 16.5:
            print(
               f"""
               1.Вам неободимо быстрее набрать вес.
               2.Вам необходимо срочно обратиться к врачу.
               3.Вам необходимы силовые тренировки.""" 
               )
      elif  16.5 <= user_BMI < 40:
            print(
               f"""
               1.Вам неободимо продолжать вести активный образ жизни.
               2.Вам необходимо следить за продолжительностью сна.
               3.Вам необходимо употреблять больше овощей и меньше сладостей""" 
               )
      elif  user_BMI >= 40:
            print(
               f"""
               1.Вам неободимо как можно быстрее снизить вес.
               2.Вам необходимо оратится к эндокринологу.
               3.Вам необходимо заниматься кардиотренировками каждый день.""" 
               )
elif user_gender == "Ж" and user_age > 39:
      if user_BMI < 16.5:
            print(
               f"""
               1.Вам необходимо пройти мед. обследование.
               2.Вам необходимо изменить образ жизни.
               3.Вам необходимо употреблять специальные добавки к пище.""" 
               )
      elif  16.5 <= user_BMI < 40:
            print(
               f"""
               1.Вам неободимо вести активный образ жизни.
               2.Вам необходимо есть больше овощей и фруктов.
               3.Вам необходимо уменьшить количество сладкого.""" 
               )
      elif  user_BMI >= 40:
            print(
               f"""
               1.Вам неободимо срочно снизить вес.
               2.Вам необходимо полностью отказаться от быстрых углеводов.
               3.Вам необходимы кардиотренировки каждый день.""" 
               )