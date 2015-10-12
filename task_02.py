#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Authentication """


import authentication
import getpass


def login(username, maxattempts):
    """
    Args:
        username (string): username
        maxattemtps (int): maximum authentication attempts
    Returns:
        bool: True of false depending on authentication success.
    """
    if maxattempts < 1:
        print 'Error, there must be at least one attempt to authenticate'
    if username:

        attempt = 0
        while attempt < maxattempts:
            print attempt
            mypass = getpass.getpass('Please enter your password: ')
            if authentication.authenticate(username, mypass):
                return True
            attempt += 1
            print 'Incorrect username of password. You have ' \
                + str(maxattempts - attempt) + ' attempts left.'

        return False

if __name__ == '__main__':
    print login('charlie', 5)
