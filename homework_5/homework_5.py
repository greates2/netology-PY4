#Исходные данные

students = {
  "student_1" : {"first_name" : "Вадим",
                 "last_name" : "Адельбаев",
                 "sex" : "Мужской",
                 "experience" : False,
                 "homework" : [10, 10, 10, 10, 10],
                 "exam" : 10},
  "student_2" : {"first_name" : "Никита",
                 "last_name" : "Безгрешнов",
                 "sex" : "Мужской",
                 "experience" : False,
                 "homework" : [1, 2, 3, 4, 5],
                 "exam" : 4},
  "student_3" : {"first_name" : "Вадим",
                 "last_name" : "Плотников",
                 "sex" : "Мужской",
                 "experience" : False,
                 "homework" : [10, 10, 10, 10, 10],
                 "exam" : 10},
  "student_4" : {"first_name" : "Екатерина",
                 "last_name" : "Рышкова",
                 "sex" : "Женский",
                 "experience" : True,
                 "homework" : [9, 9, 2, 6, 5],
                 "exam" : 2},
  "student_5" : {"first_name" : "Александр",
                 "last_name" : "Исайченко",
                 "sex" : "Мужской",
                 "experience" : True,
                 "homework" : [2, 2, 7, 3, 4],
                 "exam" : 3},
  "student_6" : {"first_name" : "Александр",
                "last_name" : "Иванов",
                "sex" : "Мужской",
                "experience" : True,
                "homework" : [1, 9, 3, 6, 8],
                "exam" : 9}
}

#####################################################
#########1 часть  задания############################
#####################################################

def get_result_all_homework():# Средняя оценка за домашние задания по группе:X
    result_all_homeworks = list() #Сумма всех оценок за домашку
    for students_homework_key, students_homework_val in students.items():
        #print(students_val['homework']) #Выводим уникальное имя студента
        k = list(students_homework_val['homework'])
        k = sum(k) / len(students_homework_val['homework'])#берем среднее за homework
        # print(k)
        result_all_homeworks.append(k)
    result_all_students = sum(result_all_homeworks) #суммируем средние значения homework
    print("Средняя оценка за домашние задания по группе: ", round(result_all_students / len(result_all_homeworks), 2))

def get_result_all_exam():# Средняя оценка за экзамен: Y
    result_all_exams = list() #Сумма всех оценок за экзамен
    for students_exam_key, students_exam_val in students.items():
        #print(students_exam_val)
        v = dict(students_exam_val)
        #print(v)
        v = int(students_exam_val['exam'])
        # print(type(v))
        result_all_exams.append(v)
    result_all_exams_len = len(result_all_exams)
    result_all_exams = sum(result_all_exams)
    print("Средняя оценка за экзамен у группы:", round((result_all_exams / result_all_exams_len), 2))

#####################################################
#########2 часть  задания############################
#####################################################

def get_calculate_sex_homework(input_sex):#среднеюю оценку за домашние задания и за экзамен по группе в разрезе: а)пола - U
    max_valuation_men = list()
    max_valuation_female = list()
    for student_name in students.values():
        if student_name['sex'] == input_sex:
            k = student_name['homework']
            k = sum(k) / len(student_name['homework'])
            max_valuation_men.append(k)
    print("Средний бал {} аудитории - {}".format(input_sex.lower(), round(sum(max_valuation_men) / len(max_valuation_men), 2)))


def get_calculate_exp_homework(input_exp):#среднеюю оценку за домашние задания и за экзамен по группе в разрезе: б)наличия опыта в виде: - T
    max_valuation_with_exp = list()
    for student_name in students.values():
        if student_name['experience'] == input_exp:
            k = student_name['homework']
            k = sum(k) / len(student_name['homework'])
            max_valuation_with_exp.append(k)
    print("Средний бал учеников с опытом (если True - то да, если False - то нет) {} - {}".format(str(input_exp), round(sum(max_valuation_with_exp) / len(max_valuation_with_exp), 2)))

