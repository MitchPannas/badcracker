import random, time

try:
    pwordfile = open("password.txt", "r")  # opens file with name of "test.txt"
    my_secret_password = str.strip(pwordfile.readline())
except FileNotFoundError:
    print("[!] That file does not exist. [!]")


def passwordfilecheck():
    try:
        wordlistfile = open("wordlist.txt", "r")  # opens file with name of "test.txt"
    except FileNotFoundError:
        print("[!] That file does not exist. [!]")
    for x in wordlistfile:
        if str.strip(x) == my_secret_password:
            print("Ladies and Gentleman we got him.. {}".format(x))
            break


def openfile():
    try:
        wordlistfile = open("wordlist.txt", "r")  # opens file with name of "test.txt"
    except FileNotFoundError:
        print("[!] That file does not exist. [!]")

    return wordlistfile


def randompasscheck():
    wordlist = openfile().readlines()
    howlong = len(wordlist)
    indextochoose = random.randrange(1, howlong)

    password = str.strip(wordlist[indextochoose])
    print("The password is: {}".format(password))
    counter = 0
    for x in openfile():
        counter += 1
        if str.strip(x) == password:
            print("[!] Found: {} at {}".format(str.strip(x), counter))
            break

while True:
    try:
        randompasscheck()
        time.sleep(0.1)
    except KeyboardInterrupt:
        exit(0)
