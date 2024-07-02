# Jazmin Even Dorra
# This program will play a MadLib game with the user.

def main():
    print ("MadLib Game...\n")
    print ("Enter the followring words:")
    #prompt user for words
    PNOUN1 = input("Plural Noun: ")
    FNAME = input ("Person's First Name: ")
    NOUN1 = input ("Noun: ")
    LNAME = input ("Person's Last Name: ")
    PNOUN2 = input ("Plural Noun: ")
    PLACE1 = input ("Place: ")
    PNOUN3 = input ("Plural Noun: ")
    PLACE2 = input ("Place: ")
    PNOUN4 = input ("Plural Noun: ")
    NOUN2 = input ("Noun: ")
    ADJECTIVE1 = input ("Adjective: ")
    ADJECTIVE2 = input ("Adjective: ")
    VERB = input ("Verb: ")
    ADJECTIVE3 = input ("Adjective: ")

    # Display Answers
    print ("\nThe Big Game !!!\n")
    print ("Hello there, sports ", PNOUN1, "!")
    print ("This is", FNAME, ", talking to you from the press", NOUN1)
    print ("in", LNAME, " Stadium, where 57,000 cheering", PNOUN2)
    print ("have gathered to watch (the)", PLACE1, PNOUN2)
    print ("take on (the)", PLACE2, PNOUN4)
    print ("Even though the", NOUN2, "is shining, it's a/an",ADJECTIVE1)
    print ("cold day with the temperature in the", ADJECTIVE2, "20s.")
    print ("We'll be back for the opening", VERB, "-off after a few words")
    print ("from our", ADJECTIVE3, "sponsor.")
    
main()
            
