# Hangman Game
# Danson Coats
# 10/20
# The classic game of Hangman.  The computer picks a random word
# and the player wrong to guess it, one letter at a time.  If the player
# can't guess the word in time, the little stick figure gets hanged.

#imports
import random

HANGMAN = (
"""
 ------
 |   |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 |  -+-
 |   +
 |
 |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 | /-+-
 |   +
 |
 |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 | /-+-\\
 |   +
 |
 |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 | /-+-\\
 |   +
 |  |
 |  |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 | /-+-\\
 |   +
 |  | |
 |  | |
 |
 |
----------
""",
"""
 ------
 |   |
 |   O
 | /-+-\\
 |   +
 |  | |
 |  | |
 |~-
 |
----------
""",
"""
 ------
 |   |
 |   O
 | /-+-\\
 |   +
 |  | |
 |  | |
 |~-   -~
 |
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("PRINT", "FOR", "WHILE", "SYNTAX", "PYTHON", "ENTER", "INPUT", "IDLE", "BOOLEAN", "FLOAT" )
DEFINITION = ("prints the specified message to the screen",
              "repeats a block of code a fixed number of times",
              "used to execute a block of statements repeatedly until a given condition is satisfied",
              "set of rules that defines how a Python program will be written and interpreted",
              "interpreted, object-oriented, high-level programming language with dynamic semantics",
              "takes you to the next line",
              "lets you ask the user for some text input",
              "Python's Integrated Development and Learning Environment",
              "true or flase statements"
              "represent real numbers and are written with a decimal point dividing the integer and fractional parts")
              
word=random.choice(WORDS)
index=WORDS.index(word)
#assignment
#10 python related terms
#be sure to define terms in comments
wrong = 0
used = []
so_far = "-"*len(word)

print("Welcome to Hangman.  Good luck!")

while wrong < MAX_WRONG and so_far != word:

    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n",used)
    print("\nSo far, the word is:\n",so_far)
    if wrong==3:
        print("Hint: ")
        print(DEFINITION[index])

    guess=input("\n\nEnter your guess: ")
    guess=guess.upper()
    print(guess)

    while guess in used:
        print("You've already guessed the letter",guess)
        guess=input("Enter your guess: ")
        guess=guess.upper()


    used.append(guess)

    if guess in word:
        print("\nYes!",guess,"is in the word!")

        #create a new so_far to include guess in the loop
        new=""
        for i in range(len(word)):
            if guess==word[i]:
                new+=guess
            else:
                new+=so_far[i]
        so_far=new
   
    else:
        print("\nSorry,",guess,"isn't in the word.")
        wrong+=1

if wrong==MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou Lose!")
else:
    print("\nYou guessed it!")

print("\nThe word was",word)

input("\n\nPress the enter key to exit")














#option 1
##index = random.randint(0,len(WORDS)-1)
##word = WORDS[index]
##print(word)
##x = 0
##while x < len(HANGMAN):
##    print(HANGMAN[x])
##    input()
##    x+=1




