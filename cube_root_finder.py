# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 14:56:50 2026

@author: tugru
"""

# Trying to find cube root of number

x=float(input('what x to find the cube root of?'))
g=float(input('what is your guess?'))
print('Current estimate cubed=', g**3)
next_guess= g-((g**3-x)/(3*g**2))
print('Next guess to try=', next_guess)
