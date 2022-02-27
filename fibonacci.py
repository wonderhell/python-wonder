#Fibonacci Sequence


lim = int(input('Enter limit of sequence: '))

a = 0
b = 1


for i in range(lim):
    print(a)
    
    c = a+b 
    a = b
    b = c