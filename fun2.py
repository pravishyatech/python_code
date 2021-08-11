#wap to create a calculator using functions

def get_value():
    x = int(input("Enter the first value : "))
    y = int(input("Enter the second value : "))
    return (x, y)

def add():
    x,y = get_value()
    print(x+y)

def subtract():
    x,y = get_value()
    print(x-y)

def multiply():
    x,y = get_value()
    print(x*y)

def divide():
    x,y = get_value()
    print(x/y)


def menu():
    op = int(input("Menu :  \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 0.Exit \nEnter an option : "))

    if op == 1:
        add()
        menu()
    elif op == 2:
        subtract()
        menu()
    elif op == 3:
        multiply()
        menu()
    elif op == 4:
        divide()
        menu()
    elif op == 0:
        exit()
    else:
        print ("Invalid option")

menu()