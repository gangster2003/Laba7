k = int(input("Введите границу: "))
m = int(input("Введите правую границу: "))
sum = 0
for i in range(k, m + 1):
     sum += pow(i,2)
print("Сумма квадратов = " + str(sum))