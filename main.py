from Objects import Game

#These are variables for 
turn_counter = 0
flag = 1

#We get the names of the players to display onto the screen
player1 = input("What is the name of the first player? ")
player2 = input("What is the name of the second player? ")

#simple boolean variable used for loops 
symbol_flag = True

#loop to get exactly one characyer for the players symbol
while symbol_flag:
    symbol1 = input("Player 1 what is the symbol for your tic tac toe? (Must be one character) ")
    if len(symbol1) == 1:
        symbol_flag = False
    else:
        print("Your symbol was not 1 character")

#same loop is the one above just for the second character 
symbol_flag = True
while symbol_flag:
    symbol2 = input("Player 2 what is the symbol for your tic tac toe? (Must be one character) ")
    if len(symbol2) == 1:
        symbol_flag = False
    else:
        print("Your symbol was not 1 character")
    

#initializes game and starts it 
game1 = Game(player1, player2, False, "", 0, 0)
game1.start_game()

#flag is to stop the loop and stop the game from starting up again
while flag != 0:
    #player 1 starts his turn
    print( player1 + " it is your turn! ")
    game1.player_turn(symbol1, symbol2)
    turn_counter += 1
    
    #checks if the player1 won the game
    if not game1.check_game(symbol1):
        #checks if the game is a tie
        if turn_counter >= 9:
            print("The game is a tie!")
            #
            while True:
                try:
                    flag = int(input("Type 1 if you want to play again and 0 if you are done playing. "))
                    break
                except ValueError:
                    print("Input was not an integer")
            if flag == 1:
                turn_counter = 0
                game1.start_game()
        else : 
            print(player2 + " it is your turn! ")
            game1.player_turn(symbol2, symbol1)
            turn_counter += 1
            if game1.check_game(symbol2):
                print(player2 + " wins!")
                game1.add_player_score(player2)
                while True:
                    try:
                        flag = int(input("Type 1 if you want to play again and 0 if you are done playing. "))
                        break
                    except ValueError:
                        print("Input was not an integer")
                if flag == 1:
                    turn_counter = 0
                    game1.start_game()
    else:
        print(player1 + " wins!")
        game1.add_player_score(player1)
        while True:
            try:
                flag = int(input("Type 1 if you want to play again and 0 if you are done playing. "))
                break
            except ValueError:
                print("Input was not an integer")
        if flag == 1:
            turn_counter = 0
            game1.start_game()
       
        
print("Game end")