import pyinputplus as pyip

def inputCorrectValidation(prompt, inputType, noTest=False):
    while True:
        userInput = input(prompt + '\n')
        yesNo = pyip.inputYesNo(prompt=f'You have entered \'{userInput}\' as {inputType}.\nIs this correct?\n')
        if yesNo in ['no', 'n', 'NO', 'N', 'No' 'nO']:
            if noTest == True:
                return False
            else:
                continue
        else:
            return userInput