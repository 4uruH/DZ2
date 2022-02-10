some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']


i = 0
while i < (len(some_list)):
    if some_list[i][-1:].isdigit() and not some_list[i].count('.'):
        if -10 < int(some_list[i]) < 0:
            some_list[i] = '0'.join(some_list[i])
        elif 0 < int(some_list[i]) < 10:
            some_list[i] = f'{0}{some_list[i]}'
        some_list.insert((i + 1), '"')
        some_list.insert(i, '"')
        i += 3
    i += 1

result = ''
for ind in some_list:
    if not ind[-1:].isdigit():
        result += ind + ' '
    elif ind[-1:].isdigit():
        result = result[:-1] + ind

print(result)