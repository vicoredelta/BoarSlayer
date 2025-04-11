class Character:
    def __init__(self, name):
        self.name = name
        self.max_health = 10
        self.current_health = 10
        self.max_mana = 10
        self.current_mana = 10
        self.strength = 3
        self.intelligence = 3
        self.level = 1
        self.xp = 0

    def attack(self, opponent):
        opponent.current_health = max(opponent.current_health - self.strength, 0)
        return (self.name + " attacks " + opponent.name + " for " + str(self.strength) + " damage.")

    def heal(self):
        self.current_mana = max(self.current_mana - 5, 0)
        self.current_health = min(self.current_health + self.intelligence*2, self.max_health)
        return (self.name + " heals himself of " + str(self.intelligence*2) + " damage.")

    def add_xp(self, xp):
        self.xp = self.xp + xp
        message = "You gain " + str(xp) + " experience."
        if self.xp >= self.xp_for_levelup():
            self.level_up()
            message = message + " You level up!"
        return message

    def level_up(self):
        self.level = self.level + 1
        self.strength = self.strength + 1
        self.intelligence = self.intelligence + 1
        self.max_health = self.max_health + 2
        self.current_health = self.current_health + 2
        self.max_mana = self.max_mana + 2
        self.current_mana = self.current_mana + 2

    def xp_for_levelup(self):
        return int(10 * self.level + pow(self.level-1, 2))

    def display_character_info(self):
        print(self.name)
        print("Level: " + str(self.level) + "\tExperience: " + str(self.xp) + "/" + str(self.xp_for_levelup()))
        print("Health: " + str(self.current_health) + "/" + str(self.max_health) +
              "\tMana: " + str(self.current_mana) + "/" + str(self.max_mana))
        print("Strength: " + str(self.strength) + "\tIntelligence: " + str(self.intelligence))
        print()

    def is_defeated(self):
        if self.current_health <= 0:
            return True
        else:
            return False