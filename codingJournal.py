import PreviousJournal
import Newjournal
import questions

def output(choice1, choice2, choice3, choice4, choice5, choice6):
    print(choice6 +"\n")
    print(f"Today's Results: {choice1}\n")
    print(f"Errors:  {choice2}\n")
    print(f"Collaborators: {choice3}\n")
    print(f"TODO: {choice4}\n")
    print(f"Commets: {choice5}\n")

def main():
    print("Welcome to your coding journal")

    while True:
        choice = int(input("Would you like to access a previous journal (press 1) or create a new journal (press 2)? "))
        
        if choice == 1:
            while True:
                name = input("What was the name of your journal?: ")
                if not PreviousJournal.checkname(name):
                    print("No such journal exists. Please try again.")
                else:
                    print("Successfully accessed the journal:", name)
                    break
            break
        
        elif choice == 2:
            while True:
                name = input("What do you want to name your journal? ")
                if not Newjournal.createJournal(name):
                    print("A journal with this name already exists. Please try again.")
                else:
                    print(f"The journal with the name '{name}' has been created.")
                    break
            break

    while True:
        pick = int(input("What would you like to do? [1] Make entries, [2] Make changes, [3] Find entry, [4] Quit: ")) 

        if pick == 1:
            choice1, choice2, choice3, choice4, choice5, choice6 = questions.entries()
            Newjournal.InsertData(choice1, choice2, choice3, choice4, choice5, choice6, name)
            output(choice1, choice2, choice3, choice4, choice5, choice6)
            print("Successfully written into journal.")
        elif pick == 2:
            date = input("What was the date of the entry you wish to eidt? (xxxx-xx-xx) ")
            PreviousJournal.modify(date,name)   
        elif pick == 3:
            date = input("What was the date of the entry you wish to see? (xxxx-xx-xx) ")
            PreviousJournal.extract(date, name)
        elif pick == 4:
            print("Hope you write again!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
