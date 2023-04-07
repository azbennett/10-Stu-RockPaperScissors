def main(): 
    import random
    import os

    os.system('cls')  #cleans things up so its nice and tidy

    print()
    print("-------------------------------")
    print("Let's Play Rock Paper Scissors!")
    print("-------------------------------")
    print()

    #The NPC makes its choice
    options = ["r", "p", "s"]
    computer_choice = random.choice(options)

    #The human picks their response
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

    rock = "Rock"
    paper = "Paper"
    scissor = "Scissor"

    #Now it is time to clean up the responses for both the PC and NPC
    if user_choice == "r": answer = rock
    elif user_choice == "p": answer = paper
    elif user_choice == "s": answer = scissor
    else:
        print()
        print("Uh-oh, looks like you did not answer correctly.  Lets try this again.")
        input("Press any key to continue...")
        main()

    if computer_choice == "r": c_answer = rock
    elif computer_choice == "p": c_answer = paper
    else: c_answer = scissor

    #compare NPC VS PC
    if (computer_choice == user_choice):         #checks for a tie
        print()
        print(f"You picked the same thing as the computer! {answer} vs {c_answer} was a tie.")
    elif (computer_choice == "r") and (user_choice == "p"):   
        print()
        print(f"Your {answer} beat {c_answer}!")  #paper beats rock        
    elif (computer_choice == "p") and (user_choice == "s"): 
        print()
        print(f"Your {answer} beat {c_answer}!")  #scissors beats paper
    elif (computer_choice == "s") and (user_choice == "r"): 
        print()
        print(f"Your {answer} beat {c_answer}!")  #rock beats scissors
    else:                                                       #everything else loses
        print()
        print(f"Ohh, better luck next time.  Your {answer} was defeated by the {c_answer}.")
    
    print()
    restart = input("Would you like to go again? (y/n)")    #play again?
    if restart == "y":                                      #if so it starts again
        main()
    else:  
        print()                                                 #if not it exits
        print("Thanks for playing!")
        exit()

#technically this is where the code begins
main()
# https://www.youtube.com/watch?v=SZdQX4gbql0 - using procedures
# https://www.geeksforgeeks.org/clear-screen-python/ - using import OS to clear screen 'cls'
