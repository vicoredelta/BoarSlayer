from character import Character
from engagement import Engagement

player = Character("Bob")

while(True):
    boar = Character("Boar")
    print("You are fighting " + boar.name + "!")
    input()
    battle = Engagement(player, boar)
    while(battle.status == "Ongoing"):
        battle.do_turn()

    if(battle.status == "Opponent won"):
        print("You have been defeated. Game over!")
        input()
        break

    if (battle.status == "Player won"):
        print("You have defeated " + boar.name + "!")
        input()
        print(player.add_xp(6))
        input()
        print("You venture further.")
        input()