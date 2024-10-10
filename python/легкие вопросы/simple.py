#Условия ##int-cmp Дается два числа a и b. Вернуть: 1, если a > b 0, если a = b -1, если a < b Sample Input: 1 0 Sample Output: 1

##Решение:
# def int_cmp(a,b):
#     if a > b:
#         return 1
#     elif a == b:
#         return 0
#     else:
#         return -1
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print("Compare",a,"and",b,"result",int_cmp(a,b))


##max-of-three Дается три числа a, b и c. Вернуть максимальное число из них. Sample Input: 42 1 0 Sample Output: 42

##Решение:
# def max_of_three(a,b,c):
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     else:
#         print(c)
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# max_of_three(a,b,c)


#Циклы ##sqr-sum-1-n Вернуть сумму квадратов чисел от 1 до n включительно. Ограничения 1 <= n <= 10860

##Решение:
#Sample Input: 3 Sample Output: 14
# def sqr_sum(a):
#     summa = 0
#     for i in range(1,a+1):
#         summa += i ** 2
#     print(summa)
# a = int(input("Введите число: "))
# sqr_sum(a)


##print-even-a-b Вывести в консоль четные числа в диапазоне от a включительно до b включительно. Sample Input: 0 4 Sample Output: 0 2 4

##Решение:
# def print_even(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i)
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print_even(a,b)


##pow-a-b Вернуть число a в степени b. Используя цикл. Ограничения b > 0 a^b входит в ограничения типа int Sample Input: 2 6 Sample Output: 64

##Решение:
# def pow_a_b(a,b):
#     result = 1
#     for i in range(1,b+1):
#         result *= a
#     print(result)
# pow_a_b(2,6)


##calc-deposit Написать функцию, которая возвращает сколько будет денег на депозите через n месяцев при ставке k и изначальном балансе b тенге. Вознаграждения по депозиту начисляются каждый месяц. Ограничения 0 <= n <= 10000 0 <= k <= 100 0 <= b <= 10000 Пример Если положить на депозит 1000 тенге на срок в 1 месяц со ставкой в 5%, то через месяц на счете будет 1050 тенге. Sample Input: 1 5 1000 Sample Output: 1050.0

##Решение:
# def calc_dep(n,k,b):
#     result = b
#     for i in range(1,n+1):
#         result += result * k / 100
#     print(result)

# n = int(input("Введите количество месяцев: "))
# k = float(input("Введите ставку по депозиту: "))
# b = float(input("Введите начальный баланс: "))
# calc_dep(n,k,b)
    
#Массивы ##Min
#Реализовать функцию min, которая возвращает минимальное число из массива. Если в массиве нет элементов, верните 0. Ограничения 0 <= array.length <= 10_000 Sample Input: [1, 2, 3] Sample Output: 1

##Решение:
# def min_list(list_a):
#     if len(list_a) == 0:
#         return 0
#     else:
#         tmp = list_a[0]
#         for i in range(1,len(list_a)):
#             if list_a[i] < tmp:
#                 tmp = list_a[i]
#         return tmp
# print(min_list([10,4,14]))


##range Реализовать функцию range, которая создает массив размером n, заполняет ячейки значениями от 1 до n и возвращает созданный массив. Пример int[] arr = range(5);
#for (int i = 0; i < arr.length; i++) {
#System.out.print(arr[i] + " "); } // Напечатает // 1 2 3 4 5 Ограничения 0 < n <= 10_000 Sample Input: 5 Sample Output: [1, 2, 3, 4, 5]

##Решение:
# def new_range(n):
#     arr = []
#     for i in range(1,n+1):
#         arr.append(i)
#     print(arr)
# n = int(input("Введите длину массива: "))
# new_range(n)


##sum Реализовать функцию sum, которая возвращает сумму чисел массива. Пример int array[] = {7, 5, 9, 1, 4}; int sum_number = sum(array);
#print(sum_number); // <-- выведет 26 Ограничения 0 <= array.length <= 10_000 Sample Input: [1, 2, 3] Sample Output: 6

##Решение:
#def sum_arr(arr):
#    result = 0
#    for i in range(0,len(arr)):
#        result += arr[i]
#    print(result)
#sum_arr([1, 2, 3])


##sort Реализовать функцию sort, которая принимает массив array(int[]). Функция должна отсортировать массив по возрастанию. Подсказка: https://habr.com/ru/post/204600/ Запрещено использовать Arrays.sort. Пример int array[] = {7, 5, 9, 1, 4}; sort(array);
#for (int i = 0; i < array.length; i++) {
#System.out.print(array[i] + " "); } // Напечатает // 1 4 5 7 9 Ограничения 0 <= array.length <= 10_000 Sample Input: [3, 2, 1] Sample Output: [1, 2, 3]

##Решение:
def sort_arr(arr):
    tmp = 0
    for j in range(1,len(arr)-1):
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
print(sort_arr([7, 5, 9, 1, 4]))
