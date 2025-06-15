def Wordle(guess, code, alphabet=['abcdefghijklmnopqrstuvwxyz'[i] for i in range(26)], n=5): # return feedback
    codecopy = code.copy()
    if len(guess) != n: # check if guess is right length
        raise Exception('your guess needs to be length ' + str(n))
        
    answer = ['' for _ in range(n)]

    for i in range(n): # set greens
        if guess[i] == codecopy[i]:
            answer[i] = 'G'
            codecopy[i] = ''
    
    for i in range(n): # set yellows
        if answer[i] != 'G' and guess[i] in codecopy and min(codecopy.count(guess[i]), guess.count(guess[i])) > 0:
            answer[i] = 'Y'
            codecopy[codecopy.index(guess[i])] = ''
            

    return(answer)