#!/usr/bin/python3
import sys
import hidden_4 as mod


for i in dir(mod):
    if i[1] != "_":
        print("{}".format(i))
