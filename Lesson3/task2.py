def user(sname,name,birth,city,email,phone):
    print(f"Вас зовут {sname} {name}\nГод рождения: {birth}\nГород: {city}\nE-mail: {email}\nТелефон: {phone}")

user(name = input('Введите имя: '), sname = input('Введите фамилию: '), birth = input('Введите год рождения: '), city = input('Введите город проживания: '), email = input('Введите e-mail: '), phone = input('Введите телефон: '))
