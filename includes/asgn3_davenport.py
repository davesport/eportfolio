import sys

print("Assignment 3")
print(" ")
print("* * The Wizard Game * *")

playGame = input("Do you want to talk to the Wizard? (Yes or No) ")

def display_greeting ():
    print("\nThe Wizard will see you now. \n OK, let's get started.\n\n")

def process_question (counter, question):
    print(str(counter) + ".  What kind of question is " + question + "?")

if playGame == "yes" or playGame == "Yes" or playGame == "YES":
              
        display_greeting()
        
        name = input("What's your name? ")
            
        try: 
            numOfQuestions = (input("How many Questions do you want to ask the Wizard? "))
            int(numOfQuestions)

        except ValueError:
            print("\nError: " + str(numOfQuestions) + " is not a Valid Number!", file=sys.stderr)
            sys.exit("PROGRAM TERMINATED WITH ERROR")

        print("You want to ask the Wizard " + numOfQuestions + " questions")
   
        counter = 1
        while True:
            
            question = input("\nWhat's your question? ")

            if question == 'bye' or question == 'BYE' or question == 'Bye':
                break
            
            process_question(counter, question)

            counter = counter + 1

if playGame == "no" or playGame == "No" or playGame == "NO": 
        print("\nThe Wizard wants you to go away now!")

print("END OF PROGRAM")
