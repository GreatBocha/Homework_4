# 2'. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]

num = int(input("Введите число: "))
i = 2 
lst = []
numb_n = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
lst = list(set(lst))  
lst.sort()      
print(f"Простые множители числа {numb_n} приведены в списке: {lst}")