import random

print("H A N G M A N")
pick = list(random.choice(['python', 'java', 'kotlin', 'javascript']))
fill = list("-" * len(pick))
guesses = []
attempts = 8
while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "play":
        while attempts > 0:
            entry = input(f"\n{''.join(fill)}\nInput a letter: ")
            if len(entry) != 1:
                print("You should input a single letter")
                guesses.append(entry)
            elif not entry.islower() or not entry.isalpha():
                print("Please enter a lowercase English letter")
                guesses.append(entry)
            elif entry in fill or entry in guesses:
                print("You've already guessed this letter")
            elif entry in pick:
                for x in range(len(pick)):
                    if entry == pick[x]:
                        fill[x] = entry
                        if "-" not in fill:
                            print("You guesses the word!\nYou survived!")
                            exit()
            else:
                print("That letter doesn't appear in the word")
                guesses.append(entry)
                attempts -= 1
                if attempts == 0:
                    print("You lost!")
    elif menu == "exit":
        exit()
