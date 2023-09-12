class Game:
    def __init__(self, player1, player2, end, game_string, player1_score, player2_score):
        self.player1 = player1
        self.player2 = player2
        self.end = False
        self.player1_score = 0
        self.player2_score = 0
        self.game_string = "   A1   A2   A3\n A1    |    |    \n     ----------- \n B1    |    |    \n     ----------- \n C1    |    |    "

    def start_game(self):
        print("The Game is starting")
        print(self.player1 + "\t\t" + self.player2)
        print(str(self.player1_score) + "\t\t" + str(self.player2_score))
        self.game_string = "   A1   A2   A3\n A1    |    |    \n     ----------- \n B1    |    |    \n     ----------- \n C1    |    |    "
        print(self.game_string)
        
        
    def add_player_score(self, player):
        if(player == self.player1):
            self.player1_score += 1
        if(player == self.player2):
            self.player2_score += 1
    
    def check_game(self, symbol):
        if self.game_string[21] == symbol and self.game_string[26] == symbol and self.game_string[30] == symbol:
            self.end = True
            return self.end
            
            
        if self.game_string[57] == symbol and self.game_string[62] == symbol and self.game_string[66] == symbol:
            self.end = True
            return self.end
            
            
        if self.game_string[93] == symbol and self.game_string[98] == symbol and self.game_string[102] == symbol:
            self.end = True
            return self.end
            
            
        if self.game_string[21] == symbol and self.game_string[57] == symbol and self.game_string[93] == symbol:
            self.end = True
            return self.end
            
            
        if self.game_string[26] == symbol and self.game_string[62] == symbol and self.game_string[98] == symbol:
            self.end = True
            return self.end
            
            
        if self.game_string[30] == symbol and self.game_string[66] == symbol and self.game_string[102] == symbol:
            self.end = True
            return self.end
            
        if self.game_string[21] == symbol and self.game_string[62] == symbol and self.game_string[102] == symbol:
            self.end = True
            return self.end
            
        if self.game_string[30] == symbol and self.game_string[62] == symbol and self.game_string[93] == symbol:
            self.end = True
            return self.end
        
            
        
            
    def player_turn(self, symbol, enemy_symbol):
        move = input("Where do you want to move? ")
        
        
        if move ==  "A1" or move == "a1":
            if self.game_string[21] == symbol or self.game_string[21] == enemy_symbol:
                print("That spot has already been used. Pick another spot?")
                self.player_turn(symbol, enemy_symbol)
            else:
                self.game_string = self.game_string[:21] + symbol + self.game_string[22:]
                print(self.player1 + "\t\t" + self.player2)
                print(str(self.player1_score) + "\t\t" + str(self.player2_score))
                print(self.game_string)
        
        
        elif move ==  "A2" or move == "a2":
            if self.game_string[26] == symbol or self.game_string[26] == enemy_symbol:
                print("That spot has already been used. Pick another spot?")
                self.player_turn(symbol, enemy_symbol)
            else:
                self.game_string = self.game_string[:26] + symbol + self.game_string[27:]
                print("The Game is starting")
                print(self.player1 + "\t\t" + self.player2)
                print(str(self.player1_score) + "\t\t" + str(self.player2_score))
                print(self.game_string)
       
        
        elif move ==  "A3" or move == "a3":
            if self.game_string[30] == symbol or self.game_string[30] == enemy_symbol:
                print("That spot has already been used. Pick another spot?")
                self.player_turn(symbol, enemy_symbol)
            else:
                self.game_string = self.game_string[:30] + symbol + self.game_string[31:]
                print(self.player1 + "\t\t" + self.player2)
                print(str(self.player1_score) + "\t\t" + str(self.player2_score))
                print(self.game_string)
        
        
        elif move ==  "B1" or move == "b1":
            if self.game_string[57] == symbol or self.game_string[57] == enemy_symbol:
                print("That spot has already been used. Pick another spot?")
                self.player_turn(symbol, enemy_symbol)
            else:
                self.game_string = self.game_string[:57] + symbol + self.game_string[58:]
                print(self.player1 + "\t\t" + self.player2)
                print(str(self.player1_score) + "\t\t" + str(self.player2_score))
                print(self.game_string)
        
        
        elif move ==  "B2" or move == "b2":
            if self.game_string[62] == symbol or self.game_string[62] == enemy_symbol:
                print("That spot has already been used. Pick another spot?")
                self.player_turn(symbol, enemy_symbol)
            else:
                self.game_string = self.game_string[:62] + symbol + self.game_string[63:]
                print(self.player1 + "\t\t" + self.player2)
                print(str(self.player1_score) + "\t\t" + str(self.player2_score))
                print(self.game_string)
       
       
        elif move ==  "B3" or move == "b3":
            if self.game_string[66] == symbol or self.game_string[66] == enemy_symbol:
                print("That spot has already been used. Pick another spot?")
                self.player_turn(symbol, enemy_symbol)
            else:
                self.game_string = self.game_string[:66] + symbol + self.game_string[67:]
                print(self.player1 + "\t\t" + self.player2)
                print(str(self.player1_score) + "\t\t" + str(self.player2_score))
                print(self.game_string)
        
        
        elif move ==  "C1" or move == "c1":
            if self.game_string[93] == symbol or self.game_string[93] == enemy_symbol:
                print("That spot has already been used. Pick another spot?")
                self.player_turn(symbol, enemy_symbol)
            else:
                self.game_string = self.game_string[:93] + symbol + self.game_string[94 :]
                print(self.player1 + "\t\t" + self.player2)
                print(str(self.player1_score) + "\t\t" + str(self.player2_score))
                print(self.game_string)
                
                
        elif move ==  "C2" or move == "c2":
            if self.game_string[98] == symbol or self.game_string[99] == enemy_symbol:
                print("That spot has already been used. Pick another spot?")
                self.player_turn(symbol, enemy_symbol)
            else:
                self.game_string = self.game_string[:98] + symbol + self.game_string[99:]
                print(self.player1 + "\t\t" + self.player2)
                print(str(self.player1_score) + "\t\t" + str(self.player2_score))
                print(self.game_string)
                
            
        elif move ==  "C3" or move == "c3":
            if self.game_string[102] == symbol or self.game_string[102] == enemy_symbol:
                print("That spot has already been used. Pick another spot?")
                self.player_turn(symbol, enemy_symbol)
            else:
                self.game_string = self.game_string[:102] + symbol + self.game_string[103:]
                print(self.player1 + "\t\t" + self.player2)
                print(str(self.player1_score) + "\t\t" + str(self.player2_score))
                print(self.game_string)
        
        else:
            print("That spot is not real try again!")
            self.player_turn(symbol, enemy_symbol)