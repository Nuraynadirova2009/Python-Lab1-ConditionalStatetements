set1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
set2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
set4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
set5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

day = 0

print(set1)
if int(input("Set 1-də var? (1 / 0): ")) == 1:
    day += 1

print(set2)
if int(input("Set 2-də var? (1 / 0): ")) == 1:
    day += 2

print(set3)
if int(input("Set 3-də var? (1 / 0): ")) == 1:
    day += 4

print(set4)
if int(input("Set 4-də var? (1 / 0): ")) == 1:
    day += 8

print(set5)
if int(input("Set 5-də var? (1 / 0): ")) == 1:
    day += 16

print("Doğum günün:", day)
