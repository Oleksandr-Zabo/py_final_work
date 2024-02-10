import random

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


# 7
student_names = ["Oliver", "Sophia", "William", "Emma", "Henry"]
student_grades = {}
for name in student_names:
    grade = random.randint(6, 12)
    student_grades[name] = grade
best_student = max(student_grades, key=student_grades.get)
print(f"Студент з найвищою оцінкою: {best_student} (оцінка: {student_grades[best_student]})")


# 8
def start_upeer(list_str):
    new_list = [string for string in list_str if string[0].isupper()]
    return new_list


num_str8 = int(input("Введи кількість рядків: "))
list_of_str8 = []
for i in range(num_str8):
    string_u = input("Введи рядок: ")
    list_of_str8.append(string_u)
print(start_upeer(list_of_str8))


# 9
def have_python(list_str):
    new_list = [string for string in list_str if "Python" in string]
    return new_list


num_str8 = int(input("Введи кількість рядків: "))
list_of_str9 = []
for i in range(num_str8):
    string_u = input("Введи рядок: ")
    list_of_str9.append(string_u)
print(have_python(list_of_str9))

# Частина 2
print("Python вікторина")

questions = ["Що таке інтерпретатор Python?", "Які типи даних є в Python?",
             "Як створити список цілих чисел від 1 до 10 включно?", "Як вивести перший елемент зі списку?",
             "Як перевірити, чи є елемент у списку?"]
right_answers = [
    "Інтерпретатор - це місце, де ви пишете код і яке обробляє процес його виконання. Він відповідає за запуск вашого коду",
    "В Python є різні типи даних, такі як цілі числа, дійсні числа, рядки, списки, кортежі, словники, множини та булеві значення",
    "my_list = list(range(1, 11))", "print(my_list[0])", "if element in my_list:"]
answers_1 = ["Інтерпретатор - це програма, яка перетворює Python-код на машинний код",
             "Інтерпретатор - це інструмент для створення графічних інтерфейсів користувача",
             "Інтерпретатор - це набір стандартних функцій Python"]
answers_2 = ["Типи даних в Python обмежуються лише цілими числами та рядками", "В Python немає типу даних список",
             "Типи даних в Python визначаються виключно користувачем"]

answers_3 = ["my_list = [x for x in range(10)]", "my_list = list(range(1, 11, 2))",
             "my_list = [1, 2, 3, 4, 4, 6, 7, 8, 9, 10]"]
answers_4 = ["print(my_list[-1])", "print(my_list[1])", "print(my_list[len(my_list) - 1])"]
answers_5 = ["if element not in my_list:", "if element == my_list:", "if element is my_list:"]
list_to_text = []
user = input("Введи твоє ім'я: ")


def question_answers(user_name, question, answers, right_answer):
    print(f"{user_name}. Питання:\n{question}")
    a = range(1, 5)
    list_answ = random.sample(a, 4)
    list_ansers = []
    for j in list_answ:
        if j == 1:
            list_ansers.append(right_answer)
        elif j == 2:
            list_ansers.append(answers[0])
        elif j == 3:
            list_ansers.append(answers[1])
        else:
            list_ansers.append(answers[2])
    dict_answ = {1: list_ansers[0], 2: list_ansers[1], 3: list_ansers[2], 4: list_ansers[3]}
    for key, value in dict_answ.items():
        print(key, ".", value)
    user_answer = int(input("Введи відповідь(цифра): "))
    if dict_answ[user_answer] == right_answer:
        print("Відповідь зараховано")
        return "Відповідь правильна\n"
    else:
        print("Відповідь зараховано")
        return f"Правильна відповідь: {right_answer}\n"


for i in range(5):
    if i == 0:
        list_to_text.append(question_answers(user, questions[0], answers_1, right_answers[0]))
    elif i == 1:
        list_to_text.append(question_answers(user, questions[1], answers_2, right_answers[1]))
    elif i == 2:
        list_to_text.append(question_answers(user, questions[2], answers_3, right_answers[2]))
    elif i == 3:
        list_to_text.append(question_answers(user, questions[3], answers_4, right_answers[3]))
    else:
        list_to_text.append(question_answers(user, questions[4], answers_5, right_answers[4]))

right_as = list_to_text.count("Відповідь правильна\n")


def write_results(userr, res_list, mark, file1):
    f_line = f"Результати {userr}:\nОцінка:{mark} з 5\n"
    with open(file1, "w", encoding="utf-8") as file:
        file.write(f_line)

    with open(file1, "a", encoding="utf-8") as file:
        file.writelines(res_list)

    print(f"Результати {userr}:\nОцінка:{mark} з 5")
    print("\n".join(res_list))


write_results(user, list_to_text, right_as, "results.txt")
