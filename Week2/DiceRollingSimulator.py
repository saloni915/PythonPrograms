import random

# displays the dice view after dice gets rolled
def display(no):
    if no==1:
        print("[-----]\n" 
            + "[     ]\n"
            + "[  0  ]\n"
            + "[     ]\n"
            + "[-----]\n"),

    elif no==2:
        print("[-----]\n" 
            + "[0    ]\n"
            + "[     ]\n"
            + "[    0]\n"
            + "[-----]\n"),

    elif no==3:
        print("[-----]\n"
            + "[0    ]\n"
            + "[  0  ]\n"
            + "[    0]\n"
            + "[-----]\n"),

    elif no==4:
        print("[-----]\n"
            + "[0   0]\n"
            + "[     ]\n"
            + "[0   0]\n"
            + "[-----]\n"),

    elif no==5:
        print("[-----]\n"
            + "[0   0]\n"
            + "[  0  ]\n"
            + "[0   0]\n"
            + "[-----]\n"),

    else:
        print("[-----]\n"
            + "[0   0]\n"
            + "[0   0]\n"
            + "[0   0]\n"
            + "[-----]\n")

# generates random number between 1 to 6 till user wants to roll the dice
def main():
    while True:
        choice=input("Enter Y/y to continue rolling the dice and N/n to stop:  ")
        if((choice=='Y') or (choice=='y')):
            number_on_dice=random.randint(1,6)
            display(number_on_dice)
            print("Number on dice is:  "+ str(number_on_dice))
        else:
            return 

if __name__=="__main__":
    main()
