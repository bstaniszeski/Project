#This program allows the user to input words to create a sentence
#The program will keep having a user input words until the user presses an exclaimation point (!)
#to signify completion of the user input

#Variables used: sentence, wordsInput, wordCount, listCapitalization
def main():

    try:

        sentence = [] #Creates list, input, and the count of inputs

        wordsInput = input("Enter words to create a sentence." '\n'
                       "When done enter an exclamation mark (!) instead of a word: ")
        wordCount = 0
                   

        while wordsInput != "!":        #Creates loop, puts input in list
                                    #Adds number of inputs
            sentence.append(wordsInput) 

            wordsInput = input("Enter another word, enter an exclamation mark (!) when done: ")

            wordCount = wordCount + 1


        listCapitalization = (sentence[0].capitalize(), *sentence[1:])

        print()
                                           
        print(*listCapitalization,end='. ') #Capitalizes first word, prints sentence, and
                                        #Displays number of inputs
        print()

        print ("There are",wordCount,"words in the sentence.")

    except:

        print ("No words were entered.")

main()
        

