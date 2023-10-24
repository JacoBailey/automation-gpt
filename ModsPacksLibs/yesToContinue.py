import pyinputplus as pyip

def yesToContinue(prompt):
    print(prompt)
    while True:
        response = pyip.inputYesNo()
        if response != 'yes':
            print('Answer other than \'yes\' provided.')
            continue
        else:
            break