def get_male_homework():# Средняя оценка за домашние задания у мужчин: A
    male_homework = list()
    for student_name in students.values():
        if student_name['sex'] == "Мужской":
            new_male_homework = list(student_name['homework'])
            # print(new_male_homework)
            new_male_homework = sum(new_male_homework) / len(student_name['homework']) #делим homework на количество значений
            # print(new_male_homework)
            male_homework.append(new_male_homework)
    print("Средний бал мужчин -", round(sum(male_homework) / len(male_homework), 2))

# Средняя оценка за домашние задания у женщин: C
def get_female_homework():
    female_homework = list()
    for student_name in students.values():
        if student_name['sex'] == "Женский":
            new_female_homework = list(student_name['homework'])
            new_female_homework = sum(new_female_homework) / len(new_female_homework)
            female_homework.append(new_female_homework)
    print("Средний бал женщин -", round(sum(female_homework) / len(female_homework), 2))

def get_male_exam():# Средняя оценка за экзамен у мужчин: B
    male_exam = list()
    for student_name in students.values():
        if student_name['sex'] == "Мужской":
            # print(student_name['exam'])
            new_male_exam = int(student_name['exam'])
            # print(new_male_exam)
            male_exam.append(new_male_exam)
    print("Средний бал за экзамен у мужчин -", round(sum(male_exam) / len(male_exam), 2))

def get_female_exam():# Средняя оценка за экзамен у женщин: D
    female_exam = list()
    for student_name in students.values():
        if student_name['sex'] == "Женский":
            # print(student_name['exam'])
            new_female_exam = int(student_name['exam'])
            # print(new_male_exam)
            female_exam.append(new_female_exam)
    print("Средний бал за экзамен у женщин -", round(sum(female_exam) / len(female_exam), 2))

def get_with_exp_homework():# Средняя оценка за домашние задания у студентов с опытом: E
    with_exp_homework = list()
    for student_name in students.values():
        if student_name['experience'] == True:
            new_with_exp_homework = list(student_name['homework'])
            new_with_exp_homework = sum(new_with_exp_homework) / len(new_with_exp_homework)
            with_exp_homework.append(new_with_exp_homework)
    print("Средний бал за домашку у студентов с опытом -", round(sum(with_exp_homework) / len(with_exp_homework), 2))

def get_without_exp_homework():#Средняя оценка за домашние задания у студентов без опыта: G
    without_exp_homework = list()
    for student_name in students.values():
        if student_name['experience'] == False:
            new_without_exp_homework = list(student_name['homework'])
            new_without_exp_homework = sum(new_without_exp_homework) / len(new_without_exp_homework)
            without_exp_homework.append(new_without_exp_homework)
    print("Средний бал за домашку у студентов без опыта -", round(sum(without_exp_homework) / len(without_exp_homework), 2))

def get_with_exp_exam():# Средняя оценка за экзамен у студентов с опытом: F
    with_exp_exam = list()
    for student_name in students.values():
        if student_name['experience'] == True:
            new_with_exp_exam = int(student_name['exam'])
            with_exp_exam.append(new_with_exp_exam)
    print("Средний бал за экзамен у мужчин -", sum(with_exp_exam) / len(with_exp_exam))

def get_without_exp_exam():# Средняя оценка за экзамен у студентов без опыта: H
    without_exp_exam = list()
    for student_name in students.values():
        if student_name['experience'] == False:
            new_without_exp_exam = int(student_name['exam'])
            without_exp_exam.append(new_without_exp_exam)
    print("Средний бал за экзамен у женщин -", round(sum(without_exp_exam) / len(without_exp_exam), 2))

#####################################################
#########3 часть  задания############################
#####################################################

