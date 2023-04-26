city1, city2, city3 = input(), input(), input()
min = min(len(city1), len(city2), len(city3))
max = max(len(city1), len(city2), len(city3))
if len(city1) == min:
    print(city1)
elif len(city2) == min:
    print(city2)
else:
    print(city3)
if len(city1) == max:
    print(city1)
elif len(city2) == max:
    print(city2)
else:
    print(city3)
