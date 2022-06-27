print("Welcome to Quiz Game 2022!")
name = input("Enter your name: ")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()
print("Let's start the quiz!")
score = 0

question = input("1. Is Python designed by Guido van Rossum? ")
if question == "yes":
    print("That's correct!")
    score += 1
else:
    print("Sorry,that's incorrect!")

question  = input("2. A variable is a named location used to store data in the memory. ")
if question  == "true":
    print("That's correct!")
    score += 1
else:
    print("Sorry,that's incorrect!")

question  = input("3. A constant is a type of variable whose value can be changed. ")
if question == "false":
    print("That's correct!")
    score += 1
else:
    print("Sorry,that's incorrect!")

question = input("4. Concatenation is when you have two or more strings \n and you want to join them into one. ")
if question  == "true":
    print("That's correct!")
    score += 1
else:
    print("Sorry,that's incorrect!")

question = input("5. Operators are used to perform operations on values and _______. ")
if question == "variables":
    print("That's correct!")
    score += 1
else:
    print("Sorry,that's incorrect!")

print(f"You got {score} questions correct!")
print(f"You got {score / 5 * 100} %!")