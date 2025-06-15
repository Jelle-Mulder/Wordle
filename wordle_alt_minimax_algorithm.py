import wordle as w
import extractguesseswordle as eg
import copy

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
        feedbacklengths = []

        for code in codelist:
            feedback = w.Wordle(guess, code)
            worstcase[possbfeedbacklists.index(feedback)].append(code)

        feedbackcounter = 0
        for feedback in worstcase: # find size of each feedback
            if len(feedback) != 0:
                feedbackcounter += 1
                feedbacklengths.append(len(feedback))

        if feedbackcounter == 0:
            bestguess = ('solution already found', [], 0)
            break
        
        averagefeedbacksize = sum(feedbacklengths) / feedbackcounter
        worstcase = max(worstcase, key=len)

        if len(codelist) == 1: # if there is only one possible code left, just choose that code as a guess.
            bestguess = (worstcase[0], [], averagefeedbacksize)
            break

        if guesslist.index(guess) == 0:
            bestguess = (guess, worstcase, averagefeedbacksize)

        elif bestguess[2] > averagefeedbacksize:
            print(guess, len(worstcase), averagefeedbacksize)
            bestguess = (guess, worstcase, averagefeedbacksize)

        elif bestguess[2] >= averagefeedbacksize and guess in codelist:
            print(guess, len(worstcase), averagefeedbacksize)
            bestguess = (guess, worstcase, averagefeedbacksize)
    
    print('returned ', bestguess[0], len(bestguess[1]), bestguess[1])
    return bestguess

guesses, codes = eg.listmaker420()




count = 0
known = False
while not known: # do minimax until worst case code is found.
    count += 1

    if count == 1:
        best, worstcase = minimax(guesses, codes)[:2]

    else:
        best, worstcase = minimax(guesses, worstcase)[:2]

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
for code in codes: # find the quality of a starting guess by creating a distribution over how many rounds it takes to win.
    round = 0

    for _ in range(100):
        round += 1

        if round == 1: # use TRACE as first guess, as it was found in minimax algorithm to be the best.
            guess = ['t', 'r', 'a', 'c', 'e']
            currentcodes = codes

        feedback = w.Wordle(guess, code)

        if feedback == ['G', 'G', 'G', 'G', 'G']: # check if we have found answer
            nrofrounds.append(round)
            break

        guesscodes = []

        for othercode in currentcodes: # figure out what codes are left with given feedback
            if w.Wordle(guess, othercode) == feedback:
                guesscodes.append(othercode)

        guess = minimax(guesses, guesscodes)[0] # find next guess

        currentcodes = guesscodes.copy() # update the codes that are left

    
print(nrofrounds)
'''