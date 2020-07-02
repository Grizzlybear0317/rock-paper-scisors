import random

def play_game():

    user_input = input("Choose either rock(r), paper(p) or scissors(s): ")
    if not verify_input(user_input):
        print("Invalid input. Please enter either 'r' for rock, 'p' for paper, or 's' for scissors")
    cpu_input = get_cpu_input()
    if get_player_result(user_input, cpu_input) == "tie":
        print("It's a tie!")
    if get_player_result(user_input, cpu_input) == "win":
        print("Congrats! You won!")
    if get_player_result(user_input, cpu_input) == "lose":
        print("Sorry. You lost.")

def get_cpu_input():
    cpu_input = random.randint(1, 3)
    if cpu_input == 1:
        cpu_input = "r"
    elif cpu_input == 2:
        cpu_input = "p"
    else:
        cpu_input = "s"
    return cpu_input

def verify_input(input):
    if input in ["r", "p", "s"]:
        return True
    return False

def get_player_result(player_input, cpu_input):
    if player_input == cpu_input:
        return "tie"
    if player_input == "r" and cpu_input == "s":
        return "win"
    if player_input == "p" and cpu_input == "r":
        return "win"
    if player_input == "s" and cpu_input == "p":
        return "win"
    return "lose"



while True:
    play_game()
    print("")
    user_choice = play_game()
    comp_choice = get_cpu_input()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You tied")

        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You lose.")

        elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You win.")

        elif user_choice == "p":
            if comp_choice == "r":
                print("You chose paper. The computer chose rock. You win.")

        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. You tied.")

        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You lose.")

        elif user_choice == "s":
            if comp_choice == "r":
                print("You chose scissors. The computer chose rock. You lose.")

        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")

        elif comp_choice == "s":
            print("You chose scissors. The computer chose scissors. You tied.")

        print("")
        print("Player wins")
        print("Computer wins")
        print("")

        user_choice = input("Do you want to play again? (y/n)")
        if user_choice in ["Y", "y", "yes", "Yes"]:
            pass
        elif user_choice in ["N", "n", "no", "No"]:
            break
        else:
            break