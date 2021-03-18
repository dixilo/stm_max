#!/usr/bin/env python3
'''Stimulator MAX board client'''
from time import sleep
from ocs.matched_client import MatchedClient

def main():
    '''Stimulator MAX board client'''
    max_client = MatchedClient('stmmax1')
    status, message, session = max_client.get_values(channel=0)
    print(status, message)
    print(session['data'])

    sleep(1)

    max_client.set_values(channel=0, tc_type=3)

    sleep(1)

    status, message, session = max_client.get_values(channel=0)
    print(status, message)
    print(session['data'])


if __name__ == '__main__':
    main()
