def check_even_or_odd():
    for i in range (3):
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(f"{number} is Event")
        else:
            print(f"{number} is Odd")


def play_rock_paper_or_scissors():
    for i in range(3):
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = "rock"

        if player_choice == computer_choice:
            print("It's a tie!")

        elif (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "scissors" and computer_choice == "rock") or \
        (player_choice == "paper" and computer_choice == "scissors"):
            print("you win!")
    else: 
        print("You lose!")


def define_adult_or_minor():
    for i in range(3):
        age = int(input("Enter your age: "))
        if age >= 18:
            print("You are an adult.")
        else:
            print("You are a minor.")

# check_even_or_odd()
# play_rock_paper_or_scissors()
define_adult_or_minor()

