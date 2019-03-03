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

def phase_check(player):
    p_phase = input("{}, did you get your phase? ".format(player.name))
    while p_phase == "" or (p_phase[0].lower() != "y" and p_phase[0].lower() != "n"):
        print("Invalid input - please answer yes or no.")
        p_phase = input("{}, did you get your phase? ".format(player.name))

    if p_phase[0].lower() == "y":
        player.next_phase()
    else:
        pass

players = []

n = 0
while n < 2 or n > 6:
    try:
        n = int(input("Enter number of players (2 - 6): "))
    except:
        pass

for num in range(1, n+1):
    name = input(f"Player {num}, enter your name: ")
    players.append(Player(name))

for player in players:
    phase_check(player)
    print(player)


