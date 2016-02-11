# The correct solution for Problem 4 is '906609'

import math

multiplier = input("\nEnter the number of digits for the two multipliers: ")
pList = []

def isPalindrome(number):
    numString = str(number)
    numLength = len(numString)
    temp = (numLength-1)
    for i in range(0,int(math.floor(numLength/2))):
        if numString[i] != numString[temp]:
            return False
        else:
            temp = temp - 1
    return True

if multiplier < 2:
    print "\nThe number of digits is too damn low!"
    print ""
else:
    if multiplier > 3:
        print "\nIt is not recommended to enter a value greater than 3."
        print "Use the keyboard interrupt (Ctrl-C) if you aren't patient."
    print "Calculating..."
    for i in range(10**(multiplier-1),(10**multiplier)):
        for j in range(10**(multiplier-1),(10**multiplier)):
            if isPalindrome(i*j) == True:
                pList.append(i*j)
    print "\nThe largest palindromic number: %i" % max(pList)
    print ""
