#WAP to find the area of shapes
def menu():
    op = int(input("Menu :  \n 1.Triangle \n 2.Rectangle \n 3.Square \n 0.Exit \nEnter an option : "))

    if op == 1:
        b = int(input("Enter the base width : "))
        h = int(input("Enter the height : "))
        area = 0.5 * (b*h)
        print("The are of the given triangle is ",area)
        menu()
    elif op == 2:
        b = int(input("Enter the breadth : "))
        l = int(input("Enter the length : "))
        area = l*b
        print("The are of the given rectangle is ",area)
        menu()
    elif op == 3:
        l = int(input("Enter the length : "))
        area = l*l
        print("The are of the given square is ",area)
        menu()
    elif op == 0:
        exit()
    else:
        print ("Invalid option")
        menu()

menu()