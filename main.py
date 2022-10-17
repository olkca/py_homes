while True:

   def ex_1():
       print("Програма №1 \nСкладання числ")
       Number1 = int(input("Перша цифра:"));
       Number2 = int(input("Друга цифра:"));
       Number3 = int(input("Третя цифра:"));
       print("Ваше число:", Number1 * 100 + Number2 * 10 + Number3)


   def ex_2():
       print("Програма №2 \nДобуток числ з числа")
       Number = int(input("Ведіть число, яке складається із чотирьох цифр"));
       Number1 = Number // 1000
       Number2 = Number // 100
       Number2_1 = Number2 % 10
       Number3 = Number // 10
       Number3_1 = Number3 % 10
       Number4 = Number % 10
       print("Число:", Number1 * Number2_1 * Number3_1 * Number4)


   def ex_3():
       print("Програма №3 \nКонвертор вимирів з метрів")
       Metr = int(input("Ведіть метри:"));
       Santimetr = Metr * 100
       Dechemetri = Metr * 10
       Milimetri = Metr * 1000
       Mili = Metr * 0.000621371
       print("Сантиметри:", Santimetr)
       print("Децеметри:", Dechemetri)
       print("Міліметри", Milimetri)
       print("Мілі", Mili)


   def ex_4():
       print("Програма №4 \nКалькулятор прощі трикутника")
       Osnova = int(input("Ведіть довжину основи:"));
       Visota = int(input("Ведіть висоту"));
       S = 0.5 * Osnova * Visota
       print("Площа:", S)


   def ex_5():
       print("Програма №5 \n54Відзеркалення числа")
       Number = int(input("Число до відзеркалення:"));
       Number1 = Number // 1000
       Number2 = Number // 100
       Number2_1 = Number2 % 10
       Number3 = Number // 10
       Number3_1 = Number3 % 10
       Number4 = Number % 10
       print("Відзеркалене число:", Number4 * 1000 + Number3_1 * 100 + Number2_1 * 10 + Number1)

   print("Доброго дня! Виберіть з переліку програму і напишіть номер програми."
         "\n1.Складання числ"
         "\n2.Добуток числ з числа"
         "\n3.Конвертор вимирів з метрів"
         "\n4.Калькулятор прощі трикутника"
         "\n5.Відзеркалення числа")
   class_work = int (input("Ведіть номер програми:"))
   if class_work == 5:
       ex_5()
   if class_work == 4:
       ex_4()
   if class_work == 3:
       ex_3()
   if class_work == 2:
       ex_2()
   if class_work == 1:
       ex_1()