# put your python code here
col1, col2 = input(), input()
if (col1 == col2
    and (
        col1 == 'красный' or col1 == 'синий' or col1 == 'желтый')):
    print(col1)
elif (col1 == 'красный' and col2 == 'синий') or (col2 == 'красный' and col1 == 'синий'):
    print('фиолетовый')
elif (col1 == 'красный' and col2 == 'желтый') or (col2 == 'красный' and col1 == 'желтый'):
    print('оранжевый')
elif (col1 == 'синий' and col2 == 'желтый') or (col2 == 'синий' and col1 == 'желтый'):
    print('зеленый')
else:
    print('ошибка цвета')
