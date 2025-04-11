import os

class Engagement:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.is_players_turn = True
        self.status = "Ongoing"
        player.current_mana = player.max_mana

    def do_turn(self):
        self.show_participants_info()
        if self.is_players_turn:
            message = self.do_player_action()
        else:
            message = self.opponent.attack(self.player)
        self.show_participants_info()
        print(message)
        input()
        if self.opponent.is_defeated():
            self.status = "Player won"
        elif self.player.is_defeated():
            self.status = "Opponent won"

        self.is_players_turn = not self.is_players_turn

    def do_player_action(self):
        while (True):
            choice = input("Attack [1]\tHeal (costs 5 mana) [2]")
            if choice == "1":
                message = self.player.attack(self.opponent)
                break
            elif choice == "2":
                if (self.player.current_mana >= 5):
                    message = self.player.heal()
                    break
                else:
                    print("Not enough mana for healing.")
        return message

    def show_participants_info(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.player.display_character_info()
        self.opponent.display_character_info()