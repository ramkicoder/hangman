import random

def random_line(fname):
    '''
    read() reads the whole file
    splitlines() splits it into a list based on newline and returns list - neat!
    random.choice() picks a random element of list - no need to give range etc.
    '''
    '''
    below logic is better
    use file handle f to read a line (for line in f)
    use the second for to split - for word in line.split
    in the iterator, the first for loop should be followed by the second
    '''
    with open(fname) as f:
        flat_list=[word for line in f for word in line.split()]

    #lines = open(fname).read().splitlines()
    return random.choice(flat_list)

maxtries = 7

def play(word):
    tries = 0
    guessedChars = ''
    showString = "-" * len(word)
    while tries < maxtries:
        print("Word so far: ", showString)
        print("Guessed so far: ", ''.join(sorted(guessedChars)))
        guess = input("Guess char:").strip()
        if guess in guessedChars:
            print("Already guessed!")
            continue
        if guess in word:
            '''
            inefficient way to update showString
            '''
            for i in range(len(word)):
                if word[i] == guess:
                    #showString[i] = guess #won't work as strings are immutable
                    #rebuild the showString - replace only the - at the matching pos with guess
                    showString = showString[:i] + guess + showString[i + 1:]
        else:
            print("Wrong guess, try again")
            tries += 1
        guessedChars += guess
        if '-' not in showString:
            print("Great! You got the word {}".format(word))
            break
    if (tries == maxtries):
        print("Sorry you missed it. The word was {}".format(word))


#main
word = random_line("words.txt")
#print("Word is: ", word)
play(word)


