def first_word(phrase):
    first = phrase.find(" ");
    word = phrase[0 : first]
    return word

def rest_of_it(phrase):
    first = phrase.find(" ");
    rest = phrase[first + 1:]
    return rest

def reverse_string(phrase):
    first = 0
    newstring2 = ""
    word1 = first_word(phrase)
    while phrase.find(" ") != -1:
        first = phrase.find(" ");
        word = phrase[0: first+1]
        rest = rest_of_it(phrase)
        phrase = rest
        newstring = word
        newstring3 = newstring + newstring2
        newstring2 = newstring3
    newstring2 = rest + " " + newstring3
    return newstring2

def main():
    phrase = input("Enter a string: ")
    print(reverse_string(phrase))
