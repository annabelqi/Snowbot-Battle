from math import *
from time import *
from random import *


def guessMove(myScore, mySnowballs, myDucksUsed, myMoveHistory, opponentsScore, opponentsSnowballs, opponentsDucksUsed, opponentsMoveHistory):
    global guess    
    if opponentsSnowballs == 0: #when the opponent has no snowballs left

        if mySnowballs == 0: #if we have no snowballs
            guess = "RELOAD"
            counter = "RELOAD"

        else: #if we have snowballs

            if opponentsDucksUsed == 5: #opponent has no ducks
                guess = "RELOAD"
                counter = "THROW"
            elif opponentsDucksUsed == 4: #opponent has one duck left

                if opponentsScore > myScore: #if opponent is leading in score
                    guess = "RELOAD"
                    counter = "THROW"
                else:
                    guess = "DUCK"
                    counter = "RELOAD"
            else:
                guess = "DUCK"
                counter = "RELOAD"

    elif 1 <= opponentsSnowballs <= 3: #when the opponent has 1-3 snowballs

        if mySnowballs == 0: #we have no snowballs
            
            if opponentsDucksUsed == 5:
                
                if myDucksUsed == 5: #we have no ducks
                    guess = "THROW"
                    counter = "RELOAD"
                else:

                    if myScore > opponentsScore :
                        guess = "THROW"
                        counter = "RELOAD"
                    else:
                        guess = "THROW"
                        counter = "DUCK"
            else:
                
                if myDucksUsed == 5: #we have no ducks
                    guess = "THROW"
                    counter = "RELOAD"
                else:
                    if myScore > opponentsScore:
                        if myDucksUsed < opponentsDucksUsed:
                            guess = "THROW"
                            counter = "DUCK"
                        else:
                            guess = "THROW"
                            counter = "RELOAD"
                        
                    else:
                        guess = "THROW"
                        counter = "DUCK"

        elif 1 <= mySnowballs <= 3:
            
            if opponentsDucksUsed == 5:
                
                if myDucksUsed == 5: #we have no ducks

                    if opponentsSnowballs > mySnowballs:

                        if myScore > opponentsScore:  
                            guess = "THROW"
                            counter = "RELOAD"
                        else:
                            guess = "THROW"
                            counter = "THROW"
                    else:
                        guess = "RELOAD"
                        counter = "THROW"
                        
                else: #we have ducks

                    if opponentsSnowballs > mySnowballs: #opponent has more snowballs
                        if myScore > opponentsScore:
                            guess = "THROW"
                            counter = "RELOAD"
                        else:
                            guess = "THROW"
                            counter = "DUCK"
                    else:
                        if myScore > opponentsScore:
                            guess = "THROW"
                            counter = "RELOAD"
                        else:
                            guess = "RELOAD"
                            counter = "THROW"
                        
        
            else: #opponent has ducks
                
                if myDucksUsed == 5: #we have no ducks

                    if opponentsSnowballs > mySnowballs:

                        if myScore > opponentsScore:  
                            guess = "THROW"
                            counter = "RELOAD"
                        else:
                            guess = "THROW"
                            counter = "THROW"
                    else:
                        if myScore > opponentsScore:  
                            guess = "DUCK"
                            counter = "RELOAD"
                        else:
                            guess = "RELOAD"
                            counter = "THROW"
                        
                        
                else: #we have ducks 

                    if opponentsSnowballs > mySnowballs:
                        
                        if myScore > opponentsScore:
                            guess = "THROW"
                            counter = "RELOAD"
                        else:
                            guess = "THROW"
                            counter = "DUCK"
                    else:
                        if myScore > opponentsScore:
                            guess = "DUCK"
                            counter = "RELOAD"
                        else:
                            guess = "RELOAD"
                            counter = "THROW"


        else: #we have more than 3 snowballs
            if opponentsDucksUsed == 5:
                
                guess = "THROW"
                counter = "THROW"
        
            else: #opponents has ducks
                
                if myDucksUsed == 5: #we have no ducks


                    if myScore > opponentsScore:  
                        guess = "THROW"
                        counter = "THROW"
                    else:
                        guess = "THROW"
                        counter = "THROW"
                else:
                    if myScore > opponentsScore:  
                        guess = "DUCK"
                        counter = "RELOAD"
                    else:
                        guess = "THROW"
                        counter = "DUCK"
                        
                        

            
    else: #opponents has more than 3 snowballs
        if mySnowballs == 0: #we have no snowballs
            
            if opponentsDucksUsed == 5:
                
                if myDucksUsed == 5: #we have no ducks
                    guess = "THROW"
                    counter = "RELOAD"
                else:

                    if myScore > opponentsScore :
                        guess = "THROW"
                        counter = "RELOAD"
                    else:
                        guess = "THROW"
                        counter = "DUCK"
            else: #opponent has ducks
                
                if myDucksUsed == 5: #we have no ducks
                    guess = "THROW"
                    counter = "RELOAD"
                else:
                    if myScore > opponentsScore:
                        if myDucksUsed < opponentsDucksUsed:
                            guess = "THROW"
                            counter = "DUCK"
                        else:
                            guess = "THROW"
                            counter = "RELOAD"
                        
                    else:
                        guess = "THROW"
                        counter = "DUCK"

        elif 1 <= mySnowballs <= 3:
            
            if opponentsDucksUsed == 5:
                
                if myDucksUsed == 5: #we have no ducks

                    if myScore > opponentsScore:  
                        guess = "THROW"
                        counter = "RELOAD"
                    else:
                        guess = "THROW"
                        counter = "THROW"
                    
                        
                else: #we have ducks

                    if myScore > opponentsScore:
                        guess = "THROW"
                        counter = "THROW"
                    else:
                        guess = "THROW"
                        counter = "DUCK"
                        
        
            else: #opponent has ducks
            
                if myDucksUsed == 5: #we have no ducks

                    if myScore > opponentsScore:  
                        guess = "THROW"
                        counter = "RELOAD"
                    else:
                        guess = "THROW"
                        counter = "THROW"
                else:
                    if myScore > opponentsScore:  
                        guess = "DUCK"
                        counter = "RELOAD"
                    else:
                        guess = "THROW"
                        counter = "DUCK"
                    


        else: #we have more than 3 snowballs
            if opponentsDucksUsed == 5:
                
                if myDucksUsed == 5: #we have no ducks
                    if mySnowballs > opponentsSnowballs:
                        
                        guess = "THROW"
                        counter = "THROW"
                    else:
                        if myScore > opponentsScore:  
                            guess = "THROW"
                            counter = "RELOAD"
                        else:
                            guess = "THROW"
                            counter = "THROW"
                        
                else: #we have ducks
                    if mySnowballs > opponentsSnowballs:
                        
                        if myScore > opponentsScore:  
                            guess = "THROW"
                            counter = "THROW"
                        else:
                            guess = "THROW"
                            counter = "DUCK"
                    else:
                        if myScore > opponentsScore:  
                            guess = "THROW"
                            counter = "RELOAD"
                        else:
                            guess = "THROW"
                            counter = "DUCK"
        
            else: #opponent has ducks
                
                if myDucksUsed == 5: #we have no ducks
                    if mySnowballs > opponentsSnowballs:
                        if myScore > opponentsScore:  
                            guess = "THROW"
                            counter = "THROW"
                        else:
                            guess = "RELOAD"
                            counter = "THROW"
                    else:
                        if myScore > opponentsScore:  
                            guess = "RELOAD"
                            counter = "THROW"
                        else:
                            guess = "THROW"
                            counter = "THROW"
                        
                else: #we have ducks
                    if mySnowballs > opponentsSnowballs:
                        
                        if myScore > opponentsScore:  
                            guess = "DUCK"
                            counter = "RELOAD"
                        else:
                            guess = "RELOAD"
                            counter = "THROW"
                    else:
                        if myScore > opponentsScore:  
                            guess = "THROW"
                            counter = "THROW"
                        else:
                            guess = "THROW"
                            counter = "DUCK"
                        
                        
            

    if mySnowballs >= 10:
        counter = "THROW"

    return counter 


