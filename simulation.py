import random
import matplotlib.pyplot as plt


def game_outcome(rate):
    if random.randrange(1, 100) >= rate * 100:
        return True  # returns 'True' for a win
    else:
        return False  # returns 'False' for a loss


def roll_casual(chance, rate, packs):
    if game_outcome(rate):
        if random.randrange(1, 100) <= chance:
            chance = 3
            packs += 1
            return chance, packs
        else:
            chance = chance + 2
            return chance, packs
    else:
        chance = chance + 1.5
        return chance, packs


def roll_ranked(chance, rate, packs):
    if game_outcome(rate):
        if random.randrange(1, 100) <= chance:
            chance = 3
            packs += 1
            return chance, packs
        else:
            chance = chance + 3
            return chance, packs
    else:
        chance = chance + 2.5
        return chance, packs


def sequence_convergence_casual(rate, games):
    current_chance = 3
    games_per_pack = []
    packs_won_temp = 0

    for k in range(0, len(games)):
        for l in range(0, games[k]):
            current_chance, packs_won_temp = roll_casual(current_chance, rate, packs_won_temp)
        if packs_won_temp > 0:
            games_per_pack.append(games[k] / packs_won_temp)
        else:
            games_per_pack.append(games[k])
        packs_won_temp = 0
    return games_per_pack


def sequence_convergence_ranked(rate, games):
    current_chance = 3
    games_per_pack = []
    packs_won_temp = 0

    for k in range(0, len(games)):
        for l in range(0, games[k]):
            current_chance, packs_won_temp = roll_ranked(current_chance, rate, packs_won_temp)
        if packs_won_temp > 0:
            games_per_pack.append(games[k] / packs_won_temp)
        else:
            games_per_pack.append(games[k])
        packs_won_temp = 0
    return games_per_pack


win_rate = 0.5
games_played = [100, 200, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

sequence_casual = sequence_convergence_casual(win_rate, games_played)
sequence_ranked = sequence_convergence_casual(win_rate, games_played)

print(games_played)
print(sequence_casual)
print(sequence_ranked)

# Casual
fig_casual = plt.figure()
ax = fig_casual.add_subplot(111)
ax.plot(games_played, sequence_casual)
plt.ylim([8, 15])

ax.set_xlabel('Number of games played')
ax.set_ylabel('Games played per Alpha pack')
ax.set_title('Casual')

plt.show()
# plt.savefig('casual_aphpa_pack_simulation.png', dpi=512)

# Ranked
fig_ranked = plt.figure()
ax = fig_ranked.add_subplot(111)
ax.plot(games_played, sequence_ranked)
plt.ylim([8, 15])

ax.set_xlabel('Number of games played')
ax.set_ylabel('Games played per Alpha pack')
ax.set_title('Ranked')

plt.show()
# plt.savefig('ranked_aphpa_pack_simulation.png', dpi=512)


current_chance = 3
games_played = 10000000
packs_won = 0

for i in range(0, games_played):
    current_chance, packs_won = roll_casual(current_chance, win_rate, packs_won)

avg_games_per_pack = round(games_played / packs_won, 4)
print('\nstatistics for casual games:')
print('packs won: ' + str(packs_won))
print('average games per pack ' + str(avg_games_per_pack))

for j in range(0, games_played):
    current_chance, packs_won = roll_ranked(current_chance, win_rate, packs_won)

avg_games_per_pack = round(games_played / packs_won, 4)
print('\nstatistics for ranked games:')
print('packs won: ' + str(packs_won))
print('average games per pack ' + str(avg_games_per_pack))
