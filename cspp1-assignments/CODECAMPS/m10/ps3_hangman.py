# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    t=0
    for i in range(0, len(secretWord), 1):
        if secretWord[i] in lettersGuessed:
            t=t+1
        else:
            continue
    if t == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    str1=''
    for i in range(0, len(secretWord), 1):
        if secretWord[i] in lettersGuessed:
            str1+=secretWord[i]
        else:
            str1+='_'
    return str1   



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    r=[]
    str1 = string.ascii_lowercase
    for i in str1:
        if i not in lettersGuessed:
            r.append(i)
        else:
            continue
    return "".join(r)

def testInput(guess):
    if len(guess)>1 or (guess<='a' and guess>='z'):
        print("INVALID INPUT")
        return False
    return True

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("WELCOME!")
    lettersGuessed=[]
    count = 0
    print("I am thinking of a word which is", len(secretWord), "letters")
    print("---------------------------------------")
    flag = False
    maxGuessLetters = len(secretWord) * 2
    print(getGuessedWord(secretWord,lettersGuessed))
    while maxGuessLetters !=0:
        print("You have:", maxGuessLetters,"left")
        print("Available letters: ",getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter:")
        maxGuessLetters -=1

        if not testInput(guess):
            continue
        lettersGuessed.append(guess)
        flag = isWordGuessed(secretWord, lettersGuessed)
        if flag:
            break
        print(getGuessedWord(secretWord, lettersGuessed))
    if flag:
        print("CONGRATS U GUESSED THE RIGHT WORD")
    print("TRY AGAIN")






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
