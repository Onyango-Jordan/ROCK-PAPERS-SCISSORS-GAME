"""A programme for rock papers scissors game"""
import random, sys, time

#Game start
print("ROCK, PAPERS, SCISSORS.")

#Inviting player
print("Welcome to Rock, Papers, Scissors game by Jordan:")
print("\nPlease enter your name:")
player_name = input()
time.sleep(2)
print(f"Hello {player_name}, Welcome to Rock, Papers, Scissors game\n", end=",")
print("The game is about to begin.\n")

#Variables to keep track of losses, wins and ties.
wins = 0
losses = 0
ties = 0

#Entering the main progmae loop
while True:
    print(f"Wins({wins}), Losses({losses}), Ties({ties})")
    while True:#Player loop
        print("\nEnter your move in (r)ock, (p)apers, (s)cissors, (q)uit")
        player_move = input()
        if player_move == "q":
            print(f"Welcome again another time {player_name} ")
            sys.exit()
        elif player_move == "r" or player_move == "p" or player_move == "s":
            break

    #Display player move.
    if player_move == "r":
        print("ROCK versus...")
    elif player_move == "p":
        print("PAPERS versus...")
    elif player_move == "s":
        print("SCISSORS versus...")

    #Display Computer move.
    secret_number = random.randint(1, 3)
    if secret_number == 1:
        computer_move = "r"
        print("ROCK")
    elif secret_number == 2:
        computer_move = "p"
        print("PAPERS")
    elif secret_number == 3:
        computer_move = "s"
        print("SCISSORS")

    #Display Ties,Wins and losses
    if player_move == computer_move:
        print("Its a tie!")
        ties = ties + 1
    elif player_move == "r" and computer_move == "s":
        print("Its a win!")
        wins = wins + 1
    elif player_move == "p" and computer_move == "r":
        print("Its a win!")
        wins = wins + 1
    elif player_move == "s" and computer_move == "P":
        print("Its a win!")
        wins = wins + 1
    elif player_move == "s" and computer_move == "r":
        print("Its a loss!")
        losses = losses + 1
    elif player_move == "r" and computer_move == "p":
        print("Its a loss!")
        losses = losses + 1
    elif player_move == "p" and computer_move == "s":
        print("Its a loss!")
        losses = losses + 1


        

