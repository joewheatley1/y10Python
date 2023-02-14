# Write a program that will ask for a favourite genre (type) of music, and then make a recommendation. 
# For example, if they like rock then they should list to the Kaiser Chiefs, or if they like R&B they should listen to Rihanna. 

genre = str(input("Enter your favourite genre ")).upper()

if genre == "ROCK":
    print("Your suggested artist is the Kaiser Cheifs")

elif genre == "POP":
    print("Your suggested artist is Justn Bieber")

elif genre == "RAP":
    print("Your suggested artist is Eminem")

elif genre == "R&B"or genre == "R AND B":
    print("Your suggested artist is Rihanna")

elif genre == "COUNTRY":
    print("Your suggested artist is Miley Cyrus")

elif genre == "DRILL":
    print("Your suggested artist is Central Cee")

else:
    print("I do not have a suggested artist")

