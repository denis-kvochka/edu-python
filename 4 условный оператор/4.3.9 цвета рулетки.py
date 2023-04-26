# put your python code here
n = int(input())
if not (0 <= n <= 36):
    print('ошибка ввода')
elif n == 0:
    print('зеленый')
# black
elif ((((1 <= n <= 10 or 19 <= n <= 28) and n % 2 == 0) or
      (11 <= n <= 18 or 29 <= n <= 36) and n % 2 != 0)):
    print('черный')
else:
    print('красный')
