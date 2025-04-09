import world

class Character:
    def __init__(self, name):
        self.name = name
        self.attributes = Attributes()
        self.level = Leveling(1)
        self.location = world.Location()

    def engage():
        pass

    def wait():
        pass

class Attributes:
    def __init__(self):
        pass

    def __init__(self, strength, intelligence):
        self.strength = strength
        self.intelligence = intelligence

class Health:
    def __init__(self):
        pass

    def __init__(self, health):
        self.max_health = health
        self.current_health = health

class Mana:
    def __init__(self):
        pass

    def __init__(self, mana):
        self.max_mana = mana
        self.current_mana = mana

class Leveling:
    def __init__(self, level):
        self.level = level
        self.xp = 0

    # Returns true on levelup
    def add_xp(self, xp):
        self.xp = self.xp + xp

        if self.xp_to_levelup() >= self.xp:
            return True
        else:
            return False

    def xp_to_levelup(self):
        return self.level * 10