k = int(input("Введите левую границу: "))
m = int(input("Введите границу: "))
sum = 0
for i in range(k, m + 1):
     sum += pow(i,2)
print("Сумма квадратов = " + str(sum))