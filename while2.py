#wap to create simple calculator
x = int(input("Enter the first value : "))
y = int(input("Enter the second value : "))
op = int(input("Enter an option :  \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 0.Exit \n"))
while op != 0:
    if op == 1:
        print (x+y)
        op = 0
    elif op == 2:
        print (x-y)
        op = 0
    elif op == 3:
        print (x*y)
        op = 0
    elif op == 4:
        print (x/y)
        op = 0
    else:
        print ("Invalid option")
        op = 0
