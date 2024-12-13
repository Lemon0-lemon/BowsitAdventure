import os
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
    global stamina, inventory
    stamina = 100
    inventory = []
    clear_screen()
    print("Welcome to **Bowsit: The Treasure Hunt Adventure**!")
    print("\nYou are an adventurer seeking the legendary treasure of Bowsit. Hidden deep within an ancient jungle, the treasure is guarded by mysterious challenges. Manage your stamina and inventory wisely to survive and succeed!")
    print("\nYour journey will test your decision-making skills. Type the option letter (e.g., 'A' or 'B') to choose your path.")
    print("Good luck!\n")
    time.sleep(4)
    jungle_entrance()

def update_stamina(amount):
    global stamina
    stamina += amount
    stamina = max(0, stamina)
    print(f"\n[Stamina: {stamina}]")

def add_to_inventory(item):
    global inventory
    if item not in inventory:
        inventory.append(item)
        print(f"\nYou found a {item}! It has been added to your inventory.")

def jungle_entrance():
    clear_screen()
    update_stamina(-10)
    print("1. The Jungle Entrance")
    print("The dense jungle looms before you, the sound of distant animals echoing through the trees.")
    print("Option A: Follow the well-trodden path.")
    print("Option B: Venture into the darker, unmarked trail.")
    
    choice = input("\nWhat do you choose? (A/B): ").strip().upper()
    if choice == 'A':
        add_to_inventory('rope')
        river_crossing()
    elif choice == 'B':
        add_to_inventory('torch')
        hidden_cave()
    else:
        print("Invalid choice. Please try again.")
        jungle_entrance()

def river_crossing():
    clear_screen()
    print("2. The River Crossing")
    print("You reach a wide river with a rickety bridge.")
    print("Option A: Cross the rickety bridge.")
    print("Option B: Attempt to swim across.")
    print("Option C: Search for materials to build a raft.")

    choice = input("\nWhat do you choose? (A/B/C): ").strip().upper()
    if choice == 'A':
        update_stamina(-10)
        if random.choice([True, False]):
            print("\nThe bridge holds, and you cross safely!")
            temple_inner_sanctum()
        else:
            print("\nThe bridge breaks, and you fall into the river!")
            if 'rope' in inventory:
                print("You use the rope to climb out safely.")
                temple_inner_sanctum()
            else:
                crocodile_escape()
    elif choice == 'B':
        update_stamina(-30)
        print("\nYou encounter a crocodile!")
        if 'torch' in inventory:
            print("You fend off the crocodile with the torch and escape.")
            temple_inner_sanctum()
        else:
            crocodile_escape()
    elif choice == 'C':
        update_stamina(-20)
        print("\nYou build a raft and cross the river safely.")
        add_to_inventory('raft')
        temple_inner_sanctum()
    else:
        print("Invalid choice. Please try again.")
        river_crossing()

def crocodile_escape():
    print("Option A: Swim to the shore as fast as you can.")
    print("Option B: Try to climb back onto the broken bridge.")

    choice = input("\nWhat do you choose? (A/B): ").strip().upper()
    if choice == 'A':
        update_stamina(-20)
        if stamina > 0:
            print("\nYou swim frantically and escape the crocodile. Barely surviving!")
            temple_inner_sanctum()
        else:
            game_over()
    elif choice == 'B':
        print("\nThe crocodile attacks while you're climbing. This is the end.")
        game_over()
    else:
        print("Invalid choice. Please try again.")
        crocodile_escape()

