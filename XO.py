import os
table = ["-","-","-",
         "-","-","-",
         "-","-","-"]

current_player = "X"
game_still_going = True

def show_current():
    print("------------------------")
    print("current_player" +" " + current_player)   
    print("------------------------")

def show_table(table):
    print("|" + table[6] + "|" + table[7] + "|" + table[8] + "|")
    print("|" + table[3] + "|" + table[4] + "|" + table[5] + "|")
    print("|" + table[0] + "|" + table[1] + "|" + table[2] + "|")
    
def playerplay(current_player, table):
    put = input("Where you want to put: ")
    print("========================")
    print("========================")
    print("========================")
    print("========================")
    print("========================")
    
    if put not in ["1","2","3","4","5","6","7","8","9"] :
        print("Plz input 1-9")
        show_table(table)
        playerplay(current_player, table)
    else :
        putting = int(put) - 1
        if table[putting] == "X" or table[putting] == "O" :
            print("Can't Put here put again")
            show_table(table)
            playerplay(current_player, table)  
        else :
            table[putting] = current_player 

def check_row(table,current_player):
    Row_1 = table[6] == table[3] == table[0] != "-"
    Row_2 = table[7] == table[4] == table[1] != "-"
    Row_3 = table[8] == table[5] == table[2] != "-"
    
    if Row_1 or Row_2 or Row_3 :
        return True
    
def check_column(table,current_player):
    Col_1 = table[6] == table[7] == table[8] != "-"
    Col_2 = table[3] == table[4] == table[5] != "-"
    Col_3 = table[0] == table[1] == table[2] != "-"

    if Col_1 or Col_2 or Col_3 :
        return True
    
def check_X(table,current_player):
    X_1 = table[6] == table[4] == table[2] != "-"
    X_2 = table[8] == table[4] == table[0] != "-"
    
    if X_1 or X_2 :
        return True
        
def check_Tie(table):
    if "-" not in table:
        return True

def check_winner(table, current_player):
    Row = check_row(table, current_player)
    Column = check_column(table, current_player)
    X = check_X(table, current_player)
    Tie = check_Tie(table)
    
    if Row or Column or X:
        return current_player
    elif Tie:
        return "No"
    
def change_player(current_player) :
    if current_player == "X" :
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return current_player
    
while game_still_going :
    show_current()
    show_table(table)
    playerplay(current_player, table)
    now_winner = check_winner(table, current_player) 
    
    if now_winner == "X" or now_winner == "O" or now_winner == "No":
        os.system('cls')
        game_still_going = False
    else :
        current_player = change_player(current_player)
        os.system('cls')

print("========================")
print("    !!!game over!!!")
print("        " + now_winner + " win")
show_table(table)
print("========================")