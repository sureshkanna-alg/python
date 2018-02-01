n = input("Enter your number:")
if type(n) == int:
    if n%2 == 0:
        print "Even"
    else:
        print "odd"
	
else:
    print "not a valid integer"
