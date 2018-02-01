n = input("Enter your number: ")
if n==1:
    print "English"

elif n==2:
    print "Telugu"

elif n==3:
    print "Maths"
    
elif n==4:
    print "Social"
    
elif n==5:
    print "Science"

else:
    print "Enter Valid Number"



n = input("Enter Your Number: ")
if type(n) == int:
    if n%2 == 0:
        print "Even"
    else:
        print "Odd"

else:
    print " Not Valid Integer"
