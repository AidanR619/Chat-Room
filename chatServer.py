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
    parser.add_argument('-p', help = 'Port', required = True)

    args = parser.parse_args()
    return args

def createSock(port):
    '''
    Description: Creates the server socket
    Returns: sock - Created socket
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', int(port)))
    sock.listen(5)
    return sock

def main():
    '''
    Description: Houses all of the function calls
    '''
    args = parse()
    try: # connects to client
        sock = createSock(args.p)
        print("Waiting for connection...")
        client, addr = sock.accept()
        print("Connected.")
    except OSError as e:
        print(f"Could not connect.")
        return
    try:
        data = client.recv(4096) # recieves data from client
        print(data.decode())
        time.sleep(2) # waits 2 seconds
        client.close() # closes client socket
        sock.close() # closes server socket
    except OSError as e:
        exit(f"ERROR: {e}")

if __name__ == "__main__":
    main()