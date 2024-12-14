def start_game():
    # Expanded introduction with more background
    print("You awaken in a dimly lit chamber, surrounded by shadows that seem to shift and move like the depths of an ocean. The air is thick with an unnameable dread, a mix of decay and something far older, far more sinister. The flicker of candles casts elongated, monstrous shadows across the walls, revealing symbols that pulse with an alien energy. This is not your ordinary room—this is a place steeped in forbidden knowledge, a threshold between worlds.")

    # Asking for the player's name
    player_name = input("Enter your name to begin this dark journey: ")

    # Adding a personalized touch with the player's GitHub profile
    github_profile = "https://github.com/MothHaisley"

    print(f"\nWelcome, {player_name}. Your chosen name will echo in the ears of the eldritch beings that reside here...")
    print("You are here because a secretive government agency has summoned you to perform an arcane task...")
    print(f"Your mission is to summon the eldritch horror known as Cthulhu. But first, you need to prove your arcane worth...\n")
    print(f"My GitHub profile, where all my dark musings and cryptic code await, can be found at: {github_profile}")
    print("\nGather your courage, young initiate, for the challenges ahead...\n")

    task = 1
    failure = False

    while task <= 5:
        if failure:
            print("You stumble through the complexities of the arcane once more...\n")
            failure = False

        if task == 1:
            if task_1(player_name):
                task += 1
            else:
                failure = True
        elif task == 2:
            if task_2(player_name):
                task += 1
            else:
                failure = True
        elif task == 3:
            if task_3(player_name):
                task += 1
            else:
                failure = True
        elif task == 4:
            if task_4(player_name):
                task += 1
            else:
                failure = True
        elif task == 5:
            success = task_5(player_name)
            if success:
                break

def task_1(player_name):
    print(f"Step 1: Gather the Proper Implements, {player_name}...\n")

    choice = input("Select an item:\n1. A vellum scroll inscribed with non-Euclidean geometry\n2. A vial of cosmic ichor\n3. An ancient tome titled 'The Esoteric Essence of Madness'\n")

    if choice == "1":
        print("A vellum scroll inscribed with non-Euclidean geometry... an excellent choice! The cryptic figure nods approvingly, 'A touch of eldritch sophistication.'\n")
        question_1(player_name)
        return True
    elif choice == "2":
        print("A vial of cosmic ichor... not a bad choice, though perhaps a bit too messy for summoning. The cryptic figure raises an eyebrow, 'Quite the visceral option.'\n")
        question_1(player_name)
        return False
    elif choice == "3":
        print("An ancient tome titled 'The Esoteric Essence of Madness'... a classic choice, but it might be a bit too mainstream for Cthulhu's tastes. The cryptic figure rolls their eyes, 'It's been done.'\n")
        question_1(player_name)
        return False
    else:
        print("You fumble, grabbing a mundane item instead. The cryptic figure sighs, 'Not quite what we had in mind.'\n")
        question_1(player_name)
        return False

def task_2(player_name):
    print(f"Step 2: Decipher the Arcane Script, {player_name}...\n")

    choice = input("Decode: 'Nyarlathotep' (Hint: It's not just a name)\n")
    if choice.lower() == "which book is lost in the sea of madness?":
        print(f"Correct! The arcane script is deciphered. The cryptic figure grins, 'You've got a sharp mind, {player_name}.'\n")
        question_2(player_name)
        return True
    else:
        print("Incorrect! The answer you gave would have likely summoned a garden gnome, not Nyarlathotep.\n")
        give_hint(2)
        return False

def task_3(player_name):
    print(f"Step 3: Answer a Mythos Query, {player_name}...\n")

    question = "Where was Cthulhu last seen?\n1. Innsmouth\n2. R'lyeh\n3. Dunwich\n"
    choice = input(question)
    if choice == "2":
        print(f"Correct! You possess a refined grasp of the mythos, {player_name}.\n")
        question_3(player_name)
        return True
    else:
        print("Alas, Cthulhu was indeed last seen in R'lyeh, not on a vacation in Dunwich.\n")
        give_hint(3)
        return False

def task_4(player_name):
    print(f"Step 4: Confront the Guardian, {player_name}...\n")

    choice = input("Choose the correct path:\n1. Through the maze of star-twined tapestries\n2. Face the wrath of the spectral librarian\n")
    if choice == "1":
        print("Correct! You deftly navigate the guardian's wrath.\n")
        question_4(player_name)
        return True
    else:
        print("The librarian snarls, 'You're a little too late with that decision.'\n")
        give_hint(4)
        return False

def task_5(player_name):
    print(f"Step 5: The Final Conjuring, {player_name}...\n")

    choice = input("How will you summon Cthulhu?\n1. Swift and no-nonsense\n2. With ritualistic pomp and circumstance\n")
    if choice == "2":
        print("You summon Cthulhu with all the flair and formality befitting a master of the arcane. The oceans are turning red as the air thickens with an eldritch presence. World End, You Win!\n")
        return True
    else:
        print("Cthulhu appears but is unimpressed with your hurried efforts. The air grows colder, and the shadows deepen. Game over.\n")
        give_hint(5)
        return False

