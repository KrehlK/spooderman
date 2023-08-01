import nltk
import gzip
import json, tarfile, io
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from hugchat import hugchat
from hugchat.login import Login

file = open('nounAnimal.txt', 'r', encoding='unicode_escape', errors='ignore')
content = file.read()

# login
sign = Login('estherfshue@gmail.com', 'uXB^-vMw+.c3p-5')
cookies = sign.login()
sign.saveCookiesToDir('Users\meich\AppData\Local\Microsoft\Windows\INetCookies')

# load cookies from usercookies/<email>.json
sign = Login('estherfshue@gmail.com', None)
cookies = sign.loadCookiesFromDir('Users\meich\AppData\Local\Microsoft\Windows\INetCookies') # This will detect if the JSON file exists, return cookies if it does and raise an Exception if it's not.

word = input("Enter a word of your choice: ") # Lets user input selected word

hypoList = ""

# Add only the lemmas from each synset to a string
for synset in wn.synsets(word):
    for lemma in synset.lemmas():
        hypoList += lemma.name() + ", "

print("The hyponyms of " + word + " are: " + hypoList) # Returns a list of hyponyms of the selected word

print("Enter three words of your choice from the previous list and I will try to guess the word you first chose!")
# User inputs three words selected from hypoList
first = input("First word: ")
second = input("Second word: ")
third = input("Third word: ")

wordList = first + ", " + second + ", " + third
print("Here are the words you have chosen: " + wordList) # Returns a complete list of the user selected words

# Query for the ChatBot
#query = "Guess the root hypernym of the words " + wordList + " and give me 5 possible answers."
query = "Using only the contents of this file: " + file.read() + " , give me 5 possible root hypernyms for the words in " + wordList
#"Using the contents of " + file.read() + ", 
#query = "What is the root hypernym of the words " + wordList + " based on the contents of " + content
# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
response = chatbot.chat(query)
print(response)

# Create a new conversation
id = chatbot.new_conversation()
chatbot.change_conversation(id)

# Get conversation list
conversation_list = chatbot.get_conversation_list()

file.close()