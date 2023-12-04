########################################
# Name:Jordan Fasolt-Holmes
# Collaborators (if any):
# Estimated time spent (hr): 4 days
########################################

from WordleGraphics import WordleGWindow
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_COLS, N_ROWS
import random
currentRow = 0
def wordle():
    wordOfTheDay = random.choice(FIVE_LETTER_WORDS)
    firstLetter = wordOfTheDay[0]
    secondLetter = wordOfTheDay[1]
    thirdLetter = wordOfTheDay[2]
    fourthLetter = wordOfTheDay[3]
    fifthLetter = wordOfTheDay[4]
    def enter_action():
        """ What should happen when the RETURN or ENTER key is pressed. """
        global currentRow
        userWord = gw.get_square_letter(currentRow, N_COLS-5) + gw.get_square_letter(currentRow, N_COLS-4) + gw.get_square_letter(currentRow, N_COLS-3) + gw.get_square_letter(currentRow, N_COLS-2) + gw.get_square_letter(currentRow, N_COLS-1)
        userWord = userWord.lower()
        if  userWord in FIVE_LETTER_WORDS:
            firstLetterOfInput = gw.get_square_letter(currentRow, N_COLS-5)
            firstLetterOfInput = firstLetterOfInput.lower()
            secondLetterOfInput = gw.get_square_letter(currentRow, N_COLS-4)
            secondLetterOfInput = secondLetterOfInput.lower()
            thirdLetterOfInput = gw.get_square_letter(currentRow, N_COLS-3)
            thirdLetterOfInput = thirdLetterOfInput.lower()
            fourthLetterOfInput = gw.get_square_letter(currentRow, N_COLS-2)
            fourthLetterOfInput = fourthLetterOfInput.lower()
            fifthLetterOfInput = gw.get_square_letter(currentRow, N_COLS-1)
            fifthLetterOfInput = fifthLetterOfInput.lower()
            #Checks word to see if the word was guessed correctly first try
            if userWord == wordOfTheDay:
                if firstLetterOfInput == firstLetter:
                    firstLetterOfInput = firstLetterOfInput.upper()
                    gw.set_key_color(firstLetterOfInput, CORRECT_COLOR)
                if secondLetterOfInput == secondLetter:
                    secondLetterOfInput = secondLetterOfInput.upper()
                    gw.set_key_color(secondLetterOfInput, CORRECT_COLOR)
                if thirdLetterOfInput == thirdLetter:
                    thirdLetterOfInput = thirdLetterOfInput.upper()
                    gw.set_key_color(thirdLetterOfInput, CORRECT_COLOR)
                if fourthLetterOfInput == fourthLetter:
                    fourthLetterOfInput = fourthLetterOfInput.upper()
                    gw.set_key_color(fourthLetterOfInput, CORRECT_COLOR)
                if fifthLetterOfInput == fifthLetter:
                    fifthLetterOfInput = fifthLetterOfInput.upper()
                    gw.set_key_color(fifthLetterOfInput, CORRECT_COLOR)
                for x in range(5, 0, -1):
                    gw.set_square_color(currentRow, N_COLS-x, CORRECT_COLOR)
                gw.show_message("Congratulations!")
                
            else:
            #Checks first letter and sets key color to see if it is in the correct spot, is present, or if its missing from the word
                if firstLetterOfInput in wordOfTheDay and firstLetter == firstLetterOfInput:
                    gw.set_square_color(currentRow, N_COLS-5, CORRECT_COLOR)
                    firstLetterOfInput = firstLetterOfInput.upper()
                    if gw.get_key_color(firstLetterOfInput) == PRESENT_COLOR:
                        gw.set_key_color(firstLetterOfInput, PRESENT_COLOR)
                    elif gw.get_key_color(firstLetterOfInput) == MISSING_COLOR:
                        gw.set_key_color(firstLetterOfInput, MISSING_COLOR)
                    else:
                        gw.set_key_color(firstLetterOfInput, CORRECT_COLOR)
                elif firstLetterOfInput in wordOfTheDay:
                    gw.set_square_color(currentRow, N_COLS-5, PRESENT_COLOR)
                    firstLetterOfInput = firstLetterOfInput.upper()
                    if gw.get_key_color(firstLetterOfInput) == CORRECT_COLOR:
                        gw.set_key_color(firstLetterOfInput, CORRECT_COLOR)
                    elif gw.get_key_color(firstLetterOfInput) == MISSING_COLOR:
                        gw.set_key_color(firstLetterOfInput, MISSING_COLOR)
                    else:
                        gw.set_key_color(firstLetterOfInput, PRESENT_COLOR)
                else:
                    gw.set_square_color(currentRow, N_COLS-5, MISSING_COLOR)
                    firstLetterOfInput = firstLetterOfInput.upper()
                    if gw.get_key_color(firstLetterOfInput) == CORRECT_COLOR:
                        gw.set_key_color(firstLetterOfInput, CORRECT_COLOR)
                    elif gw.get_key_color(firstLetterOfInput) == PRESENT_COLOR:
                        gw.set_key_color(firstLetterOfInput, MISSING_COLOR)
                    else:
                        gw.set_key_color(firstLetterOfInput, MISSING_COLOR)
            #Checks second letter and sets key color to see if it is in the correct spot, is present, or if its missing from the word  
                if secondLetterOfInput in wordOfTheDay and secondLetter == secondLetterOfInput:
                    gw.set_square_color(currentRow, N_COLS-4, CORRECT_COLOR)
                    secondLetterOfInput = secondLetterOfInput.upper()
                    if gw.get_key_color(secondLetterOfInput) == PRESENT_COLOR:
                        gw.set_key_color(secondLetterOfInput, PRESENT_COLOR)
                    elif gw.get_key_color(secondLetterOfInput) == MISSING_COLOR:
                        gw.set_key_color(secondLetterOfInput, MISSING_COLOR)
                    else:
                        gw.set_key_color(secondLetterOfInput, CORRECT_COLOR)
                elif secondLetterOfInput in wordOfTheDay:
                    gw.set_square_color(currentRow, N_COLS-4, PRESENT_COLOR)
                    secondLetterOfInput = secondLetterOfInput.upper()
                    if gw.get_key_color(secondLetterOfInput) == CORRECT_COLOR:
                        gw.set_key_color(secondLetterOfInput, CORRECT_COLOR)
                    elif gw.get_key_color(secondLetterOfInput) == MISSING_COLOR:
                        gw.set_key_color(secondLetterOfInput, MISSING_COLOR)
                    else:
                        gw.set_key_color(secondLetterOfInput, PRESENT_COLOR)
                else:
                    gw.set_square_color(currentRow, N_COLS-4, MISSING_COLOR)
                    secondLetterOfInput = secondLetterOfInput.upper()
                    if gw.get_key_color(secondLetterOfInput) == CORRECT_COLOR:
                        gw.set_key_color(secondLetterOfInput, CORRECT_COLOR)
                    elif gw.get_key_color(secondLetterOfInput) == PRESENT_COLOR:
                        gw.set_key_color(secondLetterOfInput, PRESENT_COLOR)
                    else:
                        gw.set_key_color(secondLetterOfInput, MISSING_COLOR)
            #Checks third letter and sets key color to see if it is in the correct spot, is present, or if its missing from the word
                if thirdLetterOfInput in wordOfTheDay and thirdLetter == thirdLetterOfInput:
                    gw.set_square_color(currentRow, N_COLS-3, CORRECT_COLOR)
                    thirdLetterOfInput = thirdLetterOfInput.upper()
                    if gw.get_key_color(thirdLetterOfInput) == PRESENT_COLOR:
                        gw.set_key_color(thirdLetterOfInput, PRESENT_COLOR)
                    elif gw.get_key_color(thirdLetterOfInput) == MISSING_COLOR:
                        gw.set_key_color(thirdLetterOfInput, MISSING_COLOR)
                    else:
                        gw.set_key_color(thirdLetterOfInput, CORRECT_COLOR)
                elif thirdLetterOfInput in wordOfTheDay:
                    gw.set_square_color(currentRow, N_COLS-3, PRESENT_COLOR)
                    thirdLetterOfInput = thirdLetterOfInput.upper()
                    if gw.get_key_color(thirdLetterOfInput) == CORRECT_COLOR:
                        gw.set_key_color(thirdLetterOfInput, CORRECT_COLOR)
                    elif gw.get_key_color(thirdLetterOfInput) == MISSING_COLOR:
                        gw.set_key_color(thirdLetterOfInput, MISSING_COLOR)
                    else:
                        gw.set_key_color(thirdLetterOfInput, PRESENT_COLOR)
                else:
                    gw.set_square_color(currentRow, N_COLS-3, MISSING_COLOR)
                    thirdLetterOfInput = thirdLetterOfInput.upper()
                    if gw.get_key_color(thirdLetterOfInput) == PRESENT_COLOR:
                        gw.set_key_color(thirdLetterOfInput, PRESENT_COLOR)
                    elif gw.get_key_color(thirdLetterOfInput) == CORRECT_COLOR:
                        gw.set_key_color(thirdLetterOfInput, CORRECT_COLOR)
                    else:
                        gw.set_key_color(thirdLetterOfInput, MISSING_COLOR)     
            #Checks fourth letter and sets key color to see if it is in the correct spot, is present, or if its missing from the word
                if fourthLetterOfInput in wordOfTheDay and fourthLetter == fourthLetterOfInput:
                    gw.set_square_color(currentRow, N_COLS-2, CORRECT_COLOR)
                    fourthLetterOfInput = fourthLetterOfInput.upper()
                    if gw.get_key_color(fourthLetterOfInput) == PRESENT_COLOR:
                        gw.set_key_color(fourthLetterOfInput, PRESENT_COLOR)
                    elif gw.get_key_color(fourthLetterOfInput) == MISSING_COLOR:
                        gw.set_key_color(fourthLetterOfInput, MISSING_COLOR)
                    else:
                        gw.set_key_color(fourthLetterOfInput, CORRECT_COLOR)
                elif fourthLetterOfInput in wordOfTheDay:
                    gw.set_square_color(currentRow, N_COLS-2, PRESENT_COLOR)
                    fourthLetterOfInput = fourthLetterOfInput.upper()
                    if gw.get_key_color(fourthLetterOfInput) == CORRECT_COLOR:
                        gw.set_key_color(fourthLetterOfInput, CORRECT_COLOR)
                    elif gw.get_key_color(fourthLetterOfInput) == MISSING_COLOR:
                        gw.set_key_color(fourthLetterOfInput, MISSING_COLOR)
                    else:
                        gw.set_key_color(fourthLetterOfInput, PRESENT_COLOR)
                else:
                    gw.set_square_color(currentRow, N_COLS-2, MISSING_COLOR)
                    fourthLetterOfInput = fourthLetterOfInput.upper()
                    if gw.get_key_color(fourthLetterOfInput) == PRESENT_COLOR:
                        gw.set_key_color(fourthLetterOfInput, PRESENT_COLOR)
                    elif gw.get_key_color(fourthLetterOfInput) == CORRECT_COLOR:
                        gw.set_key_color(fourthLetterOfInput, CORRECT_COLOR)
                    else:
                        gw.set_key_color(fourthLetterOfInput, MISSING_COLOR)
            #Checks fifth letter and sets key color to see if it is in the correct spot, is present, or if its missing from the word
                if fifthLetterOfInput in wordOfTheDay and fifthLetter == fifthLetterOfInput:
                    gw.set_square_color(currentRow, N_COLS-1, CORRECT_COLOR)
                    fifthLetterOfInput = fifthLetterOfInput.upper()
                    if gw.get_key_color(fifthLetterOfInput) == PRESENT_COLOR:
                        gw.set_key_color(fifthLetterOfInput, PRESENT_COLOR)
                    elif gw.get_key_color(fifthLetterOfInput) == MISSING_COLOR:
                        gw.set_key_color(fifthLetterOfInput, MISSING_COLOR)
                    else:
                        gw.set_key_color(fifthLetterOfInput, CORRECT_COLOR)
                elif fifthLetterOfInput in wordOfTheDay:
                    gw.set_square_color(currentRow, N_COLS-1, PRESENT_COLOR)
                    fifthLetterOfInput = fifthLetterOfInput.upper()
                    if gw.get_key_color(fifthLetterOfInput) == CORRECT_COLOR:
                        gw.set_key_color(fifthLetterOfInput, CORRECT_COLOR)
                    elif gw.get_key_color(fifthLetterOfInput) == MISSING_COLOR:
                        gw.set_key_color(fifthLetterOfInput, MISSING_COLOR)
                    else:
                        gw.set_key_color(fifthLetterOfInput, PRESENT_COLOR)
                else:
                    gw.set_square_color(currentRow, N_COLS-1, MISSING_COLOR)
                    fifthLetterOfInput = fifthLetterOfInput.upper()
                    if gw.get_key_color(fifthLetterOfInput) == PRESENT_COLOR:
                        gw.set_key_color(fifthLetterOfInput, PRESENT_COLOR)
                    elif gw.get_key_color(fifthLetterOfInput) == CORRECT_COLOR:
                        gw.set_key_color(fifthLetterOfInput, CORRECT_COLOR)
                    else:
                        gw.set_key_color(fifthLetterOfInput, MISSING_COLOR)
            currentRow = gw.get_current_row()+1
            gw.set_current_row(currentRow)
        else:
            gw.show_message("Not in word list")
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup boilerplate
if __name__ == "__main__":
    wordle()
