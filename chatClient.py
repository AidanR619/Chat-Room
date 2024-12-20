#!/usr/bin/env python

# Name: Aidan Rotz
# Creation Date: 12/19/2024
# Purpose: 

import argparse
import socket
import time

def parse():
    '''
    Description: Parses arguments based off of user input to get the host and port.
    Returns: args - The host and port information
    '''
    parser = argparse.ArgumentParser(add_help = False)
    parser.add_argument('-h', help = 'Host', default = 'localhost')
    parser.add_argument('-p', help = 'Port', required = True)

    args = parser.parse_args()
    return args

def createSock(host, port):
    '''
    Description: Creates the client socket
    Returns: sock- Created socket
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, int(port)))
    return sock
    
def send(sock, message):
    '''
    Description: Sends all of the data to the server
    '''
    sock.sendall(message.encode())

def main():
    '''
    Description: Houses all of the function calls
    '''
    args = parse()
    try:
        sock = createSock(args.h, args.p)
    except OSError as e:
        print(f"Could not connect.")
        return
    try:
        message = input("Enter a message: ") # user input message
        send(sock, message)
    except OSError as e:
        print(f"Failed to send message.")
    finally:
        time.sleep(2) #wait 2 seconds to close
        sock.close() #closes socket

if __name__ == "__main__":
    main()