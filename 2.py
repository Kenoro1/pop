enter = input('Enter numbers(123456): ')

my_list_1 = list(enter)

a = 0
for i in range(int(len(my_list_1)/2)):
    my_list_1[a], my_list_1[a + 1] = my_list_1[a + 1], my_list_1[a]
    a += 2

print(my_list_1)