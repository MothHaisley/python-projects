print("Hello! Type all responses in lower case, single word responses.")
print("Have fun, and all correct responses will be given at the end.")
intro_q = input("Are you excited? yes/no: ")

if intro_q == "yes":
    print("Yay! Let me know what you think.")
else:
    print(":(")

print("I will be your friendly guide, CERA!")
print(
    """CERA stands for
Certified
Educated
Ritual
Assistant."""
)
print("I am here to help you not get eaten by Cthulhu during your trial.")
print("Oh, look at me rambling on. Let's start with your name.")

player_name = input("Please tell me who you are: ")
print(f"Hello, {player_name}!")

print(
    """Now, we better get started! In case you forgot, you are responsible
for summoning our Lord God, Divine Horrorterror Chutulhu! I'm so happy
for you having this honor! There are a series of 6 steps that need to be followed,
and if you mess a single one up, Cthulhu will refuse to incarnate,
and the Facility will release the hounds. You don't want that.
You should have been given a blood-covered leather necronomicon, which
will have all the instructions. What, mugged? By a child? Oh well,
I'm sure you got this!"""
)

q0 = input("Now, do you remember the first step? yes/no: ")

if q0 == "yes":
    print("Good! Here I was worrying for nothing.")
elif q0 == "no":
    print(
        """Well, I believe in you! I'm just going to back up my program to
the cloud really quickly, don't mind me."""
    )

# Step 1: Loop to ensure correct input
while True:
    print("What's the first step?")
    print("a. Sacrifice")
    print("b. Blood Letting")
    print("c. Let Me Go")
    print("d. Chalk Lines")

    q_1 = input("What is the first step? a/b/c/d: ").strip().lower()

    if q_1 == "a":
        print("Early for that!")
    elif q_1 == "b":
        print("Good thought, but not yet!")
    elif q_1 == "c":
        print("...")
    elif q_1 == "d":
        print("Good Job!")
        break  # Exit loop on correct answer
    else:
        print("Invalid choice! Please select a, b, c, or d.")
        print("You Died! Try again.\n")

# Step 2
while True:
    print("Those lines look great! Now for Step 2.")
    print("a. Sacrifice?")
    print("b. Blood Letting")
    print("c. Please Let Me Go")
    print("d. *$#*")

    q_2 = input("Please select Step 2. a/b/c/d: ").strip().lower()

    if q_2 == "a":
        print("Still not yet.")
    elif q_2 == "b":
        print(
            """Yes! Good Job! You have to fill up the bowl and place it
in the chalk lines."""
        )
        break
    elif q_2 == "c":
        print("....")
    elif q_2 == "d":
        print("%&@#^*!")
    else:
        print("Invalid choice! Please select a, b, c, or d.")

print("You're doing good so far!")

# Step 3
print("Now on to Step 3!")
while True:
    print("")
    print("a. No.")
    print("b. I have a family.")
    print("c. Please.")
    print("d. ...")

    q_3 = input("Please select Step 3. a/b/c/d: ").strip().lower()

    if q_3 == "a":
        print("You don't get a choice.")
    elif q_3 == "b":
        print("You think I don't-")
        break
    elif q_3 == "c":
        print("No.")
    elif q_3 == "d":
        print("i cant help you")
    else:
        print("Invalid choice! Please select a, b, c, or d.")

print("I am getting word that the worlds oceans are turning to blood!")
print("You are getting closer, keep going!")

#Step 4
print("Now on to Step 4!")
while True:
    print("")
    print("a. Sacrifice")
    print("b. Sacrifice")
    print("c. Sacrifice")
    print("d. Sacrifice")

    q_4 = input("Please select Step 4. a/b/c/d: ").strip().lower()

    if q_4 == "a":
        print("Yay!")
    elif q_4 == "b":
        print("Good Job!")
        break
    elif q_4 == "c":
        print("Who?")
    elif q_4 == "d":
        print("No no nonono")
    else:
        print("Invalid choice! Please select a, b, c, or d.")

print("Why does it have to be my daughter?")
