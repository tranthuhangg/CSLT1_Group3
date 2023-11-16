import random

num_simulations = 10
total_flips = 0

for _ in range(num_simulations):
    flips = 0
    consecutive = 0
    previous_outcome = None

    while consecutive < 3:
        outcome = random.choice(['H', 'T'])
        flips += 1

        if outcome == previous_outcome:
            consecutive += 1
        else:
            consecutive = 1

        print(outcome, end=' ')

        previous_outcome = outcome

    print(f"({flips} flips)")
    total_flips += flips

average_flips = total_flips / num_simulations
print("\non average,", average_flips, "flips were needed.")