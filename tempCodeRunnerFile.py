def check_even_or_odd():
    for i in range (3):
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(f"{number} is Event")
        else:
            print(f"{number} is Odd")
check_even_or_odd()