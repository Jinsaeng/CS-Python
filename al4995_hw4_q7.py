import random
rand = random.randrange(1,101);
lowerBound = 1;
upperBound = 100;
totalGuesses = 5
guessCount = 0;

print("Range: [",lowerBound, "," , upperBound, "], Number of guesses left: ", (totalGuesses- guessCount));
guess = int(input("Guess a number between 1 and 100: "));

while (guessCount < totalGuesses-1):
    guessCount += 1;
    
    if (rand < guess):
        print("Wrong! My number is smaller");
        upperBound = guess - 1;
        lowerBound = lowerBound
    elif( rand > guess):
        print("Wrong! My number is bigger");
        lowerBound = guess + 1;
        upperBound = upperBound
    else:
        print("Congrats! You guessed my number in ", (guessCount), "guesses.");
    print("")
    print("Range: [", lowerBound, "," , upperBound, "], Number of guesses left: ", (totalGuesses- guessCount));
    guess = int(input("Your guess: "));
print("Out of guesses! My number was ", rand);
