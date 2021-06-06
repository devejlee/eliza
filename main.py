import nltk
import random
import string
from nltk.corpus import wordnet as wn

lemmatizer = nltk.stem.WordNetLemmatizer()

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
    "sorry": {
        "weight": 1,
        "responses": ["Please don't apologize.", "Apologies are not necessary.", "Apologies are not required."]
    },
    "always": {
        "weight": 2,
        "responses": ["Can you think of a specific example?"]
    },
    "because": {
        "weight": 3,
        "responses": ["Is that the real reason?"]
    },
    "maybe": {
        "weight": 4,
        "responses": ["You don't seem very certain."]
    },
    "think": {
        "weight": 5,
        "responses": ["Do you really think so?"]
    },
    "you": {
        "weight": 6,
        "responses": ["We were discussing you, not me.", "Why do you say that about me?",
                      "Why do you care whether I \"*\"?"]
    },
    "yes": {
        "weight": 7,
        "responses": ["Why do you think so?", "You seem quite positive."]
    },
    "no": {
        "weight": 8,
        "responses": ["Why not?", "Are you sure?"]
    },
    "am": {
        "weight": 9,
        "responses": ["I am sorry to hear you are *.", "How long have you been *?",
                      "Do you believe it is normal to be *?", "Do you enjoy being *?",
                      "Did you come to me because you are *?"]
    },
    "i feel": {
        "weight": 10,
        "responses": ["Tell me more about such feelings.", "Do you often feel *?", "Do you enjoy feeling *?",
                      "Why do you feel that way?"]
    },
    "family": {
        "weight": 11,
        "responses": ["Tell me more about your family.", "How do you get along with your family?",
                      "Is your family important to you?"]
    },
    "mother": {
        "weight": 12,
        "responses": ["Tell me more about your family.", "How do you get along with your family?",
                      "Is your family important to you?"]
    },
    "father": {
        "weight": 13,
        "responses": ["Tell me more about your family.", "How do you get along with your family?",
                      "Is your family important to you?"]
    },
    "mom": {
        "weight": 14,
        "responses": ["Tell me more about your family.", "How do you get along with your family?",
                      "Is your family important to you?"]
    },
    "sister": {
        "weight": 15,
        "responses": ["Tell me more about your family.", "How do you get along with your family?",
                      "Is your family important to you?"]
    },
    "brother": {
        "weight": 16,
        "responses": ["Tell me more about your family.", "How do you get along with your family?",
                      "Is your family important to you?"]
    },
    "husband": {
        "weight": 17,
        "responses": ["Tell me more about your family.", "How do you get along with your family?",
                      "Is your family important to you?"]
    },
    "wife": {
        "weight": 18,
        "responses": ["Tell me more about your family.", "How do you get along with your family?",
                      "Is your family important to you?"]
    },
    "child": {
        "weight": 19,
        "responses": ["Did you have close friends as a child?", "What is your favorite childhood memory?",
                      "Do you remember any dreams or nightmares from childhood?",
                      "Did the other children sometimes tease you?",
                      "How do you think your childhood experiences relate to your feelings today?"]
    },
    "dreamed": {
        "weight": 20,
        "responses": ["What does that dream suggest to you?", "Do you dream often?",
                      "What people appear in your dreams?", "Are you disturbed by your dreams?",
                      "Have you ever fantasized * while you were awake?"]
    },
    "nightmare": {
        "weight": 21,
        "responses": ["What does that dream suggest to you?", "Do you dream often?",
                      "What persons appear in your dreams?", "Are you disturbed by your dreams?"]
    },
    "hello": {
        "weight": 22,
        "responses": ["Hi again! How is going?", "How are you today? Any problems?"]
    },
    "good afternoon": {
        "weight": 23,
        "responses": ["Hi again! How is going?", "How are you today? Any problems?"]
    },
    "good morning": {
        "weight": 24,
        "responses": ["Hi again! How is going?", "How are you today? Any problems?"]
    },
    "hi": {
        "weight": 25,
        "responses": ["Hi again! How is going?", "How are you today? Any problems?"]
    },
    "goodbye": {
        "weight": 26,
        "responses": ["Goodbye.  Thank you for talking to me."]
    },
    "i need": {
        "weight": 27,
        "responses": ["Why do you need *?", "Would it really help you to get *?", "Are you sure you need *?"]
    },
    "why don\'t you": {
        "weight": 28,
        "responses": ["Do you really think I don't *?", "Perhaps eventually I will *.",
                      "Do you really want me to *?"]
    },
    "why can\'t i": {
        "weight": 29,
        "responses": ["Do you think you should be able to *?", "If you could *, what would you do?",
                      "I don't know -- why can't you *?", "Have you really tried?"]
    },
    "i can\'t": {
        "weight": 30,
        "responses": ["How do you know you can't \"*\"?", "Perhaps you could * if you tried.",
                      "What would it take for you to *?"]
    },
    "perhaps": {
        "weight": 31,
        "responses": ["How do you know you can't \"*\"?", "Perhaps you could * if you tried.",
                      "What would it take for you to *?"]
    },
    "remember": {
        "weight": 32,
        "responses": ["Do you often think of *?", "Does thinking of * bring anything else to mind",
                      "What else do you recollect?", "Why do you recollect * just now?",
                      "What in the present situation reminds you of *?", "What is the connection between me and *?"]
    },
    "do you remember": {
        "weight": 33,
        "responses": ["Do you think I would forget?", "Yes I do remember *."]
    },
    "if": {
        "weight": 34,
        "responses": ["Do you think it\'s likely that *?", "Do you wish that *?", "What do you know about *?",
                      "Really, if *?"]
    },
    "name": {
        "weight": 35,
        "responses": ["I am not interested in names.",
                      "I\'ve told you before, I do not care about names -- please continue."]
    },
    "another language": {
        "weight": 36,
        "responses": ["I told you before, I don't understand languages that are not English."]
    },
    "computer": {
        "weight": 37,
        "responses": ["Do computers worry you?", "Why do you mention computers?",
                      "Could you expand on how computers and * are related?",
                      "What do you think machines have to do with your problem?",
                      "Don't you think computers can help people?", "What about machines worrys you?",
                      "What do you think about machines?"]
    },
    "are you": {
        "weight": 38,
        "responses": ["Why are you interested in whether I am * or not?", "Would you prefer if I weren't *?",
                      "Perhaps I am * in your fantasies.", "Do you sometimes think I am *?"]
    },
    "are": {
        "weight": 39,
        "responses": ["Did you think they might not be *?", "Would you like it if they were not *?",
                      "What if they were not *?", "Possibly they are *."]
    },
    "your": {
        "weight": 40,
        "responses": ["Why are you concerned over my *?", "What about your own *?",
                      "Are you worried about someone else's *?", "Really, my *?"]
    },
    "was i": {
        "weight": 41,
        "responses": ["What if you were *?", "Do you think you were *?", "Were you *?",
                      "What would it mean if you were *?", "What does * suggest to you?"]
    },
    "was you": {
        "weight": 42,
        "responses": ["Would you like to believe I was *?", "What suggests that I was *?", "What do you think?"]
    },
    "i desire": {
        "weight": 43,
        "responses": ["What would it mean to you if you got it?", "Why do you want it?", "What if you never got it?"]
    },
    "i desired": {
        "weight": 44,
        "responses": ["Did you achieve it or simply moved on?"]
    },
    "i am sad": {
        "weight": 45,
        "responses": ["Sorry to hear you are. Tell me about it."]
    },
    "i am happy": {
        "weight": 46,
        "responses": ["That's good. What is making you happy?"]
    },
    "i am bored": {
        "weight": 47,
        "responses": ["What makes you bored?"]
    }
}

