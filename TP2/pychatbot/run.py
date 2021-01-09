import aiml
import os
from autocorrect import Speller
spell = Speller()

BRAIN_FILE = "brain.brn"

kernel = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    kernel.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    kernel.bootstrap(learnFiles="aiml/learningFileList.aiml", commands="load aiml")
    print("Saving brain file: " + BRAIN_FILE)
    kernel.saveBrain(BRAIN_FILE)

# Press CTRL-C to break this loop
while True:
    msg = input(">>> ")
    msg = [spell(w) for w in (msg.split())]
    question = " ".join(msg)
    response = kernel.respond(question)
    if response:
        print("PyChatBot > ", response)
    else:
        print("PyChatBot > Sorry, I don't understand...", )
