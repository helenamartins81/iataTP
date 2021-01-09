import aiml
import os
import random

BRAIN_FILE = "brain.brn"
sessionId = random.randrange(10000)

kernel = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    kernel.loadBrain(BRAIN_FILE)
else:
    kernel.bootstrap(learnFiles="learningFileList.aiml", commands="LEARN AIML")
    print("Saving brain file: " + BRAIN_FILE)
    kernel.saveBrain(BRAIN_FILE)

print("Welcome to PyChatBot!")

# Press CTRL-C to break this loop
while True:
    message = input(">>> ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain(BRAIN_FILE)
    else:
        bot_response = kernel.respond(message, sessionId)
        print(bot_response)
