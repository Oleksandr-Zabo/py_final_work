print("Hello python exam")

# Частина 1
# 1
print("Привіт, світ!")  # print("Hello world")

# 2
f_numb2 = int(input("Введи перше число: "))
s_numb2 = int(input("Введи друге число: "))
sum_range2 = 0
for i in range(f_numb2 + 1, s_numb2):
    sum_range2 += i
print(f"Сума діапазону чисел : {sum_range2}")

# 3
sum_range3 = 0
for i in range(1, 100 + 1):
    if i % 2 == 0:
        sum_range3 += i
print(sum_range3)

# 4
user_str4 = input("Введи твій рядок: ")
for char in user_str4:
    print(char)

# 5
user_str5 = input("Введи твоє слово: ")
list_1_5 = []
list_2_5 = []
for i in range(len(user_str5)):
    list_1_5.append(user_str5[i])
    list_2_5.append(user_str5[-(i + 1)])
if list_1_5 == list_2_5:
    print("Твоє слово паліндром")
else:
    print("Твоє слово не паліндром")

# 6
list_6 = [x for x in range(1, 25)]
list2_6 = list(filter(lambda x: x % 2 == 0, list_6))
print(list2_6)

