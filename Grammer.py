from textblob import TextBlob
import language_tool_python


tool = language_tool_python.LanguageTool('en-US')


#Checks for spelling errors only
def spell(checked):
    for i in range(len(checked)):
        # Correct spelling and ensure the result is a string
        checked[i] = str(TextBlob(checked[i]).correct())
    
    return checked

#Checks for grammatical errors for User entries
def grammer(checked):
    for i in range(len(checked)):
        
        correct = tool.check(checked[i])
        final = language_tool_python.utils.correct(checked[i], correct)
        checked[i] = final
    
    return checked
