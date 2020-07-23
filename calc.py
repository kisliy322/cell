print("Калькулятор v 0.1")
a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
print("1 Сложить ")
print("2 Вычесть ")
print("3 Умножить ")
print("4 Разделить ")
x = int(input("Что нужно сделать?\n"))
if x == 1:
	r = a + b;
	print("Ответ " + str(r))
elif x == 2:
	r = a - b;
	print("Ответ " + str(r))
elif x == 3:
	r = a * b;
	print("Ответ " + str(r))
elif x == 4:
	r = a / b;
	print("Ответ " + str(r))
else:
	print("Введите правильно! ")