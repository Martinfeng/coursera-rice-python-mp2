# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math


# initialize global variables used in your code
high = 100
num = 0
lim = 0
count = 0


# helper function to start and restart the game
def new_game():
    global lim,num,count
    count = 0
    num = random.randrange(0, high)
    lim = math.ceil( math.log(high + 1, 2) )
    print 'New game. Range is from 0 to', high
    print 'Number of remaining guesses is', int(lim)
    print ''
    pass


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global high
    high = 100
    new_game()   
    pass

def range1000():
    # button that changes range to range [0,1000) and restarts
    global high
    high = 1000
    new_game()   
    pass
    
def input_guess(guess):
    # main game logic goes here
    global count
    guess = int(guess)
    count += 1
    print 'Guess was',guess
    print 'Number of remaining guesses is',int(lim) - count
    if int(lim) - count > 0 and guess < num:
        print 'Higher!'
        print ''
    elif int(lim) - count > 0 and guess > num:
        print 'Lower!'
        print ''
    elif int(lim) - count > 0 and guess == num:
        print 'Correct!'
        print ''
        new_game()
    elif int(lim) - count == 0 and guess != num:
        print 'You ran out of guesses. The number was',num
        print ''
        new_game()
    elif int(lim) - count == 0 and guess == num:
        print 'Correct!'
        print ''
        new_game()
    # remove this when you add your code
    pass

    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)


# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

    


# call new_game and start frame
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
