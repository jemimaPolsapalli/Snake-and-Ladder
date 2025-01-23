import random
from collections import defaultdict
snakes = {97: 78, 95: 56, 88: 24, 62: 18, 48: 26, 36: 6, 32: 10}
ladders = {2: 23, 8: 34, 20: 77, 30: 83, 41: 81, 54: 93, 71: 92}
def roll_dice():
    return random.randint(1, 6)
def play_game(num_players):
    positions = [0] * num_players
    while True:
        for i in range(num_players):
            roll=roll_dice()
            positions[i]+=roll
            if positions[i] in ladders:
                positions[i]=ladders[positions[i]]  
            if positions[i] in snakes:
                positions[i]=snakes[positions[i]]
            if positions[i]>=100:
                return i+1
num_games=100
player_range=range(2, 11)
results=defaultdict(lambda: defaultdict(int))
for num_players in player_range:
    for _ in range(num_games):
        winner=play_game(num_players)
        results[num_players][winner] += 1
for num_players, winners in results.items():
    print(f"\nResults for {num_players} players:")
    for player, wins in sorted(winners.items()):
        print(f"Player {player} won {wins} times")