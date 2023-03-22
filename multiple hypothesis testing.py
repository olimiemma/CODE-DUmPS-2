#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:01:34 2023

@author: legend
"""

import random

numCasesPerYear= 36000
numYears =3
stateSize=10000
communitySize =10
numCommunities = stateSize//communitySize

numTrials =100
numGreater =0

for t in range(numTrials):
    locs = [0]*numCommunities
    for i in range(numYears*numCasesPerYear):
        locs[random.choice(range(numCommunities))] +=1
    if locs[111] >=143:
        numGreater +=1
prob= round(numGreater/numTrials, 4)
print("Est. probabilty of region 111 having at least 143 case =", prob)
        



anyRegion=0
for trial in range(numTrials):
    locs= [0]*numCommunities
    for i in range(numYears*numCasesPerYear):
        locs[random.choice(range(numCommunities))] +=1
        if max(locs) >143:
            anyRegion +=1
print(anyRegion)
aProb =round(anyRegion/numTrials, 4)
print( "Est. Probability of some region having at least 143 cases =", aProb)