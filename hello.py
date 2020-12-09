i = 0
sum = 0
for i in range(1,101):
    sum += i
print(f"sum: {sum}")

sum = 0
for i in range(1,101):
    if (i % 2) == 0:
        continue
    else:
        sum += i
print(f"odd sum: {sum}")
