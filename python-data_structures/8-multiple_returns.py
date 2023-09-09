#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        returns = (0, None)
    else:
        returns = (len(sentence), sentence[0])
    return returns


if __name__ == "__multiple_returns__":
    multiple_returns()
