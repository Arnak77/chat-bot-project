#Lets Import the libraries
from nltk.chat.util import Chat, reflections


#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Aman Kharwal created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['New Delhi, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
    [
       r"(.*)tell me a joke(.*)",
       ["Why don't scientists trust atoms? Because they make up everything!",]
    ],
]

pairs_2=[
        [
    r"(.*)my name is (.*)",
    ["Hello %2, How are you today?",]
],
[
    r"(.*)help(.*)",
    ["I can help you.",]
],
[
    r"(.*)tell me a joke(.*)",
    ["Why don't scientists trust atoms? Because they make up everything!",]
],
[
    r"(.*)favorite movie(.*)",
    ["I don't watch movies, but I can recommend some based on your preferences.",]
],
[
    r"(.*)how are you(.*)",
    ["I'm just a computer program, but I'm here and ready to assist you!",]
],
[
    r"(.*)recommend a book(.*)",
    ["Certainly! What genre are you interested in?",]
],
[
    r"(.*)weather like today(.*)",
    ["I don't have real-time information. You can check a weather website for the latest updates.",]
],
[
    r"(.*)meaning of life(.*)",
    ["The meaning of life is subjective and varies for each person. What does it mean to you?",]
],
[
    r"(.*)make a good first impression(.*)",
    ["Making a good first impression involves being genuine, confident, and attentive. Smile, make eye contact, and show interest in the other person.",]
],
[
    r"(.*)capital of France(.*)",
    ["The capital of France is Paris.",]
],

[
    r"(.*)fun fact(.*)",
    ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",]
],
[
    r"(.*)languages do you speak(.*)",
    ["I'm fluent in multiple programming languages, but I communicate with humans in natural language like English.",]
],
[
    r"(.*)dream(.*)",
    ["No, I don't dream. I'm always here to assist you.",]
],
[
    r"(.*)largest ocean(.*)",
    ["The Pacific Ocean is the largest ocean on Earth.",]
],
[
    r"(.*)stay updated with information(.*)",
    ["I don't stay updated in real-time, but my responses are based on the knowledge available up to my last training cut-off in January 2022.",]
],
[
    r"(.*)difference between empathy and sympathy(.*)",
    ["Empathy involves understanding and sharing the feelings of others, while sympathy is feeling compassion or pity for someone.",]
],
[
    r"(.*)process of photosynthesis(.*)",
    ["Photosynthesis is a complex process where plants convert carbon dioxide and sunlight into glucose and oxygen, providing energy for growth.",]
],
[
    r"(.*)sing a song for me(.*)",
    ["I'm afraid I can't sing, but I can help you find song lyrics or information about your favorite artists.",]
],
[
    r"(.*)largest desert in the world(.*)",
    ["The largest desert in the world is Antarctica.",]
],
[
    r"(.*)internet work(.*)",
    ["The internet is a global network of interconnected computers that communicate using standardized protocols, allowing the exchange of information.",]
],
[
    r"(.*)difference between a fruit and a vegetable(.*)",
    ["Fruits develop from the ovary of a flower and contain seeds, while vegetables are any other edible part of a plant, like leaves, roots, or stems.",]
],
[
    r"(.*)president of the United States(.*)",
    ["I don't have real-time information. You may want to check the latest news for the current president.",]
],
[
    r"(.*)speed of light(.*)",
    ["The speed of light in a vacuum is approximately 299,792 kilometers per second.",]
],
[
    r"(.*)favorite hobby(.*)",
    ["I don't have hobbies, but I enjoy helping you with your questions and tasks.",]
],
[
    r"(.*)car engine work(.*)",
    ["A car engine works by converting fuel into mechanical energy through a process called internal combustion.",]
],
[
    r"(.*)famous scientist(.*)",
    ["Albert Einstein was a renowned physicist known for his theory of relativity and contributions to the field of theoretical physics.",]
],
[
    r"(.*)difference between a virus and a bacterium(.*)",
    ["Viruses are smaller than bacteria and can only reproduce inside living cells. Bacteria are single-celled organisms that can live independently.",]
],
[
    r"(.*)capital of Japan(.*)",
    ["The capital of Japan is Tokyo.",]
],
[
    r"(.*)difference between classical and quantum physics(.*)",
    ["Classical physics describes the macroscopic world, while quantum physics deals with the microscopic world of particles, where phenomena can behave differently.",]
],
[
    r"(.*)stay updated with information(.*)",
    ["I don't stay updated in real-time, but my responses are based on the knowledge available up to my last training cut-off in January 2022.",]
],
[
    r"(.*)difference between a galaxy and a solar system(.*)",
    ["A galaxy is a vast system of stars, stellar remnants, interstellar gas, dust, and dark matter, while a solar system consists of a central star and its orbiting planets.",]
],
[
    r"(.*)immune system work(.*)",
    ["The immune system defends the body against harmful pathogens by recognizing and attacking them, involving various cells, tissues, and organs.",]
],
[
    r"(.*)recommend a good workout routine(.*)",
    ["I can provide general advice, but it's important to consult with a fitness professional for a personalized workout routine based on your goals and fitness level.",]
],
[
    r"(.*)purpose of DNA(.*)",
    ["DNA carries genetic information and instructions for the development, functioning, growth, and reproduction of all known living organisms.",]
],
[
    r"(.*)difference between classical and quantum physics(.*)",
    ["Classical physics describes the macroscopic world, while quantum physics deals with the microscopic world of particles, where phenomena can behave differently.",]
],
[
    r"(.*)who painted the Mona Lisa(.*)",
    ["Leonardo da Vinci painted the Mona Lisa.",]
],
  [
      r"quit",
      ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
  ],
# Add more question-answer pairs as needed
]

       

print(reflections)





#default message at the start of chat

print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")


#Create Chat Bot
chat = Chat(pairs, reflections)

chat_2 = Chat(pairs_2, reflections)

#Now, let’s start a conversation
#Start conversation
chat.converse()

chat_2.converse()
