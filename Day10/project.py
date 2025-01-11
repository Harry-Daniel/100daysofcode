from art import art

def add(n1,n2):
    return n1 +n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

keep_calculating=True
while keep_calculating == True:

    print(art)

    first_number=float(input("Type in the first number:\n"))

    keep_calculating_with_result=True

    result=first_number

    while keep_calculating_with_result== True:

        operator=input("Type in the operation , you'd like to carry out: +, -, * or /\n")
        
        second_number=float(input("Type in the second number:\n"))

    
        result=operations[operator](result,second_number)

        print(f"The result is : {result}")
        
        calc_with_result=input("Do you want to calculate again with the RESULT? Type y to calculate with result or n to start a new calculation. Or  Type stop to exit\n").lower()
        if calc_with_result=='n':
            keep_calculating_with_result=False
            print("\n"*200)
        elif calc_with_result=='y':
            keep_calculating_with_result=True
        elif calc_with_result=='stop':
            keep_calculating_with_result=False
            keep_calculating=False
            print("Have a nice day")
        else:
            print("Wrong input, project terminating... Have a good day.")
            keep_calculating_with_result=False

    



