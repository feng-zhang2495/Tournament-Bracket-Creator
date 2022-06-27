#############################################
# Programmer: Feng Zhang
# Date: 2021-10-13
# Purpose: To create an infinite tournament
#          bracket with x elimination rounds.
#############################################

#Initialize Tkinter
from tkinter import*
myInterface = Tk()
myInterface.title("Tournament Bracket")
screen = Canvas( myInterface, width=800, height=600, background="black")
screen.pack()

#Width and height of canvas
width = 800
height = 600


#User Input for number of elimination rounds
rounds = int(input("Enter the amount of elimination rounds you wish to have:\n"))


#Formula for sum of a geometric series, since the total number of brackets results in a geometric series.
sumBrackets = 2**(rounds+1)-1

#Height of each bracket
bracketHeight = height/sumBrackets

#Width of each bracket (I assumed each red line had 1/2 the width of each bracket)
bracketWidth = width/(rounds+1+rounds/2)



#This array stores the heights of each bracket in the current column, so that the program knows where to draw the rectangles/lines. (Starts at 300 height)
currentHeights = [300]

#For each elimination round (Each column)
for elim in range(rounds+1):

  #After the first elim round is drawn (most right round)
  if elim > 0:
    
    #Remove the previous bracket heights from the heights array
    del currentHeights[:2**(elim-1)]

    #Update the x position for our current column
    width = width-bracketWidth-bracketWidth/2

    #Sort all new bracket heights by lowest to highest
    currentHeights.sort()

  #For each bracket in the column
  for bracket in range(0, 2**elim):

    #Creates the rectanglular bracket
    screen.create_rectangle(width, currentHeights[bracket]-bracketHeight/2, width-bracketWidth, currentHeights[bracket]+bracketHeight/2, fill='yellow', outline='')

  
    #First branching out line "<-""
    screen.create_line(width-bracketWidth, currentHeights[bracket], width-bracketWidth-bracketWidth/4,currentHeights[bracket], fill='red')

    #Second "split" line "|""
    screen.create_line(width-bracketWidth-bracketWidth/4, currentHeights[bracket]-currentHeights[0]/2, width-bracketWidth-bracketWidth/4, currentHeights[bracket]+currentHeights[0]/2, fill='red')

    #Upper left line after split 
    screen.create_line(width-bracketWidth-bracketWidth/4, currentHeights[bracket]-currentHeights[0]/2, width-bracketWidth-bracketWidth/2,currentHeights[bracket]-currentHeights[0]/2, fill='red')

    #Lower left Line after split 
    screen.create_line(width-bracketWidth-bracketWidth/4, currentHeights[bracket]+currentHeights[0]/2, width-bracketWidth-bracketWidth/2,currentHeights[bracket]+currentHeights[0]/2, fill='red')

    #Find the new updated heights of the new brackets and add them to the end of the heights list. 
    currentHeights.append(currentHeights[bracket]-currentHeights[0]/2)
    currentHeights.append(currentHeights[bracket]+currentHeights[0]/2)
    
#Updates the canvas
screen.update()

#END OF PROGRAM