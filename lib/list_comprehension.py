#!/usr/bin/env python3

def return_evens(num_list):
    evens=[]
    for nums in num_list:
        if nums%2==0:
            evens.append(nums)
    else:
        return evens


def make_exclamation(sentence_list):
    exclaimed_words=[]
    for words in sentence_list:
        exclaimed_words.append(words + "!")
    return exclaimed_words

make_exclamation(["I like computers', 'I require coffee', 'Live long and prosper"])
