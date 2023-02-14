numbers = 0

def sum(numbers):
    for count in range(0,5):
        newNum = int(input("Enter your number"))
        if newNum >= 100:
            print("Numbers must be below 100, 1 added")
            numbers = numbers + 1 
        else:
            numbers = numbers + newNum 
    
    return numbers

numbers2 = sum(numbers)

print(numbers2)
