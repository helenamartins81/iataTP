# Python program to implement client side of chat room.
import os
import random
import select
import socket
import sys
import re

from autocorrect import Speller

import aiml

spell = Speller()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = '127.0.0.1'
Port = 7000
server.connect((IP_address, Port))

"""
Inicializa o bot de respostas automaticas
"""

BRAIN_FILE = "brain.brn"

kernel = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    kernel.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    kernel.bootstrap(learnFiles="aiml/learningFileList.aiml",
                     commands="load aiml")
    print("Saving brain file: " + BRAIN_FILE)
    kernel.saveBrain(BRAIN_FILE)

# get random animal name
lines = open("randomanimals.txt").readlines()
randomname = random.choice(lines)

server.send(randomname[:-1].encode())

while True:
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]

    """
    Select é utilizado para identificar o estado atual
    (ou é necessario receber a msg do servidor, ou o user está
    a escrever uma mensagem para ser enviada).
    O if faz essa identificaçao
    """
    read_sockets, write_socket, error_socket = select.select(
        sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)

            if not message.decode():
                print('Servidor abaixo, vou sair...')
                exit()

            decodedmsg = message.decode()
            print(decodedmsg)

            # retira o que está entre "<>"
            msg = re.sub('<[^>]+>', '', decodedmsg)

            #fix spelling
            msg = [spell(w) for w in (msg.split())]
            question = " ".join(msg)
            response = kernel.respond(question)
            suggestion = '[Suggestion: ' + response + ' ]'

            print(suggestion)
        else:
            message = sys.stdin.readline()
            message = message[:-1]
            server.send(message.encode())
            sys.stdout.flush()
server.close()
