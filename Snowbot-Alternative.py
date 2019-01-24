#STRAT 2

from random import*

def getMove( myScore, myBalls, myDucksUsed, myMovesSoFar, oppScore, oppBalls, oppDucksUsed, oppMovesSoFar ):
    
    reloadProb= 30 # reload prob higher because it gives us a better advantage
    throwProb= 10
    duckProb= 10

# Situations for oppBalls
    if oppBalls == 0:#if opp has no balls
       duckProb= 0 #we are never going to duck because opp have no balls
       throwProb= throwProb*10
       reloadProb= reloadProb*0.05 
 
    elif oppBalls >= 5: #opponent has a large amount of snowballs --> they are more likely to throw
        duckProb= duckProb*10 #increase our probability of ducking
        
    elif oppBalls >= 3:
        duckProb= duckProb*5
            
# Situations for oppDucksUsed
    if oppDucksUsed== 5: #they have no ducks left
        throwProb= throwProb*20

    elif oppDucksUsed ==3 or oppDucksUsed ==4: #they have 1 or 2 ducks left
        throwProb= throwProb*10

    else: #they only used one or two ducks
        throwProb= throwProb*0.1 #because they are more likely to duck if they have a lot left       

# Situations for oppMovesSoFar
    for i in range (len(oppMovesSoFar)):
        if len(oppMovesSoFar) >=2:
            if oppMovesSoFar[-1] == oppMovesSoFar[-2]: #If opponent does the same move two times in a row
                if oppMovesSoFar[-1] == "THROW": #they are less likely to throw next time
                    throwProb=throwProb*20
                     
                elif oppMovesSoFar[-1] == "RELOAD": #they are more likely to throw
                    throwProb= throwProb*0.1
                    duckProb=duckProb*15
                    reloadProb=reloadProb*0.1
     
                elif oppMovesSoFar[-1] == "DUCK": #they are less likely to duck
                    throwProb=throwProb*15
                    reloadProb=reloadProb*0.1
                    duckProb=duckProb*10

# Situations for myBalls
    if myBalls > (oppBalls+ (1-oppDucksUsed)):
        throwProb=throwProb*50 #they have a disadvantage, so we continuosuly throw

    else:
        if myBalls==0:
            reloadProb=reloadProb*20
            duckProb= duckProb*20
        elif myBalls>=7:
            throwProb= throwProb*20
            duckProb= duckProb*0.05
            reloadProb= reloadProb*0.05

        elif myBalls >=3:
            throwProb= throwProb*10
            duckProb= duckProb*0.1
            reloadProb= reloadProb*0.1

        else: #we only have 1 or 2 balls
            throwProb= throwProb*0.08
            duckProb= duckProb*5
            reloadProb=reloadProb*10

# Situations for myDucksUsed
    if myDucksUsed== 0:
        duckProb= duckProb*20
        throwProb= throwProb*0.1

    elif myDucksUsed==3 or myDucksUsed==4:
        duckProb=duckProb*10

    else:
        duckProb=duckProb*0.1
        throwProb=throwProb*10
        
# Situations for Scores
    if oppScore - myScore >= 1: #they are winning
        duckProb= duckProb*10 #we duck more to play it safe
        reloadProb= reloadProb*0.05 #significantly decrease our reload to prevent being hit

    elif myScore - oppScore >= 1: #we are winning:
        duckProb= duckProb*0.1
        throwProb= throwProb*10


# DONT CHEAT 

    if myBalls==0: #preventcheating
        throwProb= 0

    if myBalls>=10: #preventcheating
        reloadProb = 0

    if myDucksUsed==5: #preventcheating
        duckProb = 0

    reloadProb2 = reloadProb/(reloadProb+throwProb+duckProb)
    throwProb2 = throwProb/(reloadProb+throwProb+duckProb)
    duckProb2 = duckProb/(reloadProb+throwProb+duckProb)
    return choice(["RELOAD"]*int(reloadProb2*100) +["THROW"]*int(throwProb2*100) +["DUCK"]*int(duckProb2*100))

