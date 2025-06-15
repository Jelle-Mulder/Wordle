
def listmaker420():
    guesses = []
    codes = []

    with open('answers.txt') as f:
        for line in f:
            lines = line.strip()
            word = []
            for letter in lines:
                word.append(letter)

            codes.append(word)


    with open('allowed.txt') as f:
        for line in f:
            lines = line.strip()
            word = []
            for letter in lines:
                word.append(letter)

            guesses.append(word)

    return (guesses, codes)