from random import randint

class Actor:
    def __init__(self):
        self.hp = 10 # health points
        self.hpmax = self.hp # max health points
        self.ap = 2 # action points
        self.atk1 = 2 # first attack
        self.atk1ap = 1 # ap for attack 1
        self.atk2 = 8 # second attack
        self.atk2ap = 3 # ap for attack 2

player = Actor()
enemy = Actor()

def attack():
    is_blocked = False
    print(f"HP - {player.hp}/{player.hpmax}, AP - {player.ap}")
    print(f"Enemy HP - {enemy.hp}")
    print(f"1. Weak Attack - (AP={player.atk1ap}, DMG<={player.atk1})")
    print(f"2. Strong Attack - (AP={player.atk2ap}, DMG<={player.atk2})")
    print(F"3. Defend (AP=0, Success chance = 80%)")
    print(f"4. Wait (AP + 1)")
    action = input(">> ")

    if action == "1":
        print(f"Enemy took {player.atk1} damage.")
        enemy.hp -= player.atk1
        player.ap -= player.atk1ap
    elif action == "2":
        damage = randint(player.atk2/2, player.atk2)
        print(f"Enemy took {damage} damage.")
        enemy.hp -= damage
        player.ap -= player.atk2ap
    elif action == "3":
        chance = randint(1,100)
        if chance <= 80:
            print("You successfully blocked enemies attack")
            is_blocked = True
        else:
            print("You failed to block the enemies attack.")
            is_blocked = False
    return is_blocked

def enemy_attack(is_blocked):
    if not is_blocked:
        print(f"The enemy delt {enemy.atk1} damage")
        player.hp -= enemy.atk1

def start():
    print("This is the battle system")
    while enemy.hp > 0 and player.hp > 0:
        enemy_attack(attack()) # the player attack returns if enemys attack is blocked
    if enemy.hp <= 0:
        print("The enemy died")
    elif player.hp <= 0:
        print("You died")

    input("Press Enter to Exit to the Main Menu")