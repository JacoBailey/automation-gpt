import pyinputplus as pyip

def confirm_input(prompt, input_type, no_test=False):
    while True:
        user_input = input(prompt + '\n')
        answer = pyip.inputYesNo(prompt=f'You have entered "{user_input}" as {input_type}.\nIs this correct?\n')
        if answer == 'no':
            if no_test:
                return False
            continue
        return user_input
    
def yes_to_continue(prompt_arg, test=False):
    while True:
        response = pyip.inputYesNo(prompt=prompt_arg)
        if response != 'yes':
            if test:
                return True
            print('Answer other than "yes" provided.')
            continue
        else:
            if test:
                return True
            break