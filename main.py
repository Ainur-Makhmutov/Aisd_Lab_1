#Числа Фибоначчи
a = b = 1
n = int(input()) # ввод номера числа Фибоначчи
print(a, b, end=' ')
for i in range(2, n):
   c = a + b
   a = b
   b = c
   print(b, end=' ')
