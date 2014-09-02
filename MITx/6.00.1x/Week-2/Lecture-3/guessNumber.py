"""Lecture 3 | Problem 9: guess a number between 0 and 100 with the bisection method"""

__author__ = 'Nicola Moretto'
__license__ = "GPLv2"

print "Please think of a number between 0 and 100!"
low = 0
high = 100
answer = 50
guess = False
while guess == False:
    print "Is your secret number " + str(answer) + "?"
    user_answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    while(user_answer != 'h' and user_answer != 'l' and user_answer != 'c'):
        print "Sorry, I did not understand your input."
        print "Is your secret number " + str(answer) + "?"
        user_answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_answer == 'h':
        high = answer
        answer = (low+high)/2
    elif user_answer == 'l':
        low = answer
        answer = (low+high)/2
    else: # user_answer == 'c'
        guess = True
print "Game over. Your secret number was: " + str(answer)