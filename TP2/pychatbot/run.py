import aiml
import os
import random
from autocorrect import Speller

spell = Speller()

BRAIN_FILE = "brain.brn"
sessionId = random.randrange(10000)

kernel = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    kernel.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    kernel.bootstrap(learnFiles="learningFileList.aiml", commands="load aiml")
    print("Saving brain file: " + BRAIN_FILE)
    kernel.saveBrain(BRAIN_FILE)

print("Welcome to PyChatBot!")

# Press CTRL-C to break this loop
while True:
    msg = input(">>> ")
    msg = [spell(w) for w in (msg.split())]
    question = " ".join(msg)
    response = kernel.respond(question, sessionId)
    if response:
        print("PyChatBot > ", response)
    else:
        print("PyChatBot > Sorry, I don't understand...", )

