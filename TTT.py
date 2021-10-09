'''
Created on 26 Sep 2021

@author: Oleg Ovroutsky
'''

def board(bd): # Prints board with inputs from game()
    print(bd["1"] + "|" + bd["2"] + "|" + bd["3"])
    print("_____")
    print(bd["4"] + "|" + bd["5"] + "|" + bd["6"])
    print("_____")
    print(bd["7"] + "|" + bd["8"] + "|" + bd["9"])
    return ""

def check_board(player,bd):# Checks the board for a winning status and return true or false
        if bd["1"] == bd["2"] == bd["3"] == player:
            return True
        if bd["1"] == bd["5"] == bd["9"] == player:
            return True
        if bd["1"] == bd["4"] == bd["7"] == player:
            return True
        if bd["2"] == bd["5"] == bd["8"] == player:
            return True
        if bd["3"] == bd["6"] == bd["9"] == player:
            return True
        if bd["3"] == bd["5"] == bd["7"] == player:
            return True
        if bd["4"] == bd["5"] == bd["6"] == player:
            return True
        if bd["7"] == bd["8"] == bd["9"] == player:
            return True
        return False
    
def check_av(board,spot):#Checks if the spot is available on the board and return true or false
    av = "XO"
    if board[spot] in av:
        return True


def game(): #The game

    bd = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9",} #The board dictionary
    TURNS = 0 # counts the turns to 9
    END = False #Boolean for game end status WIN/TIE

    while TURNS < 9:
            if TURNS % 2 == 0:
                print(board(bd))
                print("Player 1 Turn:")
                while True:
                    choice = input("player 1")
                    if check_av(bd,choice):
                        continue
                    else:    
                        bd[choice] = "X"
                        break
                
                if check_board("X",bd):
                    END = True
                    winner = "1"
                    break
                TURNS += 1
            else:
                print(board(bd))
                print("Player 2 Turn:")
                while True:
                    choice2 = input("player 2")
                    if check_av(bd,choice2):
                        continue
                    else:
                        bd[choice2] = "O"
                        break
                if check_board("O",bd):
                    END = True
                    winner = "2"
                    break

                TURNS += 1
    print(board(bd))
    if END == False:
        st1 = input("play again? y/n")
        board(bd)
        if st1 == "y":
            game()
        print("Goodbye")

    print(f"player {winner} won")
    st2 = input("play again? y/n")
    board(bd)
    if st2 == "y":
        game()
    print("Goodbye")
    

game()