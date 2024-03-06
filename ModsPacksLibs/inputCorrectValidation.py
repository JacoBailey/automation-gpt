import pyinputplus as pyip

def inputCorrectValidation(prompt, inputType):
    while True:
        userInput = input(prompt + '\n')
        yesNo = pyip.inputYesNo(prompt=f'You have entered \'{userInput}\' as {inputType}.\nIs this correct?\n')
        if yesNo == 'no':
            continue
        else:
            return userInput