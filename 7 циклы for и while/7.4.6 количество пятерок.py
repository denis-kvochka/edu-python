pupil_mark, count_of_fives = int(input()), 0
while 0 < pupil_mark < 6:
    if pupil_mark == 5:
        count_of_fives += 1
    pupil_mark = int(input())
print(count_of_fives)
