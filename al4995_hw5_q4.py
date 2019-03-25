string = input("Enter a word: ")
vowel = 0
consonant = 0
word = string.lower()
for i in range(0,len(word)):
    if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
        vowel += 1
    else:
        consonant += 1
print(word, "has", vowel, "vowels and", consonant, "consonants")

