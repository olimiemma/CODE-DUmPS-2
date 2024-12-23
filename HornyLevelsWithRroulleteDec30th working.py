# -*- coding: utf-8 -*-

import  random, requests, json, pylab

""" 
Spyder Editor


This is a temporary pogram to test your horniness and bring appropriate porn, Get straight to the point.
#side note-korean Gugak
"""

# #def rSquared(observed, predicted):
#     error = ((predicted - observed)**2).sum()
#     meanError = error/len(observed)
#     return 1 - (meanError/numpy.var(observed))


class prompt():
    def __init__(self, hi):
        self.hi=hi
        #self.freaky=freaky
    def getHi(self):
        return self.hi
   
    def __str__(self):
        return self.getHi() + 'lets get it started '

#-------------------------------------------------------------------------------------------------------
def start():
    """
    Prompts user for Names

    Returns
    -------
    name : TYPE String
        DESCRIPTION. names of the user

    """
    name =input(" Thy Names Kind sir, two names please? ").strip().title()
    first, last = name.split() 
    print(f"hello, {first}, lets get it started ")
    return name

start()

#------------------------------------------------------------------------------------------------------
def getHornLevel():
    """
    prompts for horn level

    Returns
    -------
    hornLevel : TYPE Int
        DESCRIPTION. level of horniness usser is feeling
    """
    hornLevel= int(input("1 to 37: How Horn are you..."))
    if hornLevel>0:
      print (f"Nicee!!.. Am gonna make you cum {hornLevel:,} times" )
      return hornLevel
  
getHornLevel()

#---------------------------------------------------------------------------------------------------------
# def getVids ():
#     song=input("whats your preffered black or white ") 
#     if song == "black":
#         playRoulette.bet = 1
#     else: playRoulette.bet=0
#     response=requests.get("https://itunes.apple.com/search?entity=song&limit=2&term" + song) #2 is the limit of results
# #https://api.redgifs.com/v2/gifs/52
# #https://api.redgifs.com/docs/index.html
#     print(response.json())
#    # print(josn.dumps(response.json()), indent=2)
 
# getVids()

#-------------------------------------------


class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(random.range(1,37)): # do random range of nUmbers, find right randoms funct
            self.pockets.append(i)
        self.ball = None
        self.blackOdds, self.redOdds = 1.2, 1.0
        self.pocketOdds = len(self.pockets) - 1.0
    def spin(self):
        self.ball = getHornLevel.hornLevel
    def isBlack(self):
        if type(self.ball) != int:
            return False
        if ((self.ball > 0 and self.ball <= 10)\
            or (self.ball>18 and self.ball<=28)):
            return self.ball%2 == 0 # black 0
        else:
            return self.ball%2 == 1 # red/white is 1
    def isRed(self):
        return type(self.ball) == int and not self.isBlack()
    def betBlack(self, amt):
        if self.isBlack():
            return amt*self.blackOdds
        else: return -amt
    def betRed(self, amt):
        if self.isRed():
            return amt*self.redOdds
        else: return -amt*self.redOdds
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else: return -amt
    def __str__(self):
        return 'Fair Roulette'
    
#------------------------------------------------
# def playRoulette(game, numSpins, toPrint = True):
#     luckyNumber = '2'
#     bet = 1
#     totRed, totBlack, totPocket = 0.0, 0.0, 0.0
#     for i in range(numSpins):
#         game.spin()
#         totRed += game.betRed(bet)
#         totBlack += game.betBlack(bet)
#         totPocket += game.betPocket(luckyNumber, bet)
#     if toPrint:
#         print(numSpins, 'spins of', game)
#         print('Expected return betting red =',
#               str(100*totRed/numSpins) + '%')
#         print('Expected return betting black =', 
#               str(100*totBlack/numSpins) + '%')
#         print('Expected return betting', luckyNumber, '=',\
#               str(100*totPocket/numSpins) + '%\n')
#     return (totRed/numSpins, totBlack/numSpins, totPocket/numSpins)


# numSpins = 1000
# game = FairRoulette()
# playRoulette(game, numSpins)

# class EuRoulette(FairRoulette):
#     def __init__(self):
#         FairRoulette.__init__(self)
#         self.pockets.append('0')
#     def __str__(self):
#         return 'European Roulette'

# class AmRoulette(EuRoulette):
#     def __init__(self):
#         EuRoulette.__init__(self)
#         self.pockets.append('00')
#     def __str__(self):
#         return 'American Roulette'

# def findPocketReturn(game, numTrials, trialSize, toPrint):
#     pocketReturns = []
#     for t in range(numTrials):
#         trialVals = playRoulette(game, trialSize, toPrint)
#         pocketReturns.append(trialVals[2])
#     return pocketReturns

