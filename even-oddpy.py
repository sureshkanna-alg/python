m = input("Enter values upto: ")
n = 1
even = []
odd = []
while n<=m:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)
    n = n+1
print ('Even Numbers are {0}'.format(even, odd))


print ('Odd Numbers are {1}'.format(even, odd))

