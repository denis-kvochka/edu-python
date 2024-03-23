# price = int(input())
# counter = 0
# while price // 25 != 0:
#     counter +=1
#     price -= 25
# while price // 10 != 0:
#     counter += 1
#     price -= 10
# while price // 5 != 0:
#     counter += 1
#     price -= 5
# while price != 0:
#     counter += 1
#     price -= 1
# print(counter)

# #####  v-- 1 --v #####
# price = int(input())
# coins = 0
# # отсчитываем монеты номиналом по 25
# coins += price // 25
# price %= 25
# # отсчитываем монеты номиналом по 10
# coins += price // 10
# price %= 10
# # отсчитываем монеты номиналом по 5
# coins += price // 5
# price %= 5
# # отсчитываем монеты номиналом по 1
# coins += price // 1
# price %= 1
# print(coins)
# # ^-- 1 --^

# ##### v-- 2 --v #####
# n = int(input())
# k = 0
# for i in (25, 10, 5, 1):
#     while n // i > 0:
#         k += 1
#         n -= i
# print(k)
# # ^-- 2 --^
