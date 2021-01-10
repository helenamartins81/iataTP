import os
import select
import socket
import sys
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# localhost/7000
IP_address = '127.0.0.1'
Port = 7000
server.bind((IP_address, Port))

"""
Para ouvir 50 clientes maximo
"""
server.listen(50)

list_of_clients = []

print('Servidor a escutar!')


def clientthread(conn, addr):
    name = conn.recv(2048).decode()
    # Envia welcome message
    welcomemsg = 'Welcome, your random name is ' + name + "!"
    conn.send(welcomemsg.encode())

    while True:
        try:
            message = conn.recv(2048)
            if message:
                decodedmsg = message.decode()
                
                #Print da mensagem com o nome do client
                print("<" + name + "> " + decodedmsg)

                # Broadcast da mensagem
                message_to_send = "< " + name + " > " + decodedmsg
                broadcast(message_to_send.encode(), conn)
            else:
                """
                Caso a msg esteja vazia, remove a connection
                """
                remove(conn)
        except:
            continue


"""
Broadcast manda uma mensagem para todas as connections
menos a que a enviou
"""


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()

                # remove client se estiver erro
                remove(clients)


"""
Remove client da lista de clients
"""


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    # Aceita nova connection, conn = socket do user,
    # addr = ip address do user
    conn, addr = server.accept()

    # Lista de clients
    list_of_clients.append(conn)

    # Print address de novo user
    print("New user connected")

    # Cria thread para novo user
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()
