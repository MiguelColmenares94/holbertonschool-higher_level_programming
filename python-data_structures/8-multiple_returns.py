#!/usr/bin/python3


def multiple_returns(sentence):
    """returns a tuple with the length of a
    string and its first character.
    """

    inpt_len = len(sentence)

    if inpt_len == 0:
        tup = (inpt_len, None)
    else:
        tup = (inpt_len, sentence[0])

    return (tup)
