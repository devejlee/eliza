import nltk
import random
from nltk.stem import WordNetLemmatizer

responses = {
    "NOTFOUND": {
        "weight": 0,
        "responses": [
            "What does that suggest to you?",
            "I see.",
            "I'm not sure I understand you fully.",
            "Can you elaborate?",
            "That is quite interesting.",
            "Please tell me more.",
            "Let's change focus a bit... Tell me about your family.",
            "Can you elaborate on that?",
            "Why do you say that *?"
        ]
    },
    "i think": {
        "weight": 5,
        "responses": ["Do you really think so?"]
    },
    "yes": {
        "weight": 7,
        "responses": ["Why do you think so?", "You seem quite positive."]
    },

    "no": {
        "weight": 8,
        "responses": ["Why not?", "Are you sure?"]
    },
}


# Init the Wordnet Lemmatizer
# lemmatizer = WordNetLemmatizer()

# Lemmatize list of words and join
# lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])

# Starting and ending dialogue
start_chat = ["What do you want to talk about? :)", "Hello. How are you doing today? :)"]
end_chat = ["Goodbye ):", "I have to leave ):"]

user_input = input("ELIZA: " + random.choice(start_chat) + ' ')
chatbot_response = ''

sent_list = nltk.sent_tokenize(user_input)

for sentence in sent_list:
    print('sentence', sentence)
    word_list = nltk.word_tokenize(sentence)
    print('word_list', word_list)
    for word in word_list:
        if word in responses:
            print('random response:', random.choice(responses[word]["responses"]))
        else:
            print('nope')

# remove punctuation sent_list