import socket
import sys


def createClient():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 10000)

    # Uses the hostname or IP address and port number from command line arguments
    if len(sys.argv) == 3:
        server_address = (sys.argv[1], int(sys.argv[2]))

    while True:
        try:
            message = input("Please enter a string (^d terminates):")

            # Send the original message to server
            sock.sendto(message.encode(), server_address)

            # Receive ROT-13 from server
            data, server = sock.recvfrom(4096)
            print('received "%s"' % data.decode(), "from the server")

            # Send ROT-13 back to server
            sock.sendto(data, server_address)

            # Receive the original message from server
            data, server = sock.recvfrom(4096)
            print('received "%s"' % data.decode(), "from the server")

        except EOFError:
            print("Hitting end of file, closing socket")
            sock.close()

def main():
    createClient()

if __name__ == "__main__":
    main()
