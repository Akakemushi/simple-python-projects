import random, sys
print("ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0

while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_move = input()
        if player_move == "q":
            sys.exit()
        if player_move == "r" or player_move == "p" or player_move == "s":
            break
        print("Type either r, p, s, or q.")
    if player_move == "r":
        print("ROCK versus...")
    elif player_move == "p":
        print("PAPER versus...")
    elif player_move == "s":
        print("SCISSORS versus...")

    random_num = random.randint(1, 3)
    if random_num == 1:
        computer_move = "r"
        print("ROCK")
    elif random_num == 2:
        computer_move = "p"
        print("PAPER")
    elif random_num == 3:
        computer_move = "s"
        print("SCISSORS")
    if player_move == computer_move:
        print("It's a tie!")
        ties = ties + 1
    elif player_move == "r" and computer_move == "s":
        print("You win!")
        wins = wins + 1
    elif player_move == "s" and computer_move == "p":
        print("You win!")
        wins = wins + 1
    elif player_move == "p" and computer_move == "r":
        print("You win!")
        wins = wins + 1
    elif player_move == "r" and computer_move == "p":
        print("You lose!")
        losses = losses + 1
    elif player_move == "p" and computer_move == "s":
        print("You lose!")
        losses = losses + 1
    elif player_move == "s" and computer_move == "r":
        print("You lose!")
        losses = losses + 1