#Лучший студент: S с интегральной оценкой Z
def get_best_of_the_best():
    best_of_the_best = dict()
    for best_student in students.values():
        k = round(0.6 * (sum(best_student['homework'])/len(best_student['homework'])) + (0.4 * int(best_student['exam'])))
        new_name_stud = best_student['first_name'] + " " + best_student['last_name']
        best_of_the_best.update({new_name_stud: k})
    #1 версия вывода максимального значения
    # inverse = [(value, key) for key, value in best_of_the_best.items()]
    # print("Лучший студент, это {} с оценкой {}".format(max(inverse)[1], max(inverse)[0]))#инвертируем список и выводим максимальное число
    # 2 версия вывода максимального значения
    best_students = list()
    for best_of_the_best_2 in best_of_the_best.items():
        # print(best_of_the_best_2)
        k = max(best_of_the_best, key=best_of_the_best.get)
        y = best_of_the_best[k]
        if y in best_of_the_best_2:# and (best_of_the_best_2[1] >= 2) не работает это условие
            best_students.append(best_of_the_best_2)
            # print("Лучший студент - {} с оценкой {}".format(best_of_the_best_2[0], best_of_the_best_2[1]))
    if len(best_students) > 1:
        print("Лучшие студенты: \n", end="")
        for best_student_ended in best_students:
            print("{} с оценкой {}".format(best_student_ended[0], best_student_ended[1]))
    elif len(best_students) == 1:
        for best_student_ended in best_students:
            print("Лучший студент - {} с оценкой {}".format(best_student_ended[0], best_student_ended[1]))

def main():
    calculate_male_female_homework = input("\n \
    Средняя оценка за домашние задания по группе: X \n \
    Средняя оценка за экзамен: Y \n \
    среднеюю оценку за домашние задания и за экзамен по группе в разрезе: а)пола - U \n \
    среднеюю оценку за домашние задания и за экзамен по группе в разрезе: б)наличия опыта в виде, нажмите - T \n \
    Для подсчета среднего бала у мужчин, нажмите - A, для женщин - C \n \
    Средняя оценка за экзамен у мужчин, нажмите - B, для женщин - D \n \
    Средняя оценка за домашнее задание у студентов с опытом, мужчины - E, женщины - G \n \
    Средняя оценка за экзамен у студентов с опытом, мужчины - F, женщины - H \n \
    Лучший студент - нажмите Z")

    if calculate_male_female_homework == "X":#Средняя оценка за домашние задания по группе: X
        get_result_all_homework()
    if calculate_male_female_homework == "Y":#Средняя оценка за экзамен: Y
        get_result_all_exam()
    if calculate_male_female_homework == "U":#среднеюю оценку за домашние задания и за экзамен по группе в разрезе: а)пола: E
        input_sex = input("Введите пол ученика (Мужской или Женский)")
        get_calculate_sex_homework(input_sex)
    if calculate_male_female_homework == "T":#среднеюю оценку за домашние задания и за экзамен по группе в разрезе: б)наличия опыта в виде: T
        input_exp = bool(input("Введите опыт ученика (если ничего не вводить, то False и наоборот)"))
        get_calculate_exp_homework(input_exp)
    if calculate_male_female_homework == "A":# Средняя оценка за домашние задания у мужчин: A
        get_male_homework()
    if calculate_male_female_homework == "C":# Средняя оценка за домашние задания у женщин: C
        get_female_homework()
    if calculate_male_female_homework == "B":#Средняя оценка за экзамен у мужчин: B
        get_male_exam()
    if calculate_male_female_homework == "D":#Средняя оценка за экзамен у женщин: D
        get_female_exam()
    if calculate_male_female_homework == "E":#Средняя оценка за домашние задания у студентов с опытом: E
        get_with_exp_homework()
    if calculate_male_female_homework == "G":#Средняя оценка за домашние задания у студентов без опыта: G
        get_without_exp_homework()
    if calculate_male_female_homework == "F":#Средняя оценка за экзамен у студентов с опытом: F
        get_with_exp_exam()
    if calculate_male_female_homework == "H":#Средняя оценка за экзамен у студентов без опыта: H
        get_without_exp_exam()
    if calculate_male_female_homework == "Z":  # Лучший студент: S с интегральной оценкой Z
        get_best_of_the_best()

main()