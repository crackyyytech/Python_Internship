import random
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer

lemmatizer = WordNetLemmatizer()
tokenizer = TreebankWordTokenizer()

# Predefined intents
intents = {
    "intents": [
        {"tag": "greeting",
         "patterns": ["Hi", "Hello", "Hey", "How are you?", "Good day"],
         "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
        },
        {"tag": "goodbye",
         "patterns": ["Bye", "See you", "Goodbye", "Take care"],
         "responses": ["Goodbye!", "See you later!", "Take care!"]
        },
        {"tag": "thanks",
         "patterns": ["Thanks", "Thank you", "Much appreciated"],
         "responses": ["You're welcome!", "No problem!", "Anytime!"]
        },
        {"tag": "help",
         "patterns": ["Can you help me?", "I need assistance", "Help me"],
         "responses": ["Sure, I am here to help!", "What can I assist you with?"]
        }
    ]
}

def tokenize(sentence):
    return tokenizer.tokenize(sentence)

def lemmatize_words(words):
    return [lemmatizer.lemmatize(w.lower()) for w in words]

def bag_of_words(sentence, words):
    sentence_words = lemmatize_words(tokenize(sentence))
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def prepare_training_data(intents):
    all_words = []
    tags = []
    xy = []

    for intent in intents["intents"]:
        tag = intent["tag"]
        for pattern in intent["patterns"]:
            w = tokenize(pattern)
            all_words.extend(w)
            xy.append((w, tag))
        tags.append(tag)

    all_words = lemmatize_words(all_words)
    all_words = sorted(set(all_words))
    tags = sorted(set(tags))
    return all_words, tags, xy

def get_response(tag):
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

def classify(sentence, all_words, tags, xy):
    bag = bag_of_words(sentence, all_words)
    scores = []
    for pattern_words, tag in xy:
        pattern_bag = bag_of_words(" ".join(pattern_words), all_words)
        score = np.dot(bag, pattern_bag)
        scores.append((tag, score))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[0][0] if scores[0][1] > 0 else "unknown"

if __name__ == "__main__":
    nltk.download('wordnet')

    all_words, tags, xy = prepare_training_data(intents)

    print("🤖 Simple NLP Chatbot (type 'quit' to exit)")
    while True:
        sentence = input("You: ")
        if sentence.lower() == "quit":
            break
        tag = classify(sentence, all_words, tags, xy)
        if tag == "unknown":
            print("Bot: I didn't understand that.")
        else:
            print(f"Bot: {get_response(tag)}")
