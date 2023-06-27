import nltk
from nltk.corpus import wordnet as wn
import itertools

word = input("Enter a word to check for it's synonyms: ") #word that user wants to guess synonyms for
checkWordList = wn.synonyms(word) #list of nested lists containing synonyms for word
output = list(itertools.chain(*checkWordList)) #flat list of checkWordList
synonymList = list() #list that holds all synonyms guessed correctly by user
continueGuess = True #continues loop to guess synonyms until turned to false

while continueGuess == True: #while user still wants to guess
    synonymGuess = input("Ener a word to check if it is synonymous: ") #user enters word they think is synonymous
    if (synonymGuess in output): #if guess is correct
        synonymList.append(synonymGuess) #add guess to synonymList
        print("That word is a synonym. Here is your current list: ")
    else: #else if guess isn't right
        print("That word isn't a synonym. Here is your current list: ")
    print(synonymList)

    askContinue = input("Do you want to continue (Enter Y or N)?") #asks if user wants to keep guessing
    if (askContinue == 'Y'): #if yes, continue
        continueGuess = True
    elif (askContinue == 'N'): #if not, break
        continueGuess = False
    else: #if anything other than Y or N is entered
        print("Error")


