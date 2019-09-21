from random import randrange


def board():

    board = [[] for num in range(0, 4)]

    for row in range(1, 4):
        if row == 0:
            continue
        if row == 1:
            board[row] = '     |     |    \n  {}  |  {}  |  {}  \n_____|_____|_____'.format(
                plays[0], plays[1], plays[2])

        elif row == 2:
            board[row] = '     |     |    \n  {}  |  {}  |  {}  \n_____|_____|_____'.format(
                plays[3], plays[4], plays[5])
        elif row == 3:
            board[row] = '     |     |    \n  {}  |  {}  |  {}  \n     |     |'.format(
                plays[6], plays[7], plays[8])

    for a in board[1:4]:
        print(a)


plays = [z for z in range(1, 10)]


def board_call(user_input, token):

    board = [[] for num in range(0, 4)]
    inp = user_input
    indx = inp - 1
    plays[indx] = token

    for row in range(1, 4):
        if row == 0:
            continue
        if row == 1:
            board[row] = '     |     |    \n  {}  |  {}  |  {}  \n_____|_____|_____'.format(
                plays[0], plays[1], plays[2])

        elif row == 2:
            board[row] = '     |     |    \n  {}  |  {}  |  {}  \n_____|_____|_____'.format(
                plays[3], plays[4], plays[5])
        elif row == 3:
            board[row] = '     |     |    \n  {}  |  {}  |  {}  \n     |     |'.format(
                plays[6], plays[7], plays[8])

    for a in board[1:4]:
        print(a)


class Player:
    def __init__(self, token, name):
        self.token = token
        self.name = name

    def get_token(self):
        return self.token

    def get_name(self):
        return self.name


def greeting():
    print('\nHello, will you be playing alone today?\n')
    while True:
        ans = input('\nEnter "Y" for yes and "N" for no.\n')
        player_lst = []
        if ans.upper() == "Y":
            usrname = input("\nWhat will your username be?\n")
            Player1 = Player("X", usrname)
            player_lst.append(Player1)
            CPU = Player("O", "CPU")
            player_lst.append(CPU)
            print("\nYou will be X's and the computer will be O's.\n")
            return player_lst

        elif ans.upper() == "N":
            usrname1 = input("\nThe more the merrier!\n\nPlayer 1, what will your username be?\n")
            Player1 = Player("X", usrname1)
            player_lst.append(Player1)
            usrname2 = input('\nPlayer 2, what will your username be?\n')
            Player2 = Player("O", usrname2)
            player_lst.append(Player2)
            print("\n{} will be X's and {} will be O's.\nLet the games begin!\n".format(
                Player1.get_name(), Player2.get_name()))
            return player_lst
        else:
            print("\nSorry, that is an invalid answer\n.")


def winning_cond(token):
    if plays[0:3].count(token) == 3:
        return True
    elif plays[3:6].count(token) == 3:
        return True
    elif plays[6:9].count(token) == 3:
        return True
    elif [plays[0], plays[3], plays[6]].count(token) == 3:
        return True
    elif [plays[1], plays[4], plays[7]].count(token) == 3:
        return True
    elif [plays[2], plays[5], plays[8]].count(token) == 3:
        return True
    elif [plays[0], plays[4], plays[8]].count(token) == 3:
        return True
    elif [plays[2], plays[4], plays[6]].count(token) == 3:
        return True
    else:
        return False


def turn(Player):
    while True:
        if Player.get_name() == "CPU":
            print("\nComputer selecting position...\n")
            while True:
                cpu_choice = randrange(1, 10)
                if cpu_choice in plays:
                    board_call(cpu_choice, Player.get_token())
                    print("\nComputer has selected!\n")
                    return plays
            return
        else:
            print("\n{}, it is your turn.\n".format(Player.get_name()))
            board()
            try:
                P_choice = int(input("\nSelect an open position!\n"))

                if P_choice in plays and P_choice <= 9:
                    board_call(P_choice, Player.get_token())
                    if winning_cond(Player.get_token()):
                        print("\n{} won this round!\n~GAME OVER~".format(Player.get_name()))
                        return
                    else:
                        return plays
                else:
                    print("\nThat is an invalid choice please try again.\n")

            except ValueError:
                print("\nThat is an invalid choice please try again.\n")


def game_time():
    players = greeting()
    first = randrange(0, 2)
    P1 = players.pop(first)
    P2 = players[0]
    print("Randomizing first turn..")
    print("{} will start the game".format(P1.get_name()))
    print("In order to select a position: enter the number(0-9), to a corresponding tile, that does not have a token.")

    while True:

        turn(P1)
        if winning_cond(P1.get_token()):
            return False
        turn(P2)
        if winning_cond(P2.get_token()):
            return False


print("Erik is a bitch!")
game_time()
