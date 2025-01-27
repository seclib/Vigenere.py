
def createAlphabet(key1string):

    topAlphabet = alphabet
    counter = 0

    for letter in key1string:

        topAlphabet.remove(letter)

        topAlphabet.insert(counter, letter)

        counter += 1

    return topAlphabet

def createLines(key2string, myAlphabet):

    listOfAlphabets = []

    for letter in key2string:

        index = myAlphabet.index(letter)+1

        counter = 0

        lineAlphabet = []

        while counter <= 25:
            lineAlphabet.append(myAlphabet[index % len(myAlphabet)])
            index += 1
            counter += 1

        listOfAlphabets.append(lineAlphabet)

    return listOfAlphabets

def decryptPassage(passage, myAlphabet, myLines, key2string):

    decryptedPassage = []

    counter = 0

    for letter in passage:

        ourRow = myLines[counter]

        index = ourRow.index(letter) + 1

        decLetter = myAlphabet[index]

        decryptedPassage.append(decLetter)

        if counter < len(key2string)-1:
            counter += 1
        else:
            counter = 0

    return decryptedPassage


def encryptPassage(passage, myAlphabet, myLines, key2string):

    encryptedPassage = []

    counter = 0

    for letter in passage:

        index = myAlphabet.index(letter) - 1

        ourRow = myLines[counter]

        encLetter = ourRow[index]

        encryptedPassage.append(encLetter)

        if counter < len(key2string) - 1:
            counter += 1
        else:
            counter = 0

    return encryptedPassage


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


choiceOfRun = ''

while choiceOfRun != "A" or "B" or "Q":

    choiceOfRun = input("Do you want to: A) Encrypt a passage. B) Decrypt a passage. Q) Quit program [A/B/Q]?").upper()

    if choiceOfRun == "A":

        # Encryption
        key1stringenc = input("Enter first key: ")
        key1stringenc = key1stringenc.lower().replace(" ", "")

        myAlphabet = createAlphabet(key1stringenc)

        myAlphabetString = ''.join(myAlphabet)

        print("Your alphabet line is: " + myAlphabetString)

        key2stringenc = input("Enter second key: ")
        key2stringenc = key2stringenc.lower().replace(" ", "")

        myLines = createLines(key2stringenc, myAlphabet)

        for line in myLines:

            lineSting = ''.join(line)
            print("Your lines are: " + lineSting)

        passageInput = input("Enter passage you wish to encrypt: ")
        passageInput = passageInput.lower().replace(" ", "")

        encryptedPassage = encryptPassage(passageInput, myAlphabet, myLines, key2stringenc)

        encryptedPassageString = ''.join(encryptedPassage)

        print("Your encrypted passage is: " + encryptedPassageString)

        choiceOfRun = ''

        continue

    if choiceOfRun == "B":
        # Decryption
        key1string = input("Enter first key: ")
        key1string = key1string.lower().replace(" ", "")

        myAlphabet = createAlphabet(key1string)

        myAlphabetString = ''.join(myAlphabet)

        print("Your alphabet line is: " + myAlphabetString)

        key2string = input("Enter second key: ")
        key2string = key2string.lower().replace(" ", "")

        myLines = createLines(key2string, myAlphabet)

        for line in myLines:

            lineSting = ''.join(line)
            print("Your lines are: " + lineSting)

        encryptedPassageInput = input("Enter passage you wish to decrypt: ")
        encryptedPassageInput = encryptedPassageInput.lower().replace(" ", "")

        decryptedPassage = decryptPassage(encryptedPassageInput, myAlphabet, myLines, key2string)

        decryptedPassageString = ''.join(decryptedPassage)

        print("Your decrypted passage is: " + decryptedPassageString)

        choiceOfRun = ''

        continue

    if choiceOfRun == "Q":
        break

