import pyinputplus as pyip

def inputCorrectValidation(prompt, inputType):
    while True:
        print(prompt)
        userInput = input()
        print(f'You have entered \'{userInput}\' as {inputType}.\nIs this correct?')
        yesNo = pyip.inputYesNo()
        if yesNo == 'no':
            continue
        else:
            return userInput