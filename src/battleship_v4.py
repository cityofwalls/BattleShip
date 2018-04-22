__author__="Jesse"
__date__ ="$Dec 24, 2014 11:31:11 AM$"

from random import randrange

#globals
board = []
all_guesses = []
ship1 = []
ship2 = []
cur_guess = []
game_over = False


#call to print board. can be printed at any phase of turn.
def print_board(board):
    for row in board:
        print " ".join(row)
        

#call to prompt user for another game. a negative response will start a new turn before breaking
def play_again():
    global game_over
    print ""
    
    replay = raw_input("Would you like to play again? (y/n): ")
    
    while replay != "y" and replay != "n":
        replay = raw_input("Didn't catch that... y or n?: ")
        
    if replay == "y":
        init_game()
    
    else:
        print "Thanks for playing!"
        game_over = True
        

#call to determine end of turn. ship(s) are either sunk, the max num of turns is reached, or there are more turns
def cleanup(cur_guess, turn):
    global all_guesses
    
    all_guesses.append(cur_guess)
    
    if board[ship1[0][0]][ship1[0][1]] == "#" and board[ship1[1][0]][ship1[1][1]] == "#":
        print "You sunk my battleship!"
        print_board(board)
        
        play_again()
        
    elif turn >= 9:
        print "Game Over"
        print "It was here ===>"
        
        if board[ship1[0][0]][ship1[0][1]] != "#":
            board[ship1[0][0]][ship1[0][1]] = "B"
            
        if board[ship1[1][0]][ship1[1][1]] != "#":
            board[ship1[1][0]][ship1[1][1]] = "B"
            
        print_board(board)
        
        play_again()
        


#called if valid_input() passes but all other checks fail. designates a miss, alters board appropriately, called cleanup()
def miss_check(cur_guess, turn):
    global board
    
    print "MISS"
    print ""
    
    board[cur_guess[0]][cur_guess[1]] = "X"
    
    cleanup(cur_guess, turn)
    

#called if valid_input() is true and repeat_check() fails. checks guess against ship placement. alters board if neccessary.    
def hit_check(cur_guess, turn):
    global board
    if (cur_guess[0] == ship1[0][0]) and (cur_guess[1] == ship1[0][1]):
        print "HIT"
        print ""
        board[cur_guess[0]][cur_guess[1]] = "#"
        
        cleanup(cur_guess, turn)
        
    elif (cur_guess[0] == ship1[1][0]) and (cur_guess[1] == ship1[1][1]):
        print "HIT"
        print ""
        board[cur_guess[0]][cur_guess[1]] = "#"
        
        cleanup(cur_guess, turn)
        
    else:
        miss_check(cur_guess, turn)
        
        
#called when valid_input passes. tests cur_guess against all_guesses. if fail, call hit_check()  
def repeat_check(cur_guess, turn):
    if cur_guess in all_guesses:
        print "You've guesses that space already."
        print ""
        
        cleanup(cur_guess, turn)
        
    else:
        hit_check(cur_guess, turn)
        
        
#called to confirm cur_guess is within playing field
def valid_input(cur_guess, turn):
    if (cur_guess[0] < 0 or cur_guess[0] > len(board) - 1) or (cur_guess[1] < 0 or cur_guess[1] > len(board) - 1):
        print "Oops, that's not even in the ocean..."
        print ""
        
        cleanup(cur_guess, turn)
        
    else:
        repeat_check(cur_guess, turn)
        

#displays turn (1 - 10) and calls print_board(). prompts player for a row and column. calls valid_input()
def prompt(board, turn):
    global cur_guess
    row = 0
    col = 0
    
    print "Turn", turn + 1
    
    print_board(board)
    
    row = int(raw_input("Guess a row between 1 and 7: ")) - 1
    col = int(raw_input("Guess a column between 1 and 7: ")) - 1
    
    cur_guess = []
    cur_guess.append(row)
    cur_guess.append(col)
    
    valid_input(cur_guess, turn)
    
    
#
def init_game():
    global board, all_guesses
    global ship1, ship2
    
    #these are included to start a fresh game when play_again() is successful
    board = []
    all_guesses = []
    
    #create 7x7 board
    for x in range(7):
        board.append(["O"] * 7)
        
    ship1 = []
    ship2 = []
        
    #randomly place ship1 on board. coordinates will be formatted to 1-7 for player
    ship1.append([randrange(0, len(board)), randrange(0, len(board))])
    
    #"flip a coin" to determine if ship1 faces north/south or east/west
    orient_ship = randrange(0, 2)
    if orient_ship == 0:
        ship1.append([ship1[0][0] - 1, ship1[0][1]])
    else:
        ship1.append([ship1[0][0], ship1[0][1] - 1])
        
    if ship1[1][0] < 0:
        ship1[1][0] += 2
    elif ship1[1][1] < 0:
        ship1[1][1] += 2
        
    #####debug#####
    #print "ship 1 is at [", ship1[0][0] + 1, ship1[0][1] + 1, "and", ship1[1][0] + 1, ship1[1][1] + 1, "]"
    #####debug#####
    
    #run game
    for turn in range(10):
        if game_over:
            break
        else:
            prompt(board, turn)


#run program
init_game()