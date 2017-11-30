## Alpha Pack Simulation

Since Alpha Packs were released, I've been wondering how many games I would need to play before winning a pack, statistically speaking. To answer this, I've written a script in Python that assumes a win rate (50% by default) and simulates Alpha Pack rolls while playing Casual in the following way:

- Start with a 3% chance of getting a pack.
- If a game results in a win, roll. If you get a pack, set the chance back to 3%, if not increase the chance by 2%
- If a game results in a loss, increase the chance by 1.5%

The same applies to Ranked games, just swap 2% for 2.5% and 1.5% for 2%.

It turns out that the expected number of games to play before receiving an Alpha Pack is 8.58 for Casual, and 3.91 for Ranked (that's the average over 1,000,000,000 simulated games).
Here is a graph of what the convergence looks like over time: https://imgur.com/np9f6hb
