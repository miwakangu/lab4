import random #importing random integers
def main():#because of multiple functions, we use main to call play()

    answer = input ("do you want to play a game? ")# asking user if he/she wants to play
    play(answer)


def play(answer): #defining play function

    if answer == "yes": #if our answer == the string 'yes' we proceed
        print("okay, let's play a game")
        number = random.randint(1, 100)
        guess = int(input("guess a number between 1 and 100: ")) #we ask the user to guess a number
        while guess != number: #when guess is not equal to our number .....
            if guess < number:#we initialize if statement, where if our guess is less than random number...
                print("your guess is too low") #we tell our user that it's too low
                guess = int(input("guess again: "))# we ask our user to try again
            else:
                print(guess) # if our guess is bigger than our number, we print it out
                exit()#we exit the while loop
        return guess # we return our guess variable so it can be executed by the play function


main()