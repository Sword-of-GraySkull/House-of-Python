# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:08:49 2020

@author: Venni
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('name', help = 'name of the user')

parser.add_argument('-g', '--greeting', default = 'Hello', help = 'Alternate Greeting')

args = parser.parse_args()

print("{greeting}, {name}".format(greeting = args.greeting, name = args.name))
