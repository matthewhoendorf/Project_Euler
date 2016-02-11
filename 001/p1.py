print "\nThis program will output the sum of the multiples of 3 or 5 between the range of 0 to n."

limit = input('\nPlease enter the desired value of n: ')
initList = list(range(0,limit))
sum = 0

for number in initList:
    if initList[number] % 3 == 0:
        sum = sum + number
    elif initList[number] % 5 == 0:
        sum = sum + number

print "\nThe sum of the multiple of 3 or 5 from 0 to %i is %i." % (limit,sum)