# List of special case
# "i am *1-3* happy" -> "i am happy"
# Ex.
# User> I am extremely happy
# this becomes "I am happy"
# Eliza> Why are you happy?
# Ex.
# User> I am sad because i wish i was happy
# This is changed because the 1-3 represents this
# is valid if there is 1 to 3 words between "am" and
# "happy"

responsesWithWildcard = {
    "i am *1-3* happy": {
        "weight": 20,
        "replacementWord": "i am happy"
    },
    "i am *1-3* sad": {
        "weight": 20,
        "replacementWord": "i am sad"
    },
    "i am *1-3* bored": {
        "weight": 20,
        "replacementWord": "i am bored"
    }
}

start_chat = ["Hello. How are you feeling today?",
              "Hi there, welcome to my office. I'm here to chat about anything. What's on your mind?",
              "How do you do. Please tell me your problem.", "Please tell me what's been bothering you.",
              "Is something troubling you?", "Hello. How are you doing today?"]

end_chat = ["Goodbye :)", "I have to leave ):"]

user_input = input("ELIZA: " + random.choice(start_chat) + ' ')
continue_chat = True


# check synonyms of user input
def synonyms(token):
    synsets = wn.synsets(token)
    for syn in synsets:
        syn_list = syn.lemma_names()
        for word in syn_list:
            if word in responses:
                return word


while continue_chat:
    unknown_words = []
    known_words = []
    # Check if there is a prepared response for each word user enters
    for word in set(user_input.split()):
        token = lemmatizer.lemmatize(word.lower().strip(string.punctuation))
        if synonyms(token) is not None:
            found_word = synonyms(token)
            known_words.append({"word": found_word, "weight": responses[found_word]["weight"]})
        else:
            unknown_words.append(token)
    # Debugging
    print('used_tokens:', sorted(known_words, key=lambda item: item['weight']))
    print('unused_tokens:', unknown_words)
    # Respond with the highest weight response. If there is no prepared response, end chat.
    if len(known_words) > 0:
        highest_weight = sorted(known_words, key=lambda item: item['weight'])[-1]["word"]
        print(random.choice(list(responses[highest_weight]["responses"])))
        user_input = input('ELIZA: Talk to me again: ')
    else:
        continue_chat = False

print("ELIZA: " + random.choice(end_chat) + ' ')
