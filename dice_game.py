import random
wins = 0
games = 0
playing = True
def roll(wins, games):
    for i in range(3):
        input("enter to roll!")
        dice_1 = random.randint(1, 6)
        print(f"dice 1 is {dice_1}")
        dice_2 = random.randint(1, 6)
        print(f"dice 2 is {dice_2}")
        total = dice_1 + dice_2
        print(f"your total is {total}")
        if total == 7 or total == 11:
            print("you win!")
            winner = True
            break
        else:
            winner = False
            if i <= 2:
                print("sorry, try again")

    if winner:
        print("well done!")
        wins += 1
    else:
        print("you loser")
    games += 1
    return wins, games
while playing:
    if games == 0:
        wins, games = roll(wins, games)
    else:
        choice = input("would you like to play again? ")
        if choice == "yes":
            playing = True
            wins, games = roll(wins, games)
        elif choice == "no":
            playing = False
        else:
            print("please enter 'yes' or 'no'")

print(f"you played {games} games total, and won {wins}")
print(f"you win percentage is {round((wins / games) * 100, 2)}%")