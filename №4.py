a = input("Введите первый цвет: ")
b = input("Введите второй цвет: ")
colors = ('красный', 'синий', 'жёлтый', 'желтый')

if a in colors and b in colors:
    if a != b:
        if (a in ('красный','синий')) and (b in ('красный','синий')):
            print('фиолетовый')
        if (a in ('красный', 'жёлтый', 'желтый')) and (b in ('красный', 'жёлтый', 'желтый')):
            print('оранжевый')
        if (a in ('синий', 'жёлтый', 'желтый')) and (b in ('синий', 'жёлтый', 'желтый')):
            print('зеленый')
    else:
        print(a)
else:
    print("Ошибка! Набран не основной цвет")
