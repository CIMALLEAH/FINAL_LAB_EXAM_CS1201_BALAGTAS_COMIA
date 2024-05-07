import random

class DiceGame:
    def __init__(self) -> None:
       pass
        
    
    def load(self):
        pass
        
    def save(self):
        pass
    def play(self):

        player_points = 0
        
        while  True:
            turn = 0
            player_score = 0
            cpu_score = 0
            while turn < 3:
                player = random.randint(1, 6)
                cpu = random.randint(1, 6)
        
                print(f"Player rolled {player}")
                print(f"CPU rolled {cpu}")
                turn += 1

                if player > cpu:
                    player_score += 1
                else:
                    cpu_score +=1
            if player_score > cpu_score:
                print("Player wins.")
                player_points += player_score + 3
                print(player_points)

                return player_points
            else:
                print("CPU wins.")

            try:
                action = input("Continue game (y/n): ").lower()
                if action != 'y':
                    break
            except ValueError as e:
                print(f"Error. {e}")

            
    def top_score(self):
        pass
    def logout(self):
        pass
    def menu(self):
        pass

q1 = DiceGame()

q1.play()