from textblob import TextBlob

#Checks for spelling errors only
def spell(checked):
    for i in range(len(checked)):
        # Correct spelling and ensure the result is a string
        checked[i] = str(TextBlob(checked[i]).correct())
    
    return checked
#Need to implement the grammer checker next
