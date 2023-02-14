#Function = returns something to the function call

#Procedure = does something and returns nothing
number1 = int(input("Enter a number ")) #Enter numbers to be put into function
number2 = int(input("Enter another number "))
number3 = int(input("Enter a final number "))

def largest(a,b,c): #Creates the function expecting 3 arguments(things) to be returned
    if a>b and a>c: #Which number is biggest
        return a #Returns argument
    elif b>a and b>c:
        return b
    else:
        return c
    

biggest = largest(number1, number2, number3) #takes numbers and arguments returned. Biggest is variable didgets are returned

print(biggest) 