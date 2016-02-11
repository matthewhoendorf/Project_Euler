# The correct answer to Problem 2 is '4613732'

initList = []
sum = 0

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

def fibR(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

for number in range(1,50):
    if fibR(number) <= 4000000:
        initList.append(fibR(number))
    else:
        break

for number in initList:
    if number % 2 == 0:
        sum = sum + number

print "\nThe sum of the all Fibonacci numbers < 4 million = %d.\n" % sum
