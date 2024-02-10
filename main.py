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
for i in range(1, 100+1):
    if i % 2 == 0:
        sum_range3 += i
print(sum_range3)
