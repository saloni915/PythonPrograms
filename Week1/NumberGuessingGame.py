import random

def main():
    actual_number=random.randint(1,100)     #generates a random number from 1 to 100
    attempts=0
    max_score=100

    while True:
        attempts += 1
        guess=int(input("Guess the number between 1 to 100:\n"))
        if guess>actual_number:
            print("Clue: Guessed number is greater than actual number")
        if guess<actual_number:
            print("Clue: Guessed number is smaller than actual number")
        if actual_number%guess ==0:
            print("Clue: Guessed number is divisible by actual number")
        if guess==actual_number: 
            print("You guessed correctly in "+ str(attempts) +" attempts.")
            print("Your score is ",max_score)
            return
        max_score -= 1
        

if __name__ == "__main__":
    main()
