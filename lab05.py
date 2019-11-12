# Brett Roach
# 6907380

def createWordList(filename):
    # creates a list of words from the wordlist.txt file
    wl = open(filename, "r")
    wordList = wl.readlines()
    wl.close()
    for x in range(len(wordList)):
        wordList[x] = wordList[x][0:(len(wordList[x])-1)]
    return wordList

def canWeMakeIt(myWord, myLetters):
    # given a word and a sample of letters, if the letters can form the word
    # returns True, if not returns False
    if type(myWord) !=str or type(myLetters) != str:
        return False
    else:
        for letter in myWord:
            if letter not in myLetters:
                return False
            elif myWord.count(letter) > myLetters.count(letter):
                return False
        else:
            return True

def getWordPoints(myWord, letterPoints):
    # from word, gets the value of each letter from a dictionary
    # adds them all up
    if type(myWord) != str or type(letterPoints) != dict:
        return 0
    else:
        pointTotal = 0
        for letter in myWord:
            if letter in letterPoints:
                pointTotal += letterPoints.get(letter)
        return pointTotal

def outputWordPointPairs(pointWordList, myLetters, toFile):
    # either prints a list of words and their point totals
    # or writes it into a text document
    if toFile == False:
        for item in pointWordList:
            fillers = (item[1]+(" "*(len(myLetters)-len(item[1]))), item[0])
            print("%s    %s" % fillers)
    elif toFile == True:
        myL = open(myLetters+".txt", "x")
        for item in pointWordList:
            fillers = (item[1]+(" "*(len(myLetters)-len(item[1]))), item[0])
            myL.write("%s    %s\n" % fillers)
        myL.close()

from string import ascii_lowercase

def scrabbleWords(myLetters):
    wordList = createWordList("wordlist.txt")
    myWords = list()
    for word in wordList:
        if canWeMakeIt(word, myLetters) == True:
            myWords.append(word)
    letterPoints = dict.fromkeys(ascii_lowercase)
    values = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
    for i in range(len(ascii_lowercase)):
        letterPoints[ascii_lowercase[i]] = values[i]
    pointWordList = list()
    for word in myWords:
        pointValue = getWordPoints(word, letterPoints)
        pointWordList.append((pointValue, word))
    list.sort(pointWordList, reverse=True)
    outputWordPointPairs(pointWordList, myLetters, False)
    outputWordPointPairs(pointWordList, myLetters, True)




