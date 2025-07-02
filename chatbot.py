import nltk
import random
import string

from nltk.chat.util import Chat, reflections


nltk.download('punkt')


pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"what is your name?", ["I'm a chatbot created by CODTECH intern."]],
    [r"how are you?", ["I'm doing great, thanks!", "I'm fine, how about you?"]],
    [r"what can you do?", ["I can answer simple questions using NLP!", "I'm here to chat with you."]],
    [r"bye|exit|quit", ["Goodbye!", "See you later!", "Bye! Have a nice day."]],
    [r"(.*)", ["I'm not sure I understand. Can you rephrase?"]]
]


chatbot = Chat(pairs, reflections)

print("CODTECH NLP Chatbot: Type something to start a conversation (type 'quit' to exit)")
chatbot.converse()  