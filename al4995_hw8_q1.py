import random
def create_permutation(n):
    ls = [];
    while len(ls) < n:
        num = (random.randint(0,n-1))
        if ls.count(num) == 0:
            ls.append(num)
    return ls

def find_word(filename):
    file = open("hw8 - word bank.txt", "r")
    n_word = 0
    ls = []
    for line in file:
        n_word += 1
    rand = random.randint(0,n_word)
    file.seek(0)
    num = 0
    while num<rand:
        word = file.readline()
        num +=1
    return word

def scramble_word(word):
    filename = "hw8 - word bank"
    word = find_word(filename)
    n = len(word)-1
    ls = create_permutation(n)
    mixed = ""
    for i in ls:
        mixed += word[i]
    return (word, mixed)


def main():
    filename = "hw8 - word bank"
    combin = (scramble_word(filename))
    word = combin[0]
    newword = word.replace("\n", "")
    scrambled = combin[1].replace("", "  ")
    trys = 0
    print("Unscramble the word:",scrambled)
    attempt = ""
    while (attempt != newword):
        trys +=1
        print("Try #",trys,":")
        attempt = input()
        if trys == 3:
            break
    if attempt == newword:
        print("Congratuations you've won!")
    else:
        print("Sorry, try again next time! The word was:", newword)
    
main()