# Hint system
def give_hint(task):
    hints = {
        1: "Choosing the right item is key! Remember, Cthulhu appreciates the esoteric.",
        2: "The answer involves a book lost in the depths of madness. Think metaphorically.",
        3: "Consider Cthulhu's last known whereabouts. R'lyeh isn't just a myth, you know.",
        4: "The maze or the librarian? One is definitely more cryptic, the other more confrontational.",
        5: "Cthulhu appreciates the dramatic. Take your time to invoke the proper rituals."
    }
    print(f"Hint: {hints[task]}\n")

def question_1(player_name):
    print(f"\nBetween tasks, the cryptic figure beckons you closer, 'So, {player_name}, what drew you to this eldritch path?'")
    question = input("Choose your response:\n1. 'I seek power and knowledge, no matter the cost.'\n2. 'Curiosity is a cruel mistress.'\n3. 'The fear of the unknown pushes me forward.'\n")
    if question == "1":
        print("The figure nods, 'A bold choice, indeed. But beware of the price of such power.'\n")
    elif question == "2":
        print("The figure smiles, 'Curiosity can be a dangerous path, but sometimes it's worth the risk.'\n")
    elif question == "3":
        print("The figure chuckles, 'Ah, the fear of the unknown. An appropriate choice for one about to summon Cthulhu.'\n")
    else:
        print("The figure sighs, 'A vague choice, but we’ll take it...'\n")

def question_2(player_name):
    print(f"\nAfter overcoming the second challenge, the cryptic figure asks, 'Do you believe that knowledge is power, {player_name}, or just a path to madness?'")
    question = input("Choose your response:\n1. 'Knowledge is power, but it can drive one to madness.'\n2. 'Knowledge is a path to madness, but one must walk it willingly.'\n3. 'Both knowledge and madness are intertwined.'\n")
    if question == "1":
        print("The figure nods approvingly, 'A pragmatic view. Knowledge is indeed power, but the road can be treacherous.'\n")
    elif question == "2":
        print("The figure grins, 'A path to madness, but willingly chosen? You have a dark wisdom about you, {player_name}.'\n")
    elif question == "3":
        print("The figure laughs, 'A balance of power and madness, a dangerous harmony. A wise choice indeed.'\n")
    else:
        print("The figure shrugs, 'An interesting but vague answer.'\n")

def question_3(player_name):
    print(f"\nAfter the third task, the figure asks, 'Why do you seek Cthulhu, {player_name}?'")
    question = input("Choose your response:\n1. 'I seek to control the unknown.'\n2. 'I want to understand the mysteries of the cosmos.'\n3. 'I seek an end to my own madness.'\n")
    if question == "1":
        print("The figure smiles, 'Control over the unknown, a powerful ambition. But beware of the cost.'\n")
    elif question == "2":
        print("The figure nods, 'To understand the mysteries is a noble quest, but it comes at a price.'\n")
    elif question == "3":
        print("The figure looks at you thoughtfully, 'An end to your madness? A dark choice, but one that may lead you to the truth.'\n")
    else:
        print("The figure looks unimpressed, 'A vague answer, but we’ll take it.'\n")

def question_4(player_name):
    print(f"\nAfter confronting the guardian, the figure asks, 'What do you hope to gain from summoning Cthulhu, {player_name}?'")
    question = input("Choose your response:\n1. 'Power beyond comprehension.'\n2. 'The truth hidden from mortal eyes.'\n3. 'An escape from my reality.'\n")
    if question == "1":
        print("The figure chuckles, 'Power beyond comprehension, a tempting prospect indeed.'\n")
    elif question == "2":
        print("The figure grins, 'The truth is a dangerous ally, but a worthy goal.'\n")
    elif question == "3":
        print("The figure raises an eyebrow, 'An escape from reality? A desire for release from the mundane.'\n")
    else:
        print("The figure shakes their head, 'Vague responses won’t get you far here.'\n")

def question_5(player_name):
    print(f"\nThe final challenge approaches, and the figure asks, 'What will you do once Cthulhu is summoned, {player_name}?'")
    question = input("Choose your response:\n1. 'Control it.'\n2. 'Learn from it.'\n3. 'Survive it.'\n")
    if question == "1":
        print("The figure laughs, 'Control is a dangerous ambition, but not one without its rewards.'\n")
    elif question == "2":
        print("The figure nods, 'Learning from Cthulhu would certainly be enlightening... if you survive.'\n")
    elif question == "3":
        print("The figure smirks, 'Survival is a commendable choice. But not an easy one.'\n")
    else:
        print("The figure frowns, 'We’re not looking for vague answers, {player_name}.'\n")

# Start the game
start_game()
