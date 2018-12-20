from datetime import date

def score_track():
    
    # Initialize variables to keep track of phase, round, score and winner
    player_one_phase = 1
    player_two_phase = 1
    player_one_score = 0
    player_two_score = 0
    player_one = input("Player 1, enter your name: ")
    player_two = input("Player 2, enter your name: ")
    current_round = 1
    winner = ""
    ender = ""
    today = date.today()

    # Create score logs file
    score_logs = open("score_logs.txt", "a+")

    # Control to loop while neither player has finished phase 10
    while player_one_phase <= 10 and player_two_phase <= 10:
        
        # Check phase winner
        phase_end = input("Enter who won the phase - 1 or 2: ")
        
        # Validate input
        while phase_end != "1" and phase_end != "2":
            print("Invalid input.")
            phase_end = input("Enter who won the phase - 1 or 2: ")
        
        
        # If player one wins the phase
        if phase_end == "1":
            
            # Advance player one phase
            player_one_phase += 1
            
            # Add player two score
            player_two_score += score_calc("2")

        # If player two wins the phase
        else:

            # Advance player two phase
            player_two_phase += 1

            # Add player one score
            player_one_score += score_calc("1")
        
        # Print current round and scores
        print()
        print("Round: {}".format(str(current_round)))
        print("{} is on Phase {}. Current score: {}".format(player_one, str(player_one_phase), str(player_one_score)))
        print("{} is on Phase {}. Current score: {}".format(player_two, str(player_two_phase), str(player_two_score)))
        print()

        # Update round
        current_round += 1

    if player_one_score < player_two_score:
        winner = player_one
    else:
        winner = player_two

    if player_one_phase > 10:
        ender = player_one
    else:
        ender = player_two
    
    result = ("{} wins! {} ended the game by completing Phase 10. The game ended on Round {}. {} scored {}. {} scored {}".format(winner, ender, str(current_round), player_one, str(player_one_score), player_two, str(player_two_score)))
    score_logs.write("Game played on " + today.strftime("%m/%d/%Y") + "\n")
    score_logs.write(result + "\n")
    score_logs.write("---------------------------------------------------------------\n\n")
    score_logs.close()
    print(result)
    return 0

def score_calc(player_number):
    a1_9 = int(input("Player {}, enter number of 1-9 cards: ".format(player_number)))
    a10_12 = int(input("Player {}, enter number of 10-12 cards: ".format(player_number)))
    a_skip = int(input("Player {}, enter number of Skip cards: ".format(player_number)))
    a_wild = int(input("Player {}, enter number of Wild cards: ".format(player_number)))
    return ((a1_9 * 5) + (a10_12 * 10) + (a_skip * 15) + (a_wild * 25))

if __name__ == "__main__":
    score_track()