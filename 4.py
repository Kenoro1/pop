entering = input('Введите строку из нескольких слов с пробелами: ').split(' ')


print(entering)
for a, b in enumerate(entering):
    print(a, b)