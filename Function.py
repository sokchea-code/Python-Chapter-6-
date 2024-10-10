import random
def guess_app():
    while True: 
        number = random.randint(1, 100)
        print ("Guess a magic number between 0 and 100")

        for attempt in range (1, 6):

            guess = eval (input(f"Attempt {attempt} enter your quessed number: " ))

            if guess == number : 
                print("You've got it right! Great job!", number)
            elif guess > number : 
                print("It is too high! Try again. ")
            else: 
                print("It is too low! Try again. ")

        play_again = input("Do you want to play again? (Yes/No): ").lower()
        if play_again != 'yes': 
            print("Goodbye!")
            break 

guess_app()