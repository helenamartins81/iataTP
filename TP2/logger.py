print("Bem vindo ao PyChatBot!\nComeça a conversa:")

msg = ''

while msg != 'exit':
    msg = input('> ')
    with open('messagesUser.txt', 'a') as f:
        f.write(msg + '\n')
