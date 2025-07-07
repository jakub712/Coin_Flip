import random
win_streak = 0 
while True:
    selection = input("Pick, heads or tails? ")

    options = ["heads", "tails"]
    result = random.choice(options)

    if selection not in ["heads","tails"]:
        print("please pick only heads or tails")
        continue
        
    if selection == result:
        win_streak += 1
        print(f"It landed on {result},you win! You have a win streak of {win_streak}")
    else:
        win_streak = 0
        print(f"It landed on {result},you Lose!")

