


some_list = [23.5, 38.7, 2941, 853.1, 34, 124.21, 22, 23, 48, 93.2, 45124, 411, 3623, 215.3, 697.4, 478, 2, 41, 1, 939, 0.23]
some_list.sort()

print(id(some_list))
print(id(some_list))

price_list = ''
for i in some_list:
    if some_list.index(i) < len(some_list) and isinstance(i, float):
        rubls = str(i).split('.')[0]
        cops = str(i).split('.')[1]
        price_list += f'{rubls} руб {cops:02} коп, '
    elif some_list.index(i) < len(some_list):
        price_list += f'{i} руб, '

print('Прайс', price_list.rstrip(', '))

some_list.sort(reverse=True)

print('Проверка ID ', id(some_list))

top_price = ''

for i in some_list[:5]:
    if some_list.index(i) < len(some_list[:5]) and isinstance(i, float):
        rub = str(i).split('.')[0]
        cope = str(i).split('.')[1]
        top_price += f'{rub} руб {cope:02} коп, '
    elif some_list[:5].index(i) < len(some_list[:5]):
        top_price += f'{i} руб, '
        
print('5 наиболее высоких цен в прайсе', top_price.rstrip(', '))