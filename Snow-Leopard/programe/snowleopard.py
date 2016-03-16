#This software is licensed under the GNU GPL v3.0.
#This is the current version of CalcWizard for Linux.

# -*- coding:iso-8859-1 -*-

print("CalcWizard Snow Leopard by Alex Vegas")

       
a = raw_input("Type 'Calculate!' to start the calculator, type 'Convert!' to start the temperature-converter, type 'Conjure!' to start the velocity-wizard!"
              "Type 'Multiply!' to start the multiplication-wizard! Type 'end' to stop the wizards after they have completed an operation! Type 'about' to find out more about the programe! ")

if a == "Calculate!":
    b = raw_input("Type a number! ")
    c = raw_input("Type a number! ")
    d = raw_input("Which operation would you like to do? Type 'a' for addition, type 's' for subtraction, type 'm' for multiplication and 'd' for division! ")
    if d == "a":
        print(float(b)+float(c))
    elif d == "s":
        print (float(b)-float(c))
    elif d == "m":
        print (float(b)*float(c))
    elif d == "d":
        print (float(b)/float(c))
    else:
        print ("invalid input ")

elif a == "Convert!":
    e = raw_input("Do you want to convert celsius into fahrenheit or the fahrenheit into celsius? Type 'c4tw' if you want to convert celsius into fahrenheit and 'f4tw' if you want to convert fahrenheit into celsius! ")
    if e == "c4tw":
        f = raw_input("Type your Fahrenheit value here! ")
        print (float(float(5)/float(9)) * float(float(f) - 32))
    elif e == "f4tw":
        g = raw_input("Type your celsius value here! ")
        print (float(float(g)/float(float(5)/float(9))) + float(32))
    else:
        print ("invalid input")

elif a == "Conjure!":
    h = raw_input("Type 'v' if you want to calculate the velocity, type 'd' if you want to calculate the distance a body has travelled and type 't' if you want to calculate the time! ")
    if h == "v":
        i = raw_input("Type the distance here! ")
        j = raw_input("Type the time taken here! ")
        print (float(i)/float(j))
    elif h == "d":
        k = raw_input("Type the velocity of the body here! ")
        l = raw_input("Type the time taken here! ")
        print (float(k) * float(l))
    elif h == "t":
        m = raw_input("Type the distancevalue here! ")
        n = raw_input("Type the velocityvalue here! ")
        print (float(m)/float(n))
    else:
        print ("invalid input")

elif a == "Multiply!":
   o = raw_input("Type a number! ")
   q = raw_input("Type the range! ")
   w = 1 + int(q)
   j = 0
   for j in range(1,int(w)):
        print (str(float(o)) + (" x ") + str(float(j)) + (" = ") + str(float(o)*float(j)))
		
elif a == "about":
    print("Developed by Alex Vegas. License: GNU GPL 2015 Apache v2.0. Source and further information: github.com/officialalexvegas/CalcWizard ")
   
else:
    print ("invalid input")

while a == "Calculate!" or a == "Convert!" or a == "Conjure!" or a == "Multiply!":
    a = raw_input("Type 'Calculate!' to start the calculator, type 'Convert!' to start the temperature-converter, type 'Conjure!' to start the velocity-wizard!"
              "Type 'Multiply!' to start the multiplication-wizard! Type 'end' to stop the wizards after they have completed an operation! Type 'about' to find out more about the programe! ")
    
    if a == "Calculate!":
        b = raw_input("Type a number! ")
        c = raw_input("Type a number! ")
        d = raw_input("Which operation would you like to do? Type 'a' for addition, type 's' for subtraction, type 'm' for multiplication and 'd' for division! ")
        if d == "a":
            print (float(b)+float(c))
        elif d == "s":
            print (float(b)-float(c))
        elif d == "m":
            print (float(b)*float(c))
        elif d == "d":
            print (float(b)/float(c))
        else:
            print ("invalid input ")

    elif a == "Convert!":
        e = raw_input("Do you want to convert celsius into fahrenheit or the fahrenheit into celsius? Type 'c4tw' if you want to convert celsius into fahrenheit and 'f4tw' if you want to convert fahrenheit into celsius! ")
        if e == "c4tw":
            f = raw_input("Type your Fahrenheit value here! ")
            print (float(float(5)/float(9)) * float(float(f) - 32))
        elif e == "f4tw":
            g = raw_input("Type your celsius value here! ")
            print (float(float(g)/float(float(5)/float(9))) + float(32))
        else:
            print ("invalid input")

    elif a == "Conjure!":
       h = raw_input("Type 'v' if you want to calculate the velocity, type 'd' if you want to calculate the distance a body has travelled and type 't' if you want to calculate the time! ")
       if h == "v":
           i = raw_input("Type the distance here! ")
           j = raw_input("Type the time taken here! ")
           print (float(i)/float(j))
       elif h == "d":
           k = raw_input("Type the velocity of the body here! ")
           l = raw_input("Type the time taken here! ")
           print (float(k) * float(l))
       elif h == "t":
           m = raw_input("Type the distancevalue here! ")
           n = raw_input("Type the velocityvalue here! ")
           print (float(m)/float(n))
       else:
           print ("invalid input")
   
    elif a == "Multiply!":
        o = raw_input("Type a number! ")
        q = raw_input("Type the range! ")
        w = 1 + int(q)
        j = 0
        for j in range(1,int(w)):
            print (str(float(o)) + (" x ") + str(float(j)) + (" = ") + str(float(o)*float(j)))
    elif a == "about":
        print ("Developed by Alex Vegas. License: GNU GPL 2015 Apache v2.0. Source and further information: github.com/officialalexvegas/CalcWizard ")

print ("Thank you for using CalcWizard!")
