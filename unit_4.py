#written by oliver hamburger
#program takes a maximum number and an opperation, then takes
#two random numbers smaller than the maximun munber and does
#the opperation by the two random numbers.
import random

def get_max_number():
    '''takes a maximum number from the user and returns that number'''
    max_number = float(input("what is the maximum number you would like?: "))
    return max_number

def get_type_of_problem():
    '''takes an opperation from the user and returns the opperation'''
    opperation = input("what type of problem would you like?, (+, -, or *): ")
    return opperation

def calculate_random(maximum):
    '''calculates two random numbers to do the opperation by'''
    random_number_1 = random.randrange(0, maximum)
    random_number_2 = random.randrange(0, maximum)
    return random_number_2,random_number_1

def calculate(random_number_1, opperation, random_number_2):
    '''takes the given opperation and applies it to the two random numbers'''
    if opperation == "*":
        return random_number_1 * random_number_2
    elif opperation == "-":
        return random_number_1 - random_number_2
    else:
        return random_number_1 + random_number_2

def answer(random_number_1, opperation, random_number_2):
    '''asks user for answer of problem and prints the correct answer if the users input is wrong'''
    prompt = "what is " + str(random_number_1) + opperation + str(random_number_2)
    guess = float(input(prompt))
    if guess == calculate(random_number_1, opperation, random_number_2):
        print("you are correct! great job")
        print("thanks for playing")
    else:
        print("sorry, the answer is not correct.")
        print("the answer was: " + str(calculate(random_number_1, opperation, random_number_2)))
        print("thanks for playing")


#function that runs all other functions in order
def main():
    max_number = get_max_number()
    opperation = get_type_of_problem()
    r1, r2 = calculate_random(max_number)
    answer(r1, opperation, r2)

#calls the function that runs all the other functions
main()



