# Brett Roach
# 6907380

from lab05 import createWordList

def test_createWordList_1():
    testWords = ["cheesecake"]
    outfile = open("test_file_1.txt", "x")
    for word in testWords:
        outfile.write(word+"\n")
    outfile.close()
    testList = createWordList("test_file_1.txt")
    assert len(testList) == len(testWords)
    for i in range(len(testWords)):
        assert testWords[i] == testList[i]

def test_createWordList_2():
    testWords = ["cheesecake", "grill", "minecraft"]
    outfile = open("test_file_2.txt", "x")
    for word in testWords:
        outfile.write(word+"\n")
    outfile.close()
    testList = createWordList("test_file_2.txt")
    assert len(testList) == len(testWords)
    for i in range(len(testWords)):
        assert testWords[i] == testList[i]

def test_createWordList_3():
    testWords = []
    outfile = open("test_file_3.txt", "x")
    for word in testWords:
        outfile.write(word+"\n")
    outfile.close()
    testList = createWordList("test_file_3.txt")
    assert len(testList) == len(testWords)
    for i in range(len(testWords)):
        assert testWords[i] == testList[i]

from lab05 import canWeMakeIt

def test_canWeMakeIt_1():
    assert canWeMakeIt("sodapop", "asdpoop") == True

def test_canWeMakeIt_2():
    assert canWeMakeIt(45, "asdo") == False

def test_canWeMakeIt_3():
    assert canWeMakeIt("soda", ["a", "s", "d", "o"]) == False

def test_canWeMakeIt_4():
    assert canWeMakeIt("sodapop", "adpoop") == False

def test_canWeMakeIt_5():
    assert canWeMakeIt("sodapop", "asdpoo") == False

from lab05 import getWordPoints
letterPoints = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4,\
		'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1,\
		'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,\
		's':1, 't':1, 'u':1, 'v':4,	'w':4, 'x':8,\
		'y':4, 'z':10}

def test_getWordPoints_1():
    assert getWordPoints("soda", letterPoints) == 5

def test_getWordPoints_2():
    assert getWordPoints(45, letterPoints) == 0

def test_getWordPoints_3():
    pointsList = [1, 1, 2, 1]
    assert getWordPoints("soda", pointsList) == 0