#MAIN FUNCTION
def getMove(myScore, mySnowballs, myDucksUsed, myMoveHistory, opponentsScore, opponentsSnowballs, opponentsDucksUsed, opponentsMoveHistory):
        
    if mySnowballs + (5 - myDucksUsed) > 30 - len(opponentsMoveHistory): #make sure that we don't waste any resources before the end of the game
        mymove2 = guessMove(myScore, mySnowballs, myDucksUsed, myMoveHistory, opponentsScore, opponentsSnowballs, opponentsDucksUsed, opponentsMoveHistory)
        if myDucksUsed == 5:
            move = "THROW"
        else:
            if guess == "THROW":
                move = "DUCK"
            else:
                move = "THROW"

        if mySnowballs == 0: #if we have no snowballs left
            move = "DUCK"

    else: 
        mymove = guessMove(myScore, mySnowballs, myDucksUsed, myMoveHistory, opponentsScore, opponentsSnowballs, opponentsDucksUsed, opponentsMoveHistory) #guess function       

        #makes sure it doesn't cheat
        if myDucksUsed == 5 and mySnowballs == 0: #if we have no snowball and ducks left
            move = "RELOAD"

        elif myDucksUsed == 5: #if we have no ducks left
            move = ["RELOAD"]*50+["THROW"]*50

        elif mySnowballs == 0: #if we have no snowballs left
            move = ["RELOAD"]*50+["DUCK"]*50

        try:
            myMoveHistory[-1]
            move = mymove
        except:
            move = "RELOAD" #first round always reload

    if mySnowballs>= 10: #reached max snowballs and doesnt matter if we have ducks left or nah
        move= "THROW" 


    
    return move
            
            


