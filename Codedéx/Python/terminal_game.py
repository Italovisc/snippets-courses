import random

# Variables declaration
hp = 30
potions = 2
warden_hp = 25

# Outputting player status and introduction
print(f"""----------- PLAYER STATUS ----------
HP: {hp}
Potions: {potions}
------------------------------------""")
print("You are a traveler arriving at a ruined kingdom. The Ember Crown, which kept the realm alive, has been stolen by the Warden of the Sunken Keep. You must take it back.")

# --- PART 1 ---
print("\nThe kingdom lies silent. Ash drifts from a gray sky. You reach a crossroads. To the left, a dark forest. To the right, a crumbling stone bridge.")

choice = ""
while choice not in ["1", "2"]:
    choice = input("1. Take the forest path\n2. Cross the bridge\nChoice: ")
    if choice not in ["1", "2"]:
        print("Wrong input! Please select 1 or 2.\n")

# --- PART 1A ---
if choice == "1":
    print("\nAmong the trees, an old hermit sits beside a dying fire. \"Traveler,\" he whispers, \"I can give you a healing potion, but I ask for something in return: half of your food.\"")

    choice = ""
    while choice not in ["1", "2"]:
        choice = input("1. Accept the deal (gain 1 potion, lose 5 HP from hunger)\n2. Refuse and keep walking\nChoice: ")
        if choice not in ["1", "2"]:
            print("Wrong input! Please select 1 or 2.\n")

    # Checking choices
    if choice == "1":
        potions += 1
        hp -= 5

# --- PART 1B ---
elif choice == "2":
    print("\nA troll blocks the bridge. \"Toll!\" he growls. \"Pay me, or pass through my fists.\"")

    choice = ""
    while choice not in ["1", "2", "3"]:
        choice = input("1. Pay the toll (lose 1 potion)\n2. Fight the troll (lose 10 HP, but he flees)\n3. Try to sneak past (50% chance: you slip by at no cost, or the troll catches you and you lose 15 HP)\nChoice: ")
        if choice not in ["1", "2", "3"]:
            print("Wrong input! Please select 1, 2 or 3.\n")

    # Checking choices
    if choice == "1":
        potions -= 1
    elif choice == "2":
        hp -= 10
    elif choice == "3":
        chance = random.randint(0, 1)

        if chance == 0:
            print("\nThe troll catches you!")
            hp -= 15
        else: 
            print("\nYou slip past unseen.")


# --- PART 2 ---
# Outputting player status
print(f"""\n----------- PLAYER STATUS ----------
HP: {hp}
Potions: {potions}
------------------------------------""")
print("The Sunken Keep rises from the lake of black water. A guard patrols the main gate. Beside it, a rusty drain leads inside.")

choice = ""
while choice not in ["1", "2"]:
    choice = input("1. Storm the main gate (lose 8 HP fighting the guard)\n2. Crawl through the drain (lose 3 HP, but you stay unseen)\nChoice: ")
    if choice not in ["1", "2"]:
        print("Wrong input! Please select 1 or 2.\n")

# Checking choices
if choice == "1":
    hp -= 8
elif choice == "2":
    hp -= 3


# --- PART 3 (FINAL BATTLE) ---
print("The Warden turns. Armor of black iron, eyes like cold embers. In his hands, the Ember Crown glows. \"You are not the first,\" he says. \"You will not be the last.\"")

while warden_hp > 0 and hp > 0:
    attack = random.randint(4, 8)
    warden_attack = random.randint(3, 7)

    print(f"""\n----------- PLAYER STATUS ----------
HP: {hp}
Potions: {potions}
------------------------------------""")
    print(f"Warden HP: {warden_hp}")

    choice = ""
    choice = input("""\n1. Attack: deals 4 to 8 damage
2. Block: halves the damage you take this turn
3. Heal: uses 1 potion and restores 10 HP (only if you still have a potion)
Action: """)

    # Checking choices
    if choice not in ["1", "2", "3"]:
        print("Wrong input! Please select 1, 2 or 3.\n")
    # Attack
    elif choice == "1":
        warden_hp -= attack
        print(f"You attacked for {attack} damage!")
        if warden_hp > 0:
            hp -= warden_attack
            print(f"The Warden attacked for {warden_attack} damage!")
    # Block
    elif choice == "2":
        damage = warden_attack // 2
        hp -= damage
        print(f"You blocked! The Warden's attack deals only {damage} damage.")
    # Heal
    elif choice == "3":
        if potions > 0:
            potions -= 1
            hp += 10
            hp -= warden_attack
            print(f"You healed 10 HP!\nThe Warden attacked for {warden_attack} damage!")
        else:
            print("You have no potions")


# --- ENDING ---
# --- ENDING 1 ---
if hp <= 0:
    print("\nYour vision fades. The ash settles over you, and the kingdom stays silent.\nENDING: Defeat")
elif warden_hp <= 0:
    print("\nAfter The Warden falls, you choose to:")

    choice = ""
    while choice not in ["1", "2"]:
        choice = input("1. Claim the crown\n2. Destroy the crown\nChoice: ")
        if choice not in ["1", "2"]:
            print("Wrong input! Please select 1 or 2.\n") 

    # Checking choices
    # --- ENDING 2 ---
    if choice == "1":
        print("\nYou place the Ember Crown upon your head. Warmth floods the land, but you feel its power whispering back. You are a hero...or a new warden.\nENDING: Same Old Story")
    # --- ENDING 3 ---
    elif choice == "2":
        print("\nYou shatter the Ember Crown against the stone. The embers scatter and become fireflies, and the kingdom slowly wakes.\nENDING: The Loop Ends")
