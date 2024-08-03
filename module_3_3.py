def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2,  '4')
print_params('Один аргумент')
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [17, 'Урбан', False]
values_dict = {'a': 24, 'b': 'Urban', 'c': (1, 2, 3)}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Спасибо вам кураторы и преподаватели!']
print_params(*values_list_2, 42)
