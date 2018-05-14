import random

words = ["fortnite","dog","bird","school"]

hint1 = ["popular game","common pet","they can fly","a place where you take the bus to get to"]
hint2 = ["a battle royale game","not a cat","they are usually small","you take classes here"]

number = random.randint(0,3)

secretword = words[number]

guess = ""

counter = 0

while True:
    print("guess the secret word")
    print("type, 'hint1', 'hint1', 'first letter', 'last letter', or 'give up' for help")
    guess  = input()
    counter += 1

    if guess == secretword:
        print("You Win! it took you " + str(counter) + " Guesses.")
        break
    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "first letter":
        print( secretword[0])

    elif guess == "last letter":
         print (secretword[0-1])

    elif guess == "give up":
        print("The word was" + secretword)
        break
