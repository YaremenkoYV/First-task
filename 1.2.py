n = int(input('Введіть число n:'))
N = int(input('Введіть число N:'))
sum_=0
factorial = 1
for i in range(2, n+1):
    factorial *= i
for y in range(N):
    y= ((3**n)*factorial)/(n**n)
    sum_+=y
print('Сума ряду дорівнює:',sum_)