import wordle as w
import extractguesseswordle as eg
import copy

### mini-max ###
n = 5 # code length # n=5 told me it might be going over some possibilities multiple times. does it not reset possiblecodes?
k = 26 # size of alphabet

alphabet = ['abcdefghijklmnopqrstuvwxyz'[i] for i in range(k)] # alphabet

possbfeedbacklists = []
basecase = ['' for _ in range(5)]
order = ['', 'G', 'Y']

for i in range(1, 3 ** n + 1):
    for j in range(n):
        if i % (3 ** j) == 0:
            basecase[j] = order[(order.index(basecase[j]) + 1) % 3]

    possbfeedbacklists.append(copy.deepcopy(basecase))

# print(possbfeedbacklists)

def minimax(guesslist, codelist):
    for guess in guesslist:
        # print(guess)

        worstcase = [[] for _ in range(3 ** 5)]

        for code in codelist:
            feedback = w.Wordle(guess, code)
            worstcase[possbfeedbacklists.index(feedback)].append(code)

        worstcase = max(worstcase, key=len)

        if len(codelist) == 1: # if there is only one possible code left, just choose that code as a guess.
            bestguess = (worstcase[0], [])
            break

        if guesslist.index(guess) == 0:
            bestguess = (guess, worstcase)

        elif len(bestguess[1]) > len(worstcase):
            # print(guess, len(worstcase))
            bestguess = (guess, worstcase)
    
    # print('returned ', bestguess[0], len(bestguess[1]), bestguess[1])
    return bestguess

def distribution(guess, codelist, n=n):
    possbfeedbacklists = []
    distribution = []

    for i in range(n+1):
        possbfeedbacklists.append([])
        for j in range(n+1-i):
            possbfeedbacklists[i].append([])
    
    for code in codelist:
        (a, b) = w.Wordle(guess, code, n)
        possbfeedbacklists[b][a].append(code)

    for i in range(n+1):
        for j in range(n+1-i):
            distribution.append('n(' + i * 'B' + j * 'W' + (n - j - i) * '_' + ') = ' + str(len(possbfeedbacklists[i][j])))
    
    return distribution


guesses, codes = eg.listmaker420()



count = 0
known = False
while not known: # do minimax until worst case code is found
    count += 1

    if count == 1:
        best, worstcase = minimax(guesses, codes)

    else:
        best, worstcase = minimax(guesses, worstcase)

    print(best, len(worstcase))
    
    if worstcase == []:
        known = True


'''
        
known = False
while not known: # interactive minimax alg where you can choose own guesses.

    guess = input('enter your guess: ')
    feedback = input('enter your feedback: ')

    guess = [guess[i] for i in range(n)]
    feedback = [feedback[i] for i in range(n)]
    
    while 'X' in feedback:
        feedback[feedback.index('X')] = ''

    guesscodes = []

    for code in codes:
        if w.Wordle(guess, code) == feedback:
            guesscodes.append(code)

    thing = minimax([guess], guesscodes)[1]

    if thing == []:
        known = True

    print('your next guess is being calculated...')
    minimax(guesses, thing)
    codes = guesscodes.copy()



nrofrounds = []
for code in codes: # find the quality of a starting guess
    round = 0

    for _ in range(100):
        round += 1

        if round == 1: # use TRACE as first guess, as it was found in minimax algorithm to be the best.
            guess = ['t', 'r', 'a', 'c', 'e']
            currentcodes = codes

        feedback = w.Wordle(guess, code)

        if feedback == ['G', 'G', 'G', 'G', 'G']: # check if we have found answer
            nrofrounds.append(round)
            print(round)
            break

        guesscodes = []

        for othercode in currentcodes: # figure out what codes are left with given feedback
            if w.Wordle(guess, othercode) == feedback:
                guesscodes.append(othercode)

        guess = minimax(guesses, guesscodes)[0] # find next guess

        currentcodes = guesscodes.copy() # update the codes that are left


print(nrofrounds)

'''