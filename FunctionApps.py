import random
def randomNumber():
    for i in range (3):
        random_value = random.randint(1,9)
        if random_value % 5 ==0:
            continue
        print("Random value is", random_value)

def even_odd(result):
    if result % 2 == 0 :
        return "Even"
    else: 
        return "odd"

def sumFunction():
    sum = 0
    for i in range (1,10):
        sum += i
    return sum 

sumValue = sumFunction()
print(sumValue)
even_odd(sumValue)