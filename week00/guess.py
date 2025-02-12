def guess():
    guess = int(input("Enter a Guess: "))
    return guess

def main():
    guessme = guess()
    if guessme == 1337:
        print("Correct!")
    else:
        print("Incorrect!")

main()
