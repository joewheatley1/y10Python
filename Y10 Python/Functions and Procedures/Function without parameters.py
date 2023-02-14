def menu(): #Creates a function without parameters
    print("Menu option 1")
    print("Menu option 2")
    print("Menu option 3")

    selection = (input("Enter a menu choice?: ")) #Selection is put into variable

    if selection.isdigit() == True: #Error trap. Makes sure intiger is entered 
        return selection #Returns the variable selection to the menu variable
    
    else:
        print("Enter a number not letter")

choice = menu() #Runs the menu functions


if choice == 3:
    print ("Salad ordered")

elif choice == 2:
    print("Pasta ordered")

elif choice == 1:
    print("Chicken ordered")

else:
    print("Enter an option between 1-3")
