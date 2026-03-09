import ascii
from ascii import logo
print(logo)
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    if n2 == 0:
        return "Error: Division by zero is not possible!"
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide

}
result= 0

calculating = True
while calculating:

    if result== 0:
        user_input1= int(input("Enter the first number:\n"))
    else:
        user_input1= result


    user_operation =input("+\n-\n*\n/\nPick an operation:\n")

    user_input2= int(input("Enter the second number:\n"))


    for key in operations:
        if key == user_operation:
            sub_result = operations[key](user_input1,user_input2)

    print(sub_result)
    invalid = True
    while invalid:

        again= input(f'Do you want to continue opeation with {sub_result} If yes press "y" or "n" for new calculation:\n').lower()
        if again == "n":
            result =0
            invalid = False
        elif again =="y":
            result= sub_result
            invalid = False
        else:
            print("Invalid input,'Please type again'")
