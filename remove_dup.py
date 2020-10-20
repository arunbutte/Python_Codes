# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:04:46 2020

@author: Sandeep
"""

import llist
from llist import sllist,sllistnode 


def remove_dups(ll):
    current = ll.first
    while current.next:
        if current == current.next:
            current.next = current.next.next 
    return ll