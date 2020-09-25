import socket
import sys

def encryptMessage(message):
    array = []

    for i in range(len(message)):
        char = message[i]
        isUpper = False

        if char == " " or not char.isalpha():
            array.append(char)
            continue

        if char.isupper():
            isUpper = True
            char = char.lower()

        ordNum = (ord(char) - 97 + 13) % 26 + 97
        newChar = chr(ordNum)

        if isUpper:
            newChar = newChar.upper()
        array.append(newChar)

    encryptedMessage = ''.join(c for c in array)
    print("The encrypted message is:", encryptedMessage)
    return encryptedMessage

def createServer():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)

    # Uses the port from command line argument
    if len(sys.argv) == 2:
        server_address = ('localhost', int(sys.argv[1]))
    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)

    while True:
        print('Server is waiting to receive message')
        data, address = sock.recvfrom(4096)
        print('Server has received %s bytes from %s' % (len(data), address))
        print("Server has received the original message: ",data.decode())
        encryptedMessage = encryptMessage(data.decode())
        if data:
            sock.sendto(encryptedMessage.encode(), address)

def main():
    createServer()

if __name__ == "__main__":
    main()
