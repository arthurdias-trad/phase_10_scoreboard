from datetime import date

def score_track():
    
    # Initialize variables to keep track of phase, round, score and winner
    player_one_phase = 1
    player_two_phase = 1
    player_one_score = 0
    player_two_score = 0
    current_round = 1
    winner = ""
    ender = ""
    today = date.today()

    # Create score file
    score = open("score.txt", "a+")

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
            p2_1_9 = int(input("Player 2, enter number of 1-9 cards: "))
            p2_10_12 = int(input("Player 2, enter number of 10-12 cards: "))
            p2_skip = int(input("Player 2, enter number of Skip cards: "))
            p2_wild = int(input("Player 2, enter number of Wild cards: "))
            player_two_score += ((p2_1_9 * 5) + (p2_10_12 * 10) + (p2_skip * 15) + (p2_wild * 25))

        # If player two wins the phase
        else:

            # Advance player two phase
            player_two_phase += 1

            # Add player one score
            p1_1_9 = int(input("Player 2, enter number of 1-9 cards: "))
            p1_10_12 = int(input("Player 2, enter number of 10-12 cards: "))
            p1_skip = int(input("Player 2, enter number of Skip cards: "))
            p1_wild = int(input("Player 2, enter number of Wild cards: "))
            player_one_score += ((p1_1_9 * 5) + (p1_10_12 * 10) + (p1_skip * 15) + (p1_wild * 25))
        
        # Print current round and scores
        print()
        print("Round: {}".format(str(current_round)))
        print("Player 1 is on Phase {}. Current score: {}".format(str(player_one_phase), str(player_one_score)))
        print("Player 2 is on Phase {}. Current score: {}".format(str(player_two_phase), str(player_two_score)))
        print()

        # Update round
        current_round += 1

    if player_one_score < player_two_score:
        winner = "Player 1"
    else:
        winner = "Player 2"

    if player_one_phase > 10:
        ender = "Player 1"
    else:
        ender = "Player 2"
    
    result = ("{} wins! {} ended the game by completing Phase 10. The game ended on Round {}. Player 1 scored {}. Player 2 scored {}".format(winner, ender, str(current_round), str(player_one_score), str(player_two_score)))
    score.write("Game played on " + today.strftime("%m/%d/%Y") + "\n")
    score.write(result + "\n")
    score.write("---------------------------------------------------------------\n\n")
    score.close()
    print(result)
    return 0

if __name__ == "__main__":
    score_track()