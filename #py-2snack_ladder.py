
import random
import pandas as pd 

def play_game(board_size):
    total_cells = board_size*board_size
    num_players = 4
    winner_found = False

    results = {
        "Players": [],
        "Dice Roll History": [],
        "Position History" : [],
        "Win Status": []
    }

    player_positions = [0] * num_players
    dice_histories = [[] for _ in range(num_players)]
    pos_histories = [[] for _ in range(num_players)]
    win_status = [0] * num_players

    while not winner_found:
        for p in range(num_players):

            dice_roll = random.randint(1,6)
            dice_histories[p].append(dice_roll)

            new_pos = player_positions[p] + dice_roll

            if new_pos <= total_cells:
                player_positions[p] = new_pos

            pos_histories[p].append(player_positions[p])

            if player_positions[p] == total_cells:
                win_status[p] = 1
                winner_found = True
                break

    for p in range(num_players):
        results["Players"].append(f"Player {p+1}")
        results["Dice Roll History"].append(",".join(map(str, dice_histories[p])))
        results["Position History"].append(",".join(map(str, pos_histories[p])))
        results["Win Status"].append(win_status[p])


    return pd.DataFrame(results)


board_size = int(input("Enter board size: "))
df = play_game(board_size)

print("\nBoard Size:", board_size, "x", board_size)
print(df)
