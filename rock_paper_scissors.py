def main(): 
    import random
    import os
    import time

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
    correct_choices = ["r", "rock", "p", "paper", "s", "scissor", "scissors"]
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ").lower()
    
    #Now it is time to clean up the responses for both the PC and NPC
    if user_choice in correct_choices:
        if (user_choice == "r") or (user_choice == "rock"): answer = "Rock"
        elif (user_choice == "p") or (user_choice == "paper"): answer = "Paper"
        elif (user_choice == "s") or (user_choice == "scissor") or (user_choice == "scissors"): answer = "Scissors"
    else:
        time.sleep(.5)
        print()
        print("Uh-oh, looks like you did not answer correctly.  Lets try this again.")
        input("Press any key to continue...")
        main()

    if computer_choice == "r": c_answer = "Rock"
    elif computer_choice == "p": c_answer = "Paper"
    else: c_answer = "Scissors"

    #compare NPC VS PC
    if (computer_choice == user_choice[0]):         #checks for a tie
        time.sleep(.5)
        print()
        print(f"You picked the same thing as the computer! {answer} vs {c_answer} was a tie.")
    elif (computer_choice == "r") and ((user_choice == "p") or (user_choice == "paper")):   
        time.sleep(.5)
        print()
        print(f"Your {answer} beat {c_answer}!")  #paper beats rock        
    elif (computer_choice == "p") and ((user_choice == "s") or (user_choice == "scissor") or (user_choice == "scissors")): 
        time.sleep(.5)
        print()
        print(f"Your {answer} beat {c_answer}!")  #scissors beats paper
    elif (computer_choice == "s") and ((user_choice == "r") or (user_choice == "rock")): 
        time.sleep(.5)
        print()
        print(f"Your {answer} beat {c_answer}!")  #rock beats scissors
    else:                                                       #everything else loses
        time.sleep(.5)
        print()
        print(f"Ohh, better luck next time.  Your {answer} was defeated by the {c_answer}.")
    
    time.sleep(.5)
    print()
    restart = input("Would you like to go again? (y/n)")    #play again?
    if restart == "y":                                      #if so it starts again
        main()
    else:  
        time.sleep(.5)
        print()                                             #if not it exits
        print("Thanks for playing!")
        exit()

#technically this is where the code begins
main()
# https://www.youtube.com/watch?v=SZdQX4gbql0 - using procedures
# https://www.geeksforgeeks.org/clear-screen-python/ - using import OS to clear screen 'cls'
