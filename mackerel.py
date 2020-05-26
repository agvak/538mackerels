# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:04:59 2020

@author: Sandro
"""

#Return True if any of the letters in 'state' are shared by letters in 'word'
def share(state,word):
    stateSet = set(state)
    wordSet = set(word)
    for letter in stateSet:
        if letter in wordSet:
            return True
    return False

#Read in words    
with open('word.list.txt') as f:
    words = f.readlines()
f.close()
words= [x.strip() for x in words] 

#Read in states
with open('states.txt') as f:
    states = f.readlines()
f.close()
states = [x.strip().lower() for x in states] 


#Longest mackerel?
bestLength = 0
mackerelStates = []
mackerelWords = []
bestState = 'none'
for word in words:
    if len(word)<bestLength:
        continue
    stateMatch = 0
    for state in states:
        if not share(state,word):
            stateMatch+=1
            bestState = state
        if stateMatch>1:
            break
    if stateMatch == 1:
        mackerelWords.append(word)
        bestLength = len(word)
        mackerelStates.append(bestState)

#Most mackerels?
stateCount = {}
for word in words:
    stateMatch = 0
    for state in states:
        if not share(state,word):
            stateMatch+=1
            bestState = state
        if stateMatch>1:
            break
    if stateMatch == 1:#Mackerel found
        if bestState in stateCount:
            stateCount[bestState] = stateCount[bestState]+1
        else:
            stateCount[bestState] = 1

max(stateCount, key=stateCount.get)