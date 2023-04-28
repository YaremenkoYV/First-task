a = int(input('Введіть число яке хочете поділити: '))
b = int(input('Введіть число на яке хочете поділити: '))
sum_=a
for i in range(a):
    sum_=sum_-b

    print(sum_)
    if sum_<=b:
        print('Ділення завершено')
        break
