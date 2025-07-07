import random
win_streak = 0 #
rounds = 0#

win = 0  #
loss = 0  #
longest_streak = 0
win_rate = 0#

while True:
    total_games = int(input("How many games do you wanna play good sir? Write a number from 1 to 10. "))
    games_options = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    if total_games not in games_options:
        print("pick a number 1-10")
    else:
        break


while True:
    selection = input("Pick, heads or tails? ")

    options = ["heads", "tails"]
    result = random.choice(options)

    if selection not in ["heads","tails"]:
        print("please pick only heads or tails")
        continue
        
    if selection == result:
        win += 1
        win_streak += 1
        rounds += 1
        if win_streak > longest_streak:
            longest_streak = win_streak
        print(f"It landed on {result},you win! You have a win streak of {win_streak}")
    else:
        loss += 1
        win_streak = 0
        rounds +=1
        print(f"It landed on {result},you Lose!")

    if rounds == total_games:
        win_rate = int((win / total_games) * 100)
        break


print (f"""
📝 Text Analysis Complete!
--------------------------
Total Games: {total_games}
       
Total Wins: {win}
Total Lossess: {loss}

Win Rate: {win_rate}%

Longest Win Streak: {longest_streak}
--------------------------
""")
