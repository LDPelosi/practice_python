num = int(input('Enter the len of Fibonacci numbers => '))
count = 1
count2 = 1

for i in range(num):
    aux = count + count2
    print(count)
    count, count2 = count2, aux
    