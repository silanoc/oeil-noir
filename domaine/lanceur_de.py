#! /usr/bin/env python3
# coding: utf-8

"""Module pour gérer les lancer de dé du programme."""

from random import *


def d20() -> int:
    """lance 1D20
    
    :returns: nb_alea entre 1 et 20, bornes incluses.
    :rtype: int"""
    nb_alea: int  =  randint(1,20)
    return nb_alea
    
def d6() -> int:
    """lance 1D6
    
    :returns: nb_alea entre 1 et 6, bornes incluses.
    :rtype: int"""
    nb_alea: int  =  randint(1,6)
    return nb_alea

if __name__ == "__main__":
    print(f"un nombre au hasard entre 1 et 20 : {d20()}")
    print(f"un nombre au hasard entre 1 et 6 : {d6()}")
    