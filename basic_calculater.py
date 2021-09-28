# Create a basic calculater...

# add Two Number
def add(x,y):
    return x+y

# Subtract two Number
def subtract(x,y):
    return x-y

# multiply two Number
def multiply(x,y):
    return x*y

# Divide two Number
def divide(x,y):
    return x/y

# Select operations Number
print("Select operations.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Select choice Number
while True:
    choice = input("Enter Your Choice(1/2/3/4):")
    if choice in ('1','2','3','4'):
        number1 = float(input("Enter First Number: "))
        number2 = float(input("Enter Second Number: "))
        if choice == '1':
            print(number1, "+" ,number2 ,"=", add(number1,number2))
        elif choice == '2':
            print(number1,"-",number2,"=",subtract(number1,number2))
        elif choice == '3':
            print(number1,"*",number2,"=",multiply(number1,number2))
        elif choice == '4':
            print(number1,"/",number2,"=",divide(number1,number2))
        break
    else:
        print("Enterd Input is invalid.")