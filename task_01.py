#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Matchup game """


def get_matches(players):
    """
    Args:
        players (list): List of players
    Returns:
        list: List of matchup tuples
    """
    matchup = []
    for row, player1 in enumerate(players):
        for col, player2 in enumerate(players):
            if row < col:
                matchup.append((player1, player2))
    return matchup


if __name__ == '__main__':
    import data
    print get_matches(data.VERSUS)