def hidden_cave():
    clear_screen()
    print("3. The Hidden Cave")
    print("You find carvings that describe the location of the treasure. A guardian spirit appears, testing your resolve.")
    print("Option A: Solve the guardian’s riddle.")
    print("Option B: Attempt to sneak past the guardian.")
    print("Option C: Fight the guardian.")

    choice = input("\nWhat do you choose? (A/B/C): ").strip().upper()
    if choice == 'A':
        update_stamina(-10)
        print("\nYou solve the riddle and the guardian allows you to pass.")
        add_to_inventory('key')
        temple_inner_sanctum()
    elif choice == 'B':
        update_stamina(-20)
        if random.choice([True, False]):
            print("\nYou sneak past successfully, but it was risky.")
            temple_inner_sanctum()
        else:
            print("\nThe guardian catches you and casts you out, reducing your stamina permanently.")
            update_stamina(-10)
            neutral_ending()
    elif choice == 'C':
        update_stamina(-30)
        if stamina > 0:
            print("\nYou defeat the guardian and claim a golden amulet.")
            add_to_inventory('golden amulet')
            temple_inner_sanctum()
        else:
            game_over()
    else:
        print("Invalid choice. Please try again.")
        hidden_cave()

def temple_inner_sanctum():
    clear_screen()
    print("4. The Temple's Inner Sanctum")
    print("You enter a maze-like chamber lined with glowing runes.")
    print("Option A: Follow the left path, which is dimly lit.")
    print("Option B: Take the right path, where you hear faint whispers.")
    print("Option C: Go straight, toward the sound of rushing water.")

    choice = input("\nWhat do you choose? (A/B/C): ").strip().upper()
    if choice == 'A':
        update_stamina(-20)
        if 'torch' in inventory:
            print("\nYou use the torch to avoid quicksand traps and proceed forward.")
            treasure_chamber()
        else:
            print("\nYou fall into quicksand and struggle out, losing more stamina.")
            update_stamina(-20)
            treasure_chamber()
    elif choice == 'B':
        update_stamina(-10)
        if 'key' in inventory:
            print("\nYou use the key to solve a puzzle and proceed forward.")
            treasure_chamber()
        else:
            print("\nYou fail to solve the puzzle and lose stamina.")
            update_stamina(-20)
            treasure_chamber()
    elif choice == 'C':
        update_stamina(-30)
        if 'rope' in inventory or 'golden amulet' in inventory:
            print("\nYou avoid the collapsing floor using your inventory items.")
            treasure_chamber()
        else:
            print("\nThe floor collapses, and you barely make it out alive, losing stamina.")
            update_stamina(-30)
            treasure_chamber()
    else:
        print("Invalid choice. Please try again.")
        temple_inner_sanctum()

def treasure_chamber():
    clear_screen()
    print("5. The Treasure Chamber")
    print("You stand before the treasure, protected by a pedestal with glowing buttons.")
    print("Option A: Press the red button.")
    print("Option B: Press the blue button.")
    print("Option C: Press the green button.")
    print("Option D: Press the yellow button.")

    choice = input("\nWhat do you choose? (A/B/C/D): ").strip().upper()
    if choice == 'A':
        if 'rope' in inventory:
            print("\nThe ceiling collapses, but you escape using the rope.")
            victory_ending()
        else:
            print("\nThe ceiling collapses, and this is the end.")
            game_over()
    elif choice == 'B':
        if 'golden amulet' in inventory:
            print("\nPoisonous darts fly at you, but the amulet protects you.")
            victory_ending()
        else:
            print("\nPoisonous darts hit you. This is the end.")
            game_over()
    elif choice == 'C':
        print("\nThe treasure chamber opens! The treasure is yours!")
        victory_ending()
    elif choice == 'D':
        if 'raft' in inventory:
            print("\nA sudden flood occurs, but you escape using the raft.")
            victory_ending()
        else:
            print("\nA sudden flood traps you. This is the end.")
            game_over()
    else:
        print("Invalid choice. Please try again.")
        treasure_chamber()

def victory_ending():
    print("\nYou claim the legendary treasure of Bowsit! Glory and wealth are yours!")

def neutral_ending():
    print("\nYou survive but fail to retrieve the treasure. You leave the jungle wiser but empty-handed.")

def game_over():
    print("\nYour journey ends in failure. The jungle claims another victim.")

start_game()