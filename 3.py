months = int(input('Введите месяц ввиде целого числа: '))

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if months in winter:
    print('Зима')
if months in spring:
    print('Весна')
if months in summer:
    print('Лето')
if months in autumn:
    print('Осень')

# ----------------------homework_3(2var)_____________________

months = int(input('Введите месяц ввиде целого числа: '))

dict_months = {
    [12, 1, 2]:'Зима',
    [3, 4, 5]:'Весна',
    [6, 7, 8]:'Лето',
    [9, 10, 11]:'Осень'

}

if months in dict_months.keys():
    print(dict_months.values())

