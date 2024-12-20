# Name: Aidan Rotz
# Creation Date: 12/19/2024
# Purpose: 

import argparse

def parse():
    '''
    Description: Parses arguments based off of user input to get the host and port.
    Returns: args - the host and port information
    '''
    parser = argparse.ArgumentParser(add_help = False)
    parser.add_argument('-p', help = 'Port', required = True)

    args = parser.parse_args()
    return args

def main():
    '''
    Description: Houses all of the function calls
    '''
    args = parse()

if __name__ == "__main__":
    main()