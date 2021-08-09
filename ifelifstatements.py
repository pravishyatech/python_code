#wap to find the greatest of 3 numbers
x = int(input("Enter the first number : ")) #8
y = int(input("Enter the second number : ")) #8
z = int(input("Enter the third number : ")) #2
if (x>=y and x>=z):
    if (x==y):
        print("x and y are equal")
    elif(x==z):
        print("x and z are equal")
    print(x," is the greatest of 3 numbers")
elif (y>=z):
    if (y==z):
        print("y and z are equal")
    print(y," is the greatest of 3 numbers")
else:
    print(z," is the greatest of 3 numbers")