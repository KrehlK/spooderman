import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

hyper = "hypernym"
hypo = "hyponym"

word = input("Enter a word of your choice: ") # lets user input selected word
print("You have selected the word " + "\"" + word + "\"")
firstSynset = wn.synsets(word)[0] # get the first synset of the complete list of synsets for the word inputted

hyp = input("Hypernym or Hyponym? ") # ask if the user wants to find the hypernym or hyponyms of their word

if (hyp == hyper):
    print("You have chosen to find the hypernym(s) of the word " + "\"" + word + "\"")
    print(firstSynset.hypernyms()) # return a synset of hypernyms
elif(hyp == hypo):
    print("You have chosen to find the hyponym(s) of the word " + "\"" + word + "\"")
    print(firstSynset.hyponyms()) # return a synset of hyponyms
