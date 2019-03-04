from datetime import date, datetime

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.phase = 1

    def __str__(self):
        return f"{self.name} is on Phase {self.phase} with a score of {self.score}"

    def next_phase(self):
        self.phase += 1
        return self.phase
        
def score_track():
    
    round = 1
    # Get number of players and create players' list
    n = 0
    while n < 2 or n > 6:
        try:
            n = int(input("Enter number of players (2 - 6): "))
        except:
            pass

    players = []

    for num in range(1, n + 1):
        name = input(f"Player {num}, enter your name: ")
        players.append(Player(name))


    # Create score logs file
    score_logs = open("score_logs.txt", "a+")

    # Control to loop while no player has reached phase 10
    while all(player.phase < 10 for player in players):
        
        for player in players:
        # Check who got their phase
            phase_check(player)

        # Check round winner
        round_end = int(input("Who won the round? "))
        
        # Validate input
        while round_end < 1 or round_end > n:
            print("Invalid input.")
            round_end = int(input("Who won the round? "))
                
        # Add scores, skipping player who won the round
        for player in players:
            if players.index(player) != (round_end - 1):
                player.score += score_calc(player.name)
              
        # Print current round and scores
        print()
        print("Round: {}".format(str(round)))
        for player in players:
            print(player)
        print()

        ender = players[round_end - 1].name
        # Update round
        round += 1

    # Find player with lower score and save as winner
    players.sort(key = lambda player: player.score)
    winner = players[0].name
     
    result = f"{winner} wins! {ender} ended the last round. The game ended on Round {round}."
    score_logs.write("Game played on " + date.today().strftime("%m/%d/%Y") + " at " + datetime.now().strftime("%H:%M") + "\n")
    score_logs.write(result + "\n")
    score_logs.write("Players: \n")
    for player in players:
        score_logs.write(f"{player.name}\n")
    score_logs.write("-"*len(result) + "\n\n")
    score_logs.close()
    print(result)
    return 0

def phase_check(player):
    p_phase = input(f"{player.name}, did you get your phase? ")
    while p_phase == "" or (p_phase[0].lower() != "y" and p_phase[0].lower() != "n"):
        print("Invalid input - please answer yes or no.")
        p_phase = input(f"{player.name}, did you get your phase? ")

    if p_phase[0].lower() == "y":
        player.next_phase()
        

def score_calc(player):
    
    while True:
        try:
            a1_9 = int(input("f{player}, enter number of 1-9 cards: "))
            break
        except:
            print("Invalid Input - enter an integer")
    
    while True:
        try:
            a10_12 = int(input("f{player}, enter number of 10-12 cards: "))
            break
        except:
            print("Invalid Input - enter an integer")
    
    while True:
        try:
            a_skip = int(input("f{player}, enter number of Skip cards: "))
            break
        except:
            print("Invalid Input - enter an integer")
    
    while True:
        try:
            a_wild = int(input(f"{player}, enter number of Wild cards: "))
            break
        except:
            print("Invalid Input - enter an integer")

    return ((a1_9 * 5) + (a10_12 * 10) + (a_skip * 15) + (a_wild * 25))


if __name__ == "__main__":
    score_track()
    input("Press any key to exit")