# # random.seed(0)
# # numTrials = 20
# # resultDict = {}
# # games = (FairRoulette, EuRoulette, AmRoulette)
# # for G in games:
# #     resultDict[G().__str__()] = []
# # for numSpins in (100, 1000, 10000, 100000):
# #     print('\nSimulate betting a pocket for', numTrials,
# #           'trials of',
# #           numSpins, 'spins each')
# #     for G in games:
# #         pocketReturns = findPocketReturn(G(), numTrials,
# #                                          numSpins, False)
# #         print('Exp. return for', G(), '=',
# #              str(100*sum(pocketReturns)/float(len(pocketReturns))) + '%')

# def getMeanAndStd(X):
#     mean = sum(X)/float(len(X))
#     tot = 0.0
#     for x in X:
#         tot += (x - mean)**2
#     std = (tot/len(X))**0.5
#     return mean, std

# random.seed(0)
# numTrials = 20
# resultDict = {}
# games = (FairRoulette, EuRoulette, AmRoulette)
# for G in games:
#     resultDict[G().__str__()] = []
# for numSpins in (100, 1000, 10000):
#     print('\nSimulate betting a pocket for', numTrials,
#           'trials of', numSpins, 'spins each')
#     for G in games:
#         pocketReturns = findPocketReturn(G(), 20, numSpins, False)
#         mean, std = getMeanAndStd(pocketReturns)
#         resultDict[G().__str__()].append((numSpins,
#                                           100*mean, 100*std))
#         print('Exp. return for', G(), '=', str(round(100*mean, 3))
#               + '%,', '+/- ' + str(round(100*1.96*std, 3))
#               + '% with 95% confidence')
              

# def plotReturn(resultDict):
#     for k in resultDict:
#         xVals, yVals, eVals = [], [], []
#         for trial in resultDict[k]:
#             xVals.append(trial[0])
#             yVals.append(trial[1])
#             eVals.append(trial[2])
#         pylab.errorbar(xVals, yVals, yerr = eVals, label = k, marker = 'o')
#     pylab.legend()
#     pylab.xlabel('Spins per trial', fontsize = 'x-large')
#     pylab.ylabel('Expected percentage return', fontsize = 'x-large')
#     pylab.title('Expected Return Betting a Pocket', fontsize = 'x-large')
#     pylab.semilogx()
#     minX, maxX = pylab.xlim()
#     pylab.xlim(1, maxX + 100000)
# #    
# plotReturn(resultDict)
# assert False

# def plotMeans(numDice, numRolls, numBins, legend, color, style):
#     means = []
#     for i in range(numRolls//numDice):
#         vals = 0
#         for j in range(numDice):
#             vals += 5*random.random() 
#         means.append(vals/float(numDice))
#     pylab.hist(means, numBins, color = color, label = legend,
#                weights = pylab.array(len(means)*[1.0])/len(means),
#                hatch = style)
#     return getMeanAndStd(means)
 
# mean, std = plotMeans(1, 100000, 11, '1 die', 'b', '*')
# print('Mean of rolling 1 die =', mean, 'Std =', std)
# mean, std = plotMeans(50, 100000, 11, 'Mean of 50 dice', 'r', '//')
# print('Mean of rolling 50 dice =', mean, 'Std =', std)
# pylab.title('Rolling Continuous Dice')
# pylab.xlabel('Value')
# pylab.ylabel('Probability')
# pylab.legend()


# def leaveAhead(game, stake, bet, numTrials):
#     numAhead = 0.0
#     for t in range(numTrials):
#         bankRoll = stake
#         curBet = bet
#         while bankRoll > 0 and bankRoll <= 2*stake:
#             game.spin()
#             outcome = game.betBlack(curBet)
#             bankRoll += outcome
#             if outcome < 0:
#                 curBet = min(2*curBet, bankRoll)
#             #print curBet, bankRoll
#         if bankRoll > stake:
#             numAhead += 1
#     return numAhead/numTrials

#stake = 1
#bet = 1
#numTrials = 100000
#successProb, stakes = [], []
#for i in range(10):
#    stakes.append(10**i)
#    successProb.append(leaveAhead(AmRoulette(), 10**i, bet, numTrials))
#pylab.plot(stakes, successProb)
#pylab.xlabel('Bankroll')
#pylab.ylabel('Probability of Winning')
#pylab.semilogx()
#pylab.show()






# def leve_of_horn__print (n):
#     print (f" {start},  Am gonna make you cum {n:,} times" ) # commas in numbers
#     #print (" ### find videos with that Number of times in comment")
#             #:Mind geeeks API
#     #print ("These will get the job done")

# leve_of_horn__print(horn_level)

