x_wins = False
o_wins = False
game_on = True
turn = 1
players_turn = 1
grid_dict = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}
grid_disp = f" {grid_dict[0]} | {grid_dict[1]} | {grid_dict[2]}      1 | 2 | 3 \n" \
            f"-----------    -----------\n" \
            f" {grid_dict[3]} | {grid_dict[4]} | {grid_dict[5]}      4 | 5 | 6 \n" \
            f"-----------    -----------\n" \
            f" {grid_dict[6]} | {grid_dict[7]} | {grid_dict[8]}      7 | 8 | 9 \n"

winning_moves = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (2,4,6), (0,4,8)]


def check_for_winner(player, moves):
    if player == 1:
        for win_move in winning_moves:
            if win_move[0] in moves and win_move[1] in moves and win_move[2] in moves:
                return True
            return False
    if player == 2:
        for win_move in winning_moves:
            if win_move[0] in moves and win_move[1] in moves and win_move[2] in moves:
                return True
            return False


player_1_moves = []
player_2_moves = []

while game_on:
    if turn == 1:
        print("Let's play Tic Tac Toe!\nX goes first!")
    if turn == 9:
        game_on = False
    print(grid_disp)
    if players_turn == 1:
        move = int(input("Player 1's Turn (X)! Please enter a number to place your X (Must enter a valid number or you lose):"))-1
        if grid_dict[move] == " ":
            player_1_moves.append(move)
            grid_dict[move] = "X"
            grid_disp = f" {grid_dict[0]} | {grid_dict[1]} | {grid_dict[2]}      1 | 2 | 3 \n" \
                        f"-----------    -----------\n" \
                        f" {grid_dict[3]} | {grid_dict[4]} | {grid_dict[5]}      4 | 5 | 6 \n" \
                        f"-----------    -----------\n" \
                        f" {grid_dict[6]} | {grid_dict[7]} | {grid_dict[8]}      7 | 8 | 9 \n"
            if check_for_winner(player=1, moves=player_1_moves):
                x_wins = True
                game_on = False
            players_turn = 2
            turn += 1
        else:
            print("You can't go there, please try again!")
    else:
        move = int(input("Player 2's Turn (O)! Please enter a number to place your O (Must enter a valid number or you lose):"))-1
        if grid_dict[move] == " ":
            player_2_moves.append(move)
            grid_dict[move] = "O"
            grid_disp = f" {grid_dict[0]} | {grid_dict[1]} | {grid_dict[2]}      1 | 2 | 3 \n" \
                        f"-----------    -----------\n" \
                        f" {grid_dict[3]} | {grid_dict[4]} | {grid_dict[5]}      4 | 5 | 6 \n" \
                        f"-----------    -----------\n" \
                        f" {grid_dict[6]} | {grid_dict[7]} | {grid_dict[8]}      7 | 8 | 9 \n"
            if check_for_winner(player=2, moves=player_2_moves):
                o_wins = True
                game_on = False
            players_turn = 1
            turn += 1
        else:
            print("You can't go there, please try again!")

if x_wins:
    print("Player 1 (X) Wins!")
elif o_wins:
    print("Player 2 (O) Wins!")
else:
    print("Tie!")

