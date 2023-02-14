# Write a multiple choice quiz on a topic of your choosing.
#  There should be 5 questions and each question should have 3 possible answers.
#  Use if statements to tell the user if they were correct and to keep a running total of their score.
#  At the end of the quiz, display a suitable message to the user – either “You’re a genius”, “Not bad”, or “Must try harder” depending on the user’s score.

score = 0

name = str(input("Enter your name "))

print("This is Joe's Quiz about bread")
print("This quiz is multiple choice, when you have chose your answer please input the corresponding number")
while True:
    play = str(input("Do you want to play")).upper()

    if play == "YES":
        print("Question 1")
        print("What is the best type of bread")
        print("1. White bread")
        print("2. Brown bread")
        print("3. 50/50 Bread")

        answer1 = int(input("Enter your answer"))

        if answer1 == 1:
            print("Correct +1 score")
            score = score + 1
        else:
            print("You are wrong")
        
        print("Question 2")
        print("Where was bread first made")
        print("1. England")
        print("2. France")
        print("3. Jordan")

        answer2 = int(input("Enter your answer"))
        if answer2 == 3:
            print("Correct +1 score")
            score = score + 1
        else:
            print("You are wrong. Bread was first made in the Black Desert in Jordan in the stone ages")

        print("As of Decembert 2022. Due to inflation, how much has the price of bread risen")
        print("1. 3% ")
        print("2. 32% ")
        print("3. 28% ")

        answer3 = int(input("Enter your answer "))

        if answer3 == 3:
            print("Correct +1 score")
            score = score + 1
        else:
            print("You are wrong")

        print("As of 2021, which country was the biggest exporter of bread")
        print("1. Germany")
        print("2. France")
        print("3. England")

        answer4 = int(input("Enter your answer"))

        if answer4 == 1:
            print("Correct +1 score")
            score = score + 1
        else:
            print("You are incorrect, it was Germany, generating $4.6B")

        print("Final question.")
        print("")
        print("As of 2021, which country imports the most bread")
        print("1. England")
        print("2. France")
        print("3. USA")

        answer5 = int(input("Enter your answer"))

        if answer5 == 3:
            print("You are correct")
        
        else:
            print("You are incorrect, it was the USA spending $7.8B")
        
        if score == 5:
            print("Your a genius")

        elif score >= 3:
            print("Not bad")

        else:
            print("You must try harder")
        

    else:
        break
       