# freaky = "yeahhh baby"
# muyayu = hi + " " + freaky
# print(muyayu)
# extraMuyayu = muyayu + (" " + freaky)*3 + " " + "Give it to me" 
# #print(extraMuyayu)

# chaMuy1 = "ohhh yeah "
# chaMuyAlmost = " keep going, righ there"
# callingCall= "Whistle"

# wansi="how about we turn that up some? ==D. more!!"
# list(wansi)
# wansi.split( )
# wansi_turnt="MOTHERFU**ING".join(wansi)
    



# horn_level = GET_horn_level()



# """
# Sys.exit - exits the entire program. 
# Break - breaks out of loops

# """
# def luckyroulette():
#     if horn_level ==  playRoulette.luckyNumber:
#         playRoulette(FairRoulette)
        
        
# def how_numOfCums_gets_used():  
#     if horn_level<6:
#         print ((chaMuy1 + callingCall)*horn_level)
#         #setbackground to video point on loop , write algorith to select time to loop
#     else:
#           wansi_meth()
   
    
# def wansi_meth():   
#     #while   True:
#     try:
#         LOA = input("Get harder? Yes/No...").strip().title()
        
#         if LOA == "YES" or LOA =="Yes" or LOA == "yes" or LOA == "Y" or LOA == "y":
#             print ((chaMuy1, "dont stop!")*GET_horn_level())
#               #sys.exit ((chaMuy1, "dont stop!")*GET_horn_level())
#               #break
#         else: 
#             while LOA == "No" or LOA =="no" or LOA == "N" or LOA =="n" or LOA != "yes":
#                 print("Get Harder, cooomee onnn Babbyyy:==D")
#                 LOA = input("Get harder? Yes/No...")
#                 # break
#     except ValueError:
#         print("nah Bruh")
        
# use=how_numOfCums_gets_used()  

# class FairRoulette():
#     def __init__(self):
#         self.pockets = []
#         for i in range(random.range(1,37)): # do random range of nUmbers, find right randoms funct
#             self.pockets.append(i)
#         self.ball = None
#         self.blackOdds, self.redOdds = 1.0, 1.0
#         self.pocketOdds = len(self.pockets) - 1.0
#     def spin(self):
#         self.ball = random.choice(self.pockets)
#     def isBlack(self):
#         if type(self.ball) != int:
#             return False
#         if ((self.ball > 0 and self.ball <= 10)\
#             or (self.ball>18 and self.ball<=28)):
#             return self.ball%2 == 0
#         else:
#             return self.ball%2 == 1
#     def isRed(self):
#         return type(self.ball) == int and not self.isBlack()
#     def betBlack(self, amt):
#         if self.isBlack():
#             return amt*self.blackOdds
#         else: return -amt
#     def betRed(self, amt):
#         if self.isRed():
#             return amt*self.redOdds
#         else: return -amt*self.redOdds
#     def betPocket(self, pocket, amt):
#         if str(pocket) == str(self.ball):
#             return amt*self.pocketOdds
#         else: return -amt
#     def __str__(self):
#         return 'Fair Roulette'

# def playRoulette(game, numSpins, toPrint = True):
#     luckyNumber = '2'
#     bet = 1
#     totRed, totBlack, totPocket = 0.0, 0.0, 0.0
#     for i in range(numSpins):
#         game.spin()
#         totRed += game.betRed(bet)
#         totBlack += game.betBlack(bet)
#         totPocket += game.betPocket(luckyNumber, bet)
#     if toPrint:
#         print(numSpins, 'spins of', game)
#         print('Expected return betting red =',
#               str(100*totRed/numSpins) + '%')
#         print('Expected return betting black =', 
#               str(100*totBlack/numSpins) + '%')
#         print('Expected return betting', luckyNumber, '=',\
#               str(100*totPocket/numSpins) + '%\n')
#     return (totRed/numSpins, totBlack/numSpins, totPocket/numSpins)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# def newton_sqrt(n: float, x: float = 1.0) -> float:
#     """
#     Compute the square root of n using the Newton-Raphson method.
    
#     Args:
#     - n: The number for which we want to compute the square root.
#     - x: An initial guess for the square root of n.
    
#     Returns:
#     - The square root of n.
#     """
#     # Set the tolerance for the difference between x and the true root.
#     tolerance = 1e-10

#     # Iterate until the difference between x and the true root is within the tolerance.
#     while abs(x * x - n) > tolerance:
#         # Use the Newton-Raphson update formula to compute a new estimate for the root.
#         x = x - (x * x - n) / (2 * x)
        
#     return x


# n=input("Give me a Number? ")
# print(newton_sqrt(float(n)))

# # Test the function with some example values.
# # print(newton_sqrt(2.0))
# # print(newton_sqrt(16.0))
# # print(newton_sqrt(4.0))
