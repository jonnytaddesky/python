count_cups = int(input("Введите колличество чашек: "))
cups = 6

if count_cups < cups:
    print("Бонуcных чашек: 0")
elif count_cups % cups == 0:
    bonus_count_cups = count_cups / cups
    print(f"Бонуcных чашек: {int(bonus_count_cups)}")
else:
    print(f"Бонуcных чашек: {int(count_cups//cups)}")

count_cups = int(input("Введите колличество чашек: "))
print(f"Бонуcных чашек: {count_cups // 6}")
