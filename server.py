Board = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

moves = []

for key in Board:
    moves.append(key)  #running through each board 

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('---')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('---')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

#all gameplay
def game():

    turn = 'x'
    count = 0


    for i in range(10):
        printBoard(Board)
        print("your turn" + turn + "next move?")

        move = input()

        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("alreadytaken move?")
            continue


        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ': #  top
                printBoard(Board)
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ': #  middle
                printBoard(Board)
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ': #  bottom
                printBoard(Board)
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ': #  left
                printBoard(Board)
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ': #  middle
                printBoard(Board)
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ': #
                printBoard(Board)
                break
            elif Board['7'] == Board['5'] == Board['3'] != ' ': # diagonal
                printBoard(Board)
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ':
                printBoard(Board)
                break



        if turn =='x':
            turn = 'o'
        else:
            turn = 'x'


if __name__ == "__main__":
    